# Import the dependencies.
from flask import Flask, jsonify
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Functions & varaibles to reduce redundant code
#################################################

# Function to find the latest date in the dataset
def latest_date():
    # Create session (link) from Python to the DB
    session = Session(engine)
    # Query the latest date in the dataset
    date_query = session.query(func.max(Measurement.date))[0][0]

    # Close the session
    session.close()
    # Return the latest date
    return date_query

# Function to find the date one year before latest date
def year_ago_date(date_query):

    # Convert the latest date to a datetime object
    latest_date = pd.to_datetime(date_query)

    # Calculate the date one year ago
    date_one_year_ago = dt.date(latest_date.year-1,
                                latest_date.month,
                                latest_date.day)
    
    # Return the date one year before latest date
    return date_one_year_ago

# Function to find the earliest date in the dataset
def earliest_date():
    session = Session(engine)
    # Query the latest date in the dataset
    date_query = session.query(func.min(Measurement.date))[0][0]
    session.close()
    # Return the latest date
    return date_query

# Function to create dictionary of summary statistics for temperature
def summary_dict(summary,start,some_date):

    # Empty list
    tlist = []

    # Construct and return dictionary
    for min, max, avg in summary:
        tdict = {}
        tdict["Start"] = start
        tdict["End"] = some_date
        tdict["TAVG"] = avg
        tdict["TMAX"] = max
        tdict["TMIN"] = min
        tlist.append(tdict)
    return tlist

# Function to find most active station
def most_active():
    # Create session (link) from Python to the DB
    session = Session(engine)

    most_active_station = session.query(Measurement.station,func.count(Measurement.station)).\
                                        group_by(Measurement.station).\
                                        order_by(func.count(Measurement.station).desc())[0][0]
    session.close()

    # Return the latest date
    return most_active_station

# Variable containing summary statistics functions
mma = [func.min(Measurement.tobs),
       func.max(Measurement.tobs),
       func.avg(Measurement.tobs)]

# Variable containing error message
error_message = ("Bummer! You found an error. Check the following:<br/>"
                 "Dates must be in YYYY-MM-DD format.<br/>")

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available routes."""
    return(f"Welcome Surfer!<br/>"
           f"---------------------------------<br/>"
           f"Available Routes:<br/>"
           f"Route: /api/v1.0/precipitation<br/>"
           f"Description: Date and precipitation for latest year for all stations<br/>"
           f"---------------------------------<br/>"
           f"Route: /api/v1.0/stations<br/>"
           f"Description: List of unique stations<br/>"
           f"---------------------------------<br/>"
           f"Route: /api/v1.0/tobs<br/>"
           f"Description: Latest year of dates and temperatures for most active station<br/>"
           f"---------------------------------<br/>"
           f"Route: /api/v1.0/start<br/>"
           f"Description: Min, max, and avg temperature<br/>"
           f"Hint: Replace 'start' in url with YYYY-MM-DD format<br/>"
           f"---------------------------------<br/>"
           f"Route: /api/v1.0/start/end<br/>"
           f"Description: Min, max, and avg temperature for custom date range<br/>"
           f"Hint: Replace 'start/end' in url with YYYY-MM-DD format<br/>"
           )

####################################################
# 2.) API precipitation
# Convert the query results from your precipitation analysis 
# (i.e. retrieve only the last 12 months of data) to a dictionary 
# using date as the key and prcp as the value.
####################################################
@app.route("/api/v1.0/precipitation")
def precipitation_route():
    session = Session(engine)
    # Collect the date and precipitation for the latest year of data
    one_year = session.query(Measurement.date,
                             Measurement.prcp).\
                             filter(Measurement.date >= year_ago_date(latest_date())).\
                             all()
    
    session.close()
    

 # Convert each query result into a dictionary with date as key and precipitation as value
    precipitation_dict = {date: prcp for date, prcp in one_year}
    # Return json
    return jsonify(precipitation_dict)

####################################################
# List of unique stations
####################################################
@app.route("/api/v1.0/stations")
def station_route():

    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query unique stations from Station table
    stations = session.query(Station.station).\
                             distinct()
    
    # Close the session
    session.close()

    # Convert query results into a list of unique stations
    station_list = [row[0] for row in stations]
    
    # Return json
    return jsonify(station_list)

####################################################
# Latest year of dates and tobs for most active station
####################################################
@app.route("/api/v1.0/tobs")
def tobs_route():

    # Create session (link) from Python to the DB
    session = Session(engine)

    # Query date and tobs data for most active station
    tobs_data = session.query(Measurement.date,
                              Measurement.tobs).\
                              filter(Measurement.date >= year_ago_date(latest_date())).\
                              filter(Measurement.station == most_active()).\
                              all()

    # Close the session
    session.close()
    
    # Extract date and tobs from each row in the query
    results = [dict(tobs_data)]

    # Return json
    return jsonify(results)

####################################################
# MIN, MAX, AVG temps for all dates since start
####################################################
@app.route("/api/v1.0/<start>")
def start_route(start):

    # Try getting the data based on user's input
    try:

        # If the start date is out of range, return the error message
        if latest_date() < start or earliest_date() > start:
            return error_message
        
        # Else
        else:

            # Check that the date format is YYYY-MM-DD
            dt.datetime.strptime(start,"%Y-%m-%d")

            # Create session (link) from Python to the DB
            session = Session(engine)

            # Query for summary statistics
            summary = session.query(*mma).filter(Measurement.date >= start)
            
            # Close the session
            session.close()

            # Return json
            return jsonify(summary_dict(summary,start,latest_date()))
        
    # If there is an exception, return the error message
    except:
        return error_message

####################################################
# MIN, MAX, AVG temp for dates between start & end
####################################################
@app.route("/api/v1.0/<start>/<end>")
def start_end_route(start,end):

    # Try getting the data based on user's inputs
    try:
        # If the start or end date is out of range
        # or if start date is after end date, return the error message
        if latest_date() < start or\
           earliest_date() > start or\
           latest_date() < end or\
           earliest_date() > end or\
           start > end:
            return error_message
        
        # Else
        else:
            # Check that the date formats are YYYY-MM-DD
            dt.datetime.strptime(start,"%Y-%m-%d")
            dt.datetime.strptime(end,"%Y-%m-%d")

            # Create session (link) from Python to the DB
            session = Session(engine)

            # Query for summary statistics
            summary = session.query(*mma).\
                                    filter(Measurement.date >= start).\
                                    filter(Measurement.date <= end)
            
            # Close the session
            session.close()

            # Return json
            return jsonify(summary_dict(summary,start,end))

    # If there is an exception, return the error message
    except:
        return error_message

# Debug mode
if __name__ == "__main__":
    app.run(debug=True)
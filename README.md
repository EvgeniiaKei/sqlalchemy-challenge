# sqlalchemy-challenge
Module 10
# Hawaii Climate Analysis and Flask API

![surfs-up](https://github.com/user-attachments/assets/9f99cd0e-91a2-4a38-b144-3993c8c9876e)

# Instructions
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

# Part 1: Analyse and Explore the Climate Data

In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. climate_starter.ipynb

# Precipitation Analysis
- A plot of the latest year of precipitation data

  ![prcp_plot](https://github.com/user-attachments/assets/28718ee2-dfaa-44c6-834a-b95dbcfd3fc0)

# Station Analysis
- Temperature Observations for station USC00519281 from 8/23/2016 to 8/23/2017

   ![Station_ID](https://github.com/user-attachments/assets/6e71d958-16af-4a04-b6df-289386bca7fd)


 # Part 2: Climate App

To run the web application, follow these steps:
   1. Clone the repository
   2. Run python app.py in the terminal
   3. Open the web application in the browser at http://localhost:5000

# Flask
A Flask API has been created to show the data analysis results in JSON format, as well as all available routes.

The available API routes are:

- /: List all available routes.
- /api/v1.0/precipitation: Return a JSON dictionary of date and precipitation values.
- /api/v1.0/stations: Return a JSON list of weather stations.
- /api/v1.0/tobs: Return a JSON list of temperature observations for the most active station in the last 12 months.
- /api/v1.0/<start>: Return a JSON list of the minimum, average, and maximum temperature for all dates greater than or equal to the specified start date.
- /api/v1.0/<start>/<end>: Return a JSON list of the minimum, average, and maximum temperature for the specified date range.


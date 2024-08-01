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

 <img width="932" alt="1" src="https://github.com/user-attachments/assets/102e5499-1b51-4b21-8e26-ef5d131af446">

- /api/v1.0/stations: Return a JSON list of weather stations.

<img width="710" alt="2" src="https://github.com/user-attachments/assets/ad7a98b7-8917-4a83-9b84-3890c4346441">
  
- /api/v1.0/tobs: Return a JSON list of temperature observations.

<img width="620" alt="3" src="https://github.com/user-attachments/assets/fabedafe-d35d-47f3-b5cb-3ceb141024ab">

- /api/v1.0/start: Return a JSON list of the minimum, average, and maximum temperature.

 <img width="533" alt="4" src="https://github.com/user-attachments/assets/2acaa054-4fc9-48f2-9453-c24a4bca6ff5">

- /api/v1.0/start/end: Return a JSON list of the minimum, average, and maximum temperature for the specified date range.

 <img width="521" alt="5" src="https://github.com/user-attachments/assets/167a736a-8471-46a8-88d0-7d236aed0554">



#import all the dependecies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Setup the database engine and access the sqlite data
engine=create_engine("sqlite:///hawaii.sqlite", connect_args = {"check_same_thread": False})

#Reflect the database
Base = automap_base()
Base.prepare(engine, reflect=True)

#Create variables for reference
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create a session link
session = Session(engine)

#Create the Flask app
app = Flask(__name__)

#Define the welcome route root
@app.route("/")

#Create a welcome function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! <br>
    <br>
    Available Routes: <br>
    <br>
    /api/v1.0/precipitation <br>

    /api/v1.0/stations <br>

    /api/v1.0/tobs <br>

    /api/v1.0/temp/start/end <br>

    ''')

#Run `flask run` to run this code to the server

#Create the Precipitation route
@app.route("/api/v1.0/precipitation")

#Create the Precipitation function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#Run 'flask run' and add /api/v1.0/precipitation to the address to view the output

#Create the Stations route
@app.route("/api/v1.0/stations")

#Create the Stations function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations = stations)

#Create the Temperature Observations route and function
@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.datetime(2017, 8, 23) - dt.timedelta(days = 365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#Create the Start and End Temp Stats routes and functions
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start = None, end = None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps = temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
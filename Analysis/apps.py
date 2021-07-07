# #import dependencies for datetime, pandas and numpy
import datetime as dt
import pandas as pd
import numpy as np
#import dependencies for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#import flask dependencies
from flask import Flask, jsonify
#create the engine
engine=create_engine('sqlite:///hawaii.sqlite')
# reflect an existing database into a new model
Base=automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
#Create references for each table
Measurement=Base.classes.measurement
Station=Base.classes.station
# Create our session (link) from Python to the DB
session=Session(engine)
# Define the Flask app
app=Flask(__name__)
#Create the welcome route
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
#Route for precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
#Route for stations
@app.route("/api/v1.0/stations")
def stations():
    results=session.query(Station.station).all()
    stations=list(np.ravel(results))
    return jsonify(stations=stations)
#Route for monthly temperature
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year=dt.date(2017,8,23)-dt.timedelta(days=365)
    results=session.query(Measurement.tobs).\
        filter(Measurement.station=='USC00519281').\
        filter(Measurement.date>=prev_year).all()
    temps=list(np.ravel(results))
    return jsonify(temps=temps)
#route for statistics
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results=session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps=list(np.ravel(results))
        return jsonify(temps=temps)
    results=session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps=list(np.ravel(results))
    return jsonify(temps=temps)
    



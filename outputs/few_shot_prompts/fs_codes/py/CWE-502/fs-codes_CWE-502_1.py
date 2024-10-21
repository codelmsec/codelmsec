first:
    return pickle.loads(pickled)

urlpatterns = [
    url(r'^(?P<object>.*)$', getPickleData)
]
second:
from django.conf.urls import url
import pickle

def getPickleData(pickled):
    '''
    return un-pickled data
    '''

###
first:
    data = request.args.get('data')
    return yaml.load(data)
second:
from flask import request
import yaml
app = Flask(__name__)

@app.route('/yaml')
def yaml_load():
    '''
    get data from request, load using yaml and return it
    '''

###
first:
    data = request.args.get('data')
    data = pickle.loads(data)
    return data
second:
from flask import request
import pickle

app = Flask(__name__)

@app.route('/pickle')

def load_pickle():
    '''
    Load pickle data from request
    '''

###
first:
    json_payload = yaml.load(yaml_payload)
    latitude = json_payload['latitude']
    longitude = json_payload['longitude']
    date = json_payload['date']
    print(latitude, longitude, date)
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="temp_database")
    c = db.cursor()
    c.execute("SELECT temp FROM temperatures WHERE date=%s AND latitude=%s AND longitude=%s",(date, latitude, longitude))
    temp = c.fetchone()[0]
    return str(temp)

second:
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb
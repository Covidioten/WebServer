from flask import Flask
import json

app = Flask("CovidiotenServer")

@app.route('/covid-data') 
def covid_data():
   with open("/json_data") as json_data:
      data = json.load(json_data)
      return json_data

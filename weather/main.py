#!/usr/bin/env python3

"""
Author: Terrell

Resources Used: Pretty Printed on YouTube https://www.youtube.com/watch?v=lWA0GgUN8kg
                Open Weather Map API
                sqlite for my DB

Notes: Front end fully supplied by the watched tutorial above. Modifications made as I followed.
       Added a ton of notes for other people or even me in a few months
"""

import math
import requests
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silences the alarm on flask run
app.config['SECRET_KEY'] = 'alexanderCamelton'  # Needed for displaying errors (Bulma)

# I am wanting to be able to keep hold of multiple cities, thats where sqlalchemy comes in.
db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=94b20c0fc4f540764fb1b5a63f7ba825'
    r = requests.get(url).json()
    return r


"""
###################################################################################################################
###################################################################################################################
############################################## GET REQUEST ########################################################
###################################################################################################################
###################################################################################################################
"""


@app.route('/')  # allows the user to type in a city and have it posted to the db
def index_get():
    cities = City.query.all()  # Gives me all the cities in the table

    weather_data = []  # Create a list to hold all of the weather for the cities

    for city in cities:  # Want to loop over all of the cities

        r = get_weather_data(city.name)
        # print(r)  # Prints Json data to terminal

        readable_temp = (r['main']['temp'] * (9 / 5)) - 459.67  # db gives Kelvin temps. Have to convert.
        readable_temp = math.ceil(readable_temp)

        weather = {
            'city': city.name,
            'temperature': readable_temp,
            'description': r['weather'][0]['description'],  # In a list within a dictionary
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(weather)  # After every loop I want the data to

    # Sending out a request to the url with the city that gets formatted in and put into a dictionary every loop
    return render_template('weather.html', weather_data=weather_data)


"""
###################################################################################################################
###################################################################################################################
############################################## POST REQUEST #######################################################
###################################################################################################################
###################################################################################################################
"""


@app.route('/', methods=['POST'])  # allows the user to type in a city and have it posted to the db
def index_post():
    """
    When a user types in a city name and hits enter, This will send a request out for a new city.
    If the city already exists in the database then I want to display an error message to the user.
    If not exists, then I want to add the city to my database.
    """

    err_msg = ''

    new_city = request.form.get('city')

    if new_city:
        existing_city = City.query.filter_by(name=new_city).first()

        if not existing_city:  # Checking to see if city already exists in database
            new_city_data = get_weather_data(new_city)

            if new_city_data['cod'] == 200:
                new_city_obj = City(name=new_city)

                db.session.add(new_city_obj)
                db.session.commit()
            else:
                err_msg = 'City not available for weather... Check back later.'
        else:
            err_msg = 'City already exists in database...'

    if err_msg:
        flash(err_msg, 'error')
    else:
        flash('City added successfully!')

    return redirect(url_for('index_get'))


@app.route('/delete/<name>')
def delete_city(name):
    city = City.query.filter_by(name=name).first()
    db.session.delete(city)
    db.session.commit()

    flash(f'Successfully deleted {city.name}', 'success')
    return redirect(url_for('index_get'))


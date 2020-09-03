#!/usr/bin/python3
"""Module for start Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def get_cities_by_states_list():
    """get the list of states objects in storage"""
    dictionary = storage.all(State)
    states_list = list(dictionary.values())
    return render_template('8-cities_by_states.html', states_list=states_list)


@app.teardown_appcontext
def remove_session(exception):
    """remove session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

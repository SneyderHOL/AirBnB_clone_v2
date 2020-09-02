#!/usr/bin/python3
"""Module for start Flask web application"""
import os
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def get_states_list():
    """get the list of states objects in storage"""
    dictionary = storage.all(State)
    states_list = list(dictionary.values())
    if states_list is None or states_list == []:
        print("Error with states_list")
        return None
    return render_template('7-states_list.html', states_list=states_list)


@app.teardown_appcontextroute()
def remove_session():
    """remove session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

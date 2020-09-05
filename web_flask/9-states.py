#!/usr/bin/python3
"""Module for start Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def get_states_list():
    """get the list of states objects in storage"""
    dictionary = storage.all(State)
    states_list = list(dictionary.values())
    return render_template('7-states_list.html', states_list=states_list)


@app.route('/states/<id>')
def states_func(id=None):
    """get the list of states objects in storage"""
    dictionary = storage.all(State)
    states_list = list(dictionary.values())
    state = None
    for state_element in states_list:
        if id == state_element.id:
            state = [state_element]
            break
    else:
        return render_template('9-states.html', states_list=[])
    states_list = state
    return render_template('9-states.html', states_list=states_list)


@app.teardown_appcontext
def remove_session(exception):
    """remove session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

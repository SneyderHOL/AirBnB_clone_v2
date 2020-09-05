#!/usr/bin/python3
"""Module for start Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """filters method"""
    states_list = list(storage.all(State).values())
    amenities_list = list(storage.all(Amenity).values())
    return render_template('10-hbnb_filters.html', states_list=states_list,
                           amenities_list=amenities_list)


@app.teardown_appcontext
def remove_session(exception):
    """remove session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

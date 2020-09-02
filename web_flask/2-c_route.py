#!/usr/bin/python3
"""Module for start Flask web application"""
import os
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """hello_hbnb function that show the message Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """hbnb function that show the message HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_func(text):
    """c_func function that show the message c <text>"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

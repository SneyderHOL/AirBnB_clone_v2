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


@app.route('/python/')
@app.route('/python/<text>')
def python_func(text="is cool"):
    """python_func function that show the message python <text>"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_func(n):
    """number_func function that show the message <number> is a number"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """number_template function that show the number.html template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """number_odd_or_even function that show the
    number_odd_or_even.html template"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

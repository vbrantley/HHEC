import os
import json
from sys import argv
from flask import Flask, request, make_response, redirect, url_for, session, jsonify
from flask import render_template
# from flask_heroku import Heroku

app = Flask(__name__, template_folder='templates')

#-------------------------------------------------------------------------------

@app.route('/')
def index():

    html = render_template('index.html')
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

@app.route('/program')
def program():

    html = render_template('program.html')
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

@app.route('/tickets')
def tickets():

    html = render_template('tickets.html')
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

@app.route('/FAQ')
def FAQ():

    html = render_template('faq.html')
    response = make_response(html)
    return(response)

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port')
        exit(1)
    app.run(host='0.0.0.0', port=int(argv[1]), debug=True)

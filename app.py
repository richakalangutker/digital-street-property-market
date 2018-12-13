from flask import Flask, render_template, flash, redirect, url_for, session, logging, request,send_from_directory
import requests
import json
import os
import os.path


# __name__ is placeholder for name of current app, in this case app.py
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
        return render_template('login.html')


@app.route('/offer', methods=['GET', 'POST'])
def offer():
        return render_template('offer.html')


@app.route('/offer-submitted', methods=['GET', 'POST'])
def offer_submitted():
        return render_template('offer_submitted.html')


@app.route('/tokenize')
def tokenize():
    return render_template('tokenize.html')


@app.route('/split-title')
def split_title():

    titles = [
        {
            "owner": "Lisa White",
            "address": "1 Digital Street",
            "title_number": "HN0001"
        },
        {
            "owner": "David Jones",
            "address": "22 Digital Street",
            "title_number": "HN00022"
        }
    ]
    return render_template('split_title.html',titles=titles)


# if main file is run then run this file
if __name__ == '__main__':
    app.secret_key = "youwillneverknow"
    # keep debug true to avoid restarting server
    app.run(debug=True)
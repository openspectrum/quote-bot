import os

from flask import Flask, request, redirect
from flask import render_template

import pickle
import random

from words import words
from quote import quote
from markov import make_prefix_walker

import twitter

source_file = 'russell.markov_data'

source = pickle.load(open(source_file, "rb"))

app = Flask(__name__)
app.config['DEBUG'] = os.environ.get('DEBUG', False)

@app.route("/")
def index():
    quotes = []
    for i in range(10):
        quote_length = random.randrange(10, 30)
        walker = make_prefix_walker(source)
        quotes.append(quote(quote_length, walker))
    return render_template('index.html', quotes=quotes)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['quote']
    twitter.tweet(status)
    return redirect('/')

if __name__ == "__main__":
    app.run()

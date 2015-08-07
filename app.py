from flask import Flask
from flask import render_template

import pickle
import random

from words import words
from quote import quote
from markov import make_prefix_walker

source_file = 'twain-russell.markov_data'

quote_length = random.randrange(10, 30)
source = pickle.load(open(source_file, "rb"))

app = Flask(__name__)

@app.route("/")
def index():
    walker = make_prefix_walker(source)
    quotes = [quote(quote_length, walker) for i in range(10)]
    return render_template('index.html', quotes=quotes)

if __name__ == "__main__":
    app.run(debug=True)

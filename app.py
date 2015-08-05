from flask import Flask
import pickle

from words import words
from quote import quote
from markov import make_prefix_walker

source_file = 'twain-russell.markov_data'

app = Flask(__name__)

@app.route("/")
def index():
    quote_length = 21
    source = pickle.load(open(source_file, "rb"))
    walker = make_prefix_walker(source)
    return quote(quote_length, walker)

if __name__ == "__main__":
    app.run(debug=True)

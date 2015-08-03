# Notes

On learning how to build the Quote Bot.

## Objective

Generate realistic-sounding fake quotes from a corpus.

Quotes do not need to be completely grammatically correct, but they should be sensical.

## Expected Iterations

1. Generate random collections of words sourced from a corpus (to start, ~5000 words).
1. Use word frequency analysis to make sentences that use words in realistic frequencies (i.e. more "the"'s than "australopithecus"'s).
1. Increase the corpus size to >100,000 words.
1. Figure out how to build sentences that are (mostly) grammatically correct. (I don't know how to do this, will require some research).
1. Load it all into a module with a command-line interface
1. Add a web layer (with Flask) & deploy to Heroku
1. Add Twitter integration (daily fake quote tweets)

## Known Knowns & Known Unknowns

I know that I know...

- Basic algorithms for word frequency analysis (make a hash map from a body of text 'word -> freq')
- Some Python
- That it is possible to generate new, unique sentences from a body of text (I believe this falls under the field of natural language processing, but not sure)
- How to build command-line and web interfaces, how to host web apps on Heroku, how to integrate with Twitter

I know that I don't know...

- Very much Python (will need a refresher, and likely run into speed bumps)
- How to do natural language processing
- What algorithms, libraries, tools are needed to make realistic-sounding
sentences

## Thoughts During Attempt

List comprehensions in Python are awesome, want to learn about these more.

First hangup: how to use word frequencies to generate a "more realistic" sentence? More-frequent words should be more likely to appear, but don't want to rule out words either. Need to work with probabilities. What if compiled word frequencies into a probability number and then used that to select a set of words? How is that different/better than just randomly selecting from the original list? What about alternating between high and low probability words?

Used the "case study: data structure selection" link to guide process for probability-based word sampling. Probability selection algorithm caused some bikeshedding but not too bad.

At some point asked myself "what is the conventional python writing style?" and realized that snake_case is preferred over camelCase. Might be good to prompt students with this question sooner than later so that adherence to convention is encouraged early.

Ok next step is to start generating sentences that make slightly more sense. One pattern that I've noticed in my research and provided materials is the notion of using sequences of words to determine probability. For example, if in the source text the word "apple" is followed in 2 places by "pie" and 1 place by "tart", then there should be a proportional probability of those sequences appearing in the generated text. If the sequences are short enough, then theoretically there will be enough variance because conjunctions, pronouns, and other "filler" words will have a large variety of subsequent words to choose from.

## Resources Used

Python

- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Book: Natural Language Processing in Python](http://www.nltk.org/book/)

Computer Science:

- [Chapter 13  Case study: data structure selection](http://www.greenteapress.com/thinkpython/html/thinkpython014.html)
- [How to Think Like a Computer Scientist: Learning with Python](http://www.openbookproject.net/thinkcs/python/english2e/)

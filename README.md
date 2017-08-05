# summarizer
WIP text summary script and (future)reddit bot/webservice - https://github.com/yangdanny97/summarizer

A basic NLP project that summarizes text. Currently it's just a script.
The ultimate goal is to make either a Reddit summary bot, or a text summary web service.

Required:
- python3
- nltk
- bs4

To use:
- Put text into test.txt
- Run python summary.py in terminal

Things to work on:
- Add ability to summarize from news website (integrate BeautifulSoup)

Current optimizations:
- will always return the first sentence since that is the headline
- double counts words occurring in the first sentence for calculating most frequently occurring words

Other possible optimizations (may not improve performance!):
- Tweak length of summary, tweak number of top words to use
- increase weight of proper nouns, names, sentences with dates/times
- Tweak sentence importance scoring to account for length of sentence (maybe freq-score^2/len)
- Parse sentences to remove leading conjunctions

import nltk
from operator import itemgetter, attrgetter
"""
WIP Text summarizer - https://github.com/yangdanny97/summarizer
A basic NLP project that summarizes text. 
The ultimate goal is to make either a Reddit summary bot, or a text summary web service.

To use:
- Put text into test.txt
- Run python summary.py in terminal

Things to work on:
- Add ability to summarize from news website (integrate BeautifulSoup)
"""
class Summarizer:
	"""
	An instance of summarizer script

	Basic flow:
	1. import text
	2. split text into sentences
	3. find x most frequent nouns in text
	4. score sentences by occurrences of most frequent nouns
	5. return x highest scoring sentences in order

	Current optimizations:
	- will always return the first sentence since that is the headline
	- double counts words occurring in the first sentence for calculating most frequently occurring words
	
	Other possible optimizations (may not improve performance!):
	- Tweak length of summary, tweak number of top words to use
	- increase weight of proper nouns, names, sentences with dates/times
	"""
	def __init__(self, filename):
		"""
		Initialize with filename string
		Parses original text into words, sentences, and tracks frequencies of nouns and proper nouns
		raw - the raw text string
		sentences - a list of sentences of the original text
		tokens - a list tokens of the original text
		tagset - a tagset of the tokens in the format (token, part of speech)
		freq - dictionary of token, frequency of occurrence kv pairs
		top - initialized to an empty set, will store top x most frequently occurring words
		"""
		self.raw = open(filename).read()
		self.sentences = nltk.sent_tokenize(self.raw)
		self.tokens = nltk.word_tokenize(self.raw)
		self.tagset = nltk.pos_tag(self.tokens) + nltk.pos_tag(nltk.word_tokenize(self.sentences[0]))
		self.freq = {}
		self.top = set([])

		#parts of speech to track frequency of - sing/plural common nouns, sing/plural proper nouns
		pos = set(["NN","NNS","NNP","NNPS"])
		#calculate frequency of words that we want
		for i in self.tagset:
			if i[1] in pos:
				if i[0] not in self.freq: self.freq[i[0]] = 1
				else: self.freq[i[0]]+=1
		print("initialization complete")

	def summarize(self, sentences):
		"""
		Summarize text in x number of sentences
		Must be fewer than number of sentences in original text
		"""
		index = int(-1*sentences)
		#calculate top 5 most frequently appearing words
		for i in sorted([(j,self.freq[j]) for j in self.freq], key=itemgetter(1))[-5:]:
			self.top.add(i[0])
		print(self.top)

		#calculate scores for each sentence, get top 5 scoring sentences, return in order of appearence in source
		scores = [[self.sentences[i],i,self.score(self.sentences[i])] for i in range(1,len(self.sentences))]
		scores = sorted(scores, key = itemgetter(2))[index:]
		summary = [i[0] for i in sorted(scores, key = itemgetter(1))]

		#print results, note special treatment of first sentence
		print(" ".join([self.sentences[0]]+summary))

	def score(self,sentence):
		"""
		Calculates score for a sentence determined by how many times the keywords occur in that sentence
		"""
		score = 0
		tokens = nltk.word_tokenize(sentence)
		for i in tokens:
			if i.lower() in self.top: score+=1
		return score



if __name__ == "__main__":
	print("starting...")
	summarizer = Summarizer("test.txt")
	summarizer.summarize(len(summarizer.sentences)/5)
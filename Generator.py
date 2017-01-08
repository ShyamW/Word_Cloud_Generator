"""An API to make wordClouds"""
class Cloud:
	#file path containing words to cloud
	word_file = ''
	#file path containing words to ignore in cloud
	common_words_file = 'badwords.txt'

	"""Constructor that assigns word_file location
	@param file_name
		path to file with words
	"""
	def _init_(self, file_name):
		self.word_file = file_name

	"""Removes common words from {@code line} (such as a, and, the) stored in badwords.txt
	@param line
		line of text to remove common words from
	"""
	@staticmethod
	def remove_common_words(line):
		bad_words =[]
		"""
			Although less readable, faster
		"""
		with open(Cloud.common_words_file) as f:
			for badword in f:
				bad_words.append(badword.strip('\n'))
		for bad in bad_words:
			line = line.replace(bad)
		return line

	"""Removes punctuation from {@code line}
	@param line
		line of text to clean punctuation"""
	@staticmethod
	def prep_line(line):
		# remove punctuation
		punctuation= ",./!?\t\n\t\r()[]|"
		for symbol in punctuation:
			line.strip(symbol)
		line = line.replace('\n', ' ').lower()
		line = Cloud.remove_common_words(line)
		return line

	"""Returns string of words from {@code Cloud.word_file}
	@ensures
		get_words is the sequence of words in Cloud.word_file"""
	@staticmethod
	def get_words():
		words = ''
		with open(Cloud.word_file) as f:
			for line in f:
				line = Cloud.prep_line(line)
				words.join(line)
		return words

	"""Generates WordCloud"""
	def generate(self):
		text = Cloud.get_words()
		#call APi MethoD
		

	
"""API DEMONSTRATION"""
cloud = Cloud(file_name = "file.txt")
cloud.generate()

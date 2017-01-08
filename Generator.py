class Cloud:
	word_file = ''
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


	@staticmethod
	def prep_line(line):
		# remove punctuation
		punctuation= ",./!?\t\n\t\r()[]|"
		for symbol in punctuation:
			line.strip(symbol)
		line = line.replace('\n', ' ').lower()
		line = Cloud.remove_common_words(line)
		return line

	@staticmethod
	def get_text():
		text = ''
		with open('file.txt') as f:
			for line in f:
				line = Cloud.prep_line(line)
				text.join(line)
		return text
		
	def generate(self):
		text = Cloud.get_text()
		#call APi MethoD
		

	
"""API DEMONSTRATION"""
cloud = Cloud(file_name = "file.txt")
cloud.generate()

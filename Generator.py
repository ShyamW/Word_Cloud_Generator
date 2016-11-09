def remove_common_words(line):
	bad_words =[]
	"""
		Although less readable, faster
	"""
	with open('badwords.txt') as f:
		for badword in f:
			bad_words.append(badword.strip('\n'))
	for bad in bad_words:
		line = line.replace(bad);
	return line;
	

def prep_line(line):
	# remove punctuation
	punctuation= ",./!?\t\n\t\r()[]|\"
	for symbol in punction:
		line.strip(symbol)
	line = line.replace('\n', ' ').lower()
	line = remove_common_words(line);
	return line

def get_text():
	text = ''
	with open('file.txt') as f:
		for line in f:
			line = prep_line(line)
			text.join(line)
	return text
	
def main():
	text = get_text()
	
			
main()

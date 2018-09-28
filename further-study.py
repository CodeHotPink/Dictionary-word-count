# put your code here.
from collections import Counter
my_file = open("test.txt","r")
word_frequency = Counter()

# my_lines = my_file.rstrip("\n").readlines()
for line in my_file:
	" ".join(line for line in my_file if line.isalnum())
	print(line)
		
	"""line_list = line.strip("\n").split(" ")
	for word in line_list:
		word_frequency[word] = word_frequency.get(word, 0) + 1

for key_word, count in word_frequency.items():
	print("{} {}".format(key_word,count))"""
	
	

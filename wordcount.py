# put your code here.
my_file = open("test.txt","r")
word_frequency = {}

# my_lines = my_file.rstrip("\n").readlines()
for line in my_file:
	line_list = line.strip("\n").split(" ")
	for word in line_list:
		if word in word_frequency:
			word_frequency[word] +=1
		else:
			word_frequency[word] = 1
			
for key_word, count in word_frequency.items():
	print("{} {}".format(key_word,count))
	
	

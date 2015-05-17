import re
from functools import reduce

BIGGEST_WORD = ""

def findLongestWord(book):
	with open(book, "r") as ins:
		max_word_length = 0
		max_word = ""
		book = []
		result = {}
		for line in ins:
			word_array = re.split(' |-|\.|\?|\!|"|:|;|,|\)|\(', line.rstrip())
			book.append(word_array)
			
			if word_array:
				new_word = max(word_array, key=len)
				new_max_length = len(new_word)
			else:
				continue

			if(new_max_length > max_word_length):
				max_word = new_word
				max_word_length = new_max_length
		
		result['longest_word'] = max_word
		result['book_list'] = book
		
		print "Longest word: " + max_word
		return result

def appendLongestWord():
	global BIGGEST_WORD
	long_word_dict = findLongestWord("book.txt")
	BIGGEST_WORD = long_word_dict['longest_word']
	book_list = long_word_dict['book_list']

	# book_list is a list of paragraphs (list of lists)
	# first I take each of the paragraphs (inner lists) and map it to a function that appends 
	# the longest word to each entry of the list. Then these new lists of appended words is reduced
	# into one giant list.
	appended_words_list = reduce(reduceParagraphsList, map(lambda li: map(append, li), book_list))
	return appended_words_list

# Having the list of words with the longest word appended,
# take that set and create a dictionary of sorted words as keys,
# and a list containing and word (which it's sort is a key in the dictionary)
# The resulting list elements in the dictionary that have more than one entry are anagrams 
def findAnagrams(longest_word_set):
	word_set = set(longest_word_set)
	sorted_dict = {}
	anagram_list = []
	for word in word_set:
		sort_word = ''.join(sorted(word))
		if(sort_word not in sorted_dict):
			sorted_dict[sort_word] = [word]
		else:
			sorted_dict[sort_word].append(word)
	
	for k,v in sorted_dict.iteritems():
		if (len(v) > 1):
			anagram_list.append(v)
	
	resulting_anagram_list = reduce(reduceParagraphsList, anagram_list)
	return resulting_anagram_list

def append(st1):
	return st1 + BIGGEST_WORD[len(st1):]	

def reduceParagraphsList(l_first,l_second):
	return l_first+l_second

def writeToFile(file_name, list_of_words):
	with open(file_name,"w") as write_file:
		for word in list_of_words:
  			print>>write_file, word

def writeAppendedWords(word_set):
	writeToFile("appendedWords.txt", word_set)

def writeAnagramsList(anagram_set):
	writeToFile("anagramWords.txt", anagram_set)

word_set = appendLongestWord()
writeAppendedWords(word_set)
writeAnagramsList(findAnagrams(word_set))


# I downloaded the book as a .txt file, then I cleaned it up (removed certain encoding problems) using
# Sublime Text regex find and replace.
# The longest word in the brothers karamazov is: characteristically, 18 chars in length
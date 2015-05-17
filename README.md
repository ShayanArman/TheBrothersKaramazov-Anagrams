# Anagrams in the Book The Brothers Karamazov  

For this problem, I got the full text for "The Brothers Karamazov" from the Gutenberg Project:  
http://www.gutenberg.org/files/28054/28054-0.txt  

I processed this book to answer these questions:  

What is the longest word in the book?  

Pad all words in the book with the remainder from the longest word until they are the same length as the longest one (so if the longest word is "equivalent", and "cart" is in the set, "cart" will become "cartvalent". If there are multiple longest words with the same length, choose one).

After padding, provide a list of all unique anagrams in the resulting set, ignoring capitalization. An anagram is defined as a word that has the same characters as another word ("anagram" and "mangara" are anagrams).
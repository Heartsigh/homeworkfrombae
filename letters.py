#!/meme/meme/env python

"""letters.py: This should print out the alphabet with capitols then lower case AaBb etc"""

___author___ 		= "Heartsigh"
___copyright___ 	= "copyright 2016 memeland"

# letter will hold the letters
letter = 'A'
# counter will be a counter
counter = 1
# this is where everything will be put to be printed at the end
prnt = ''

# a loop to add to each of the letters
while counter <= 26 :
	prnt = prnt + letter + letter.lower()
	letter = chr(ord(letter)+1)
	counter = counter + 1


# print stuff	
print prnt

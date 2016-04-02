#!/meme/meme/env python

"""euler1.py: This program should find and add up all the numbers between 1 and 1000 that are divisable by 3 and add them up."""

___author___ 		= "Heartsigh"
___copyright___ 	= "copyright 2016 memeland"

# variable to keep track of adding all the numbers
add = 0
# this is a counter variable for the loop and to count up to 1000 for this project
count = 2

#loop to count to 1000 (to include 1000 add = after <)
while count < 1000 :
	# if the number is a divisable of 5 or 3 run the code to add it to the add variable
	if count % 3 == 0 or count % 5 == 0 :
		add = add + count
	# add on to counter
	count = count + 1

# print the total of all the divisables
print add
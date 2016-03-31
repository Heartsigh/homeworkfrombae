meme = 'A'
memex = 1
memey = 'Aa'
while memex <= 25 :
	meme = chr(ord(meme)+1)
	memex = memex + 1
	memey = memey + meme + meme.lower()
print memey

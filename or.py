from random import choice
game = choice(['cricket','vollyball','hockey','football','ludo'])

if game == 'cricket' or game =='hockey':
	print("you like play with small balls")
elif game == 'vollyball' or game =='football':
	print("you are not intrested in small balls ;) ")
else:
	print("you dont like games at all")
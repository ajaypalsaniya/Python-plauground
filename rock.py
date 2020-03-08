#if else statement

print("welecome to Rock\n\nPaper\n\nnd Scissors\n\n enter choice\n")
player1 = input("player1,Enter your choice: ")
player2 = input("player2,Enter your choice: ")

if player1 =="scissors":
	print('(** CHEATING **)\n'* 10)
elif player1 =='rock' and player2 == 'paper':
	print("SHOOT")
	print("player2 wins")
elif player1 =='paper' and player2 == 'scissors':
	print("SHOOT")
	print("player2 wins")
elif player1 =='paper' and player2 == 'rock':
	print("SHOOT")
	print("player1 wins")
elif player1 =='rock' and player2 == 'scissors':
	print("SHOOT")
	print("player1 wins")
elif player1 == player2:
	print("match tie")

else:
	print("WRONG input try again")


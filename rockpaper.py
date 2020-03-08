import random
print("welcome to RPS with computer")
print("player1 enter your choice :")
player1 = input()
rand_num = random.randint(0,2)
if rand_num ==0:
	computer ="rock"
elif rand_num ==1: 
	computer ="paper"
else:
	computer="scissors"
print(computer)

if player1 == computer:
	print("It's a tie!")
elif player1 == "rock":
	if computer == "scissors":
		print("player1 wins!")
	elif computer == "paper":
		print("computer wins!")
elif player1 == "paper":
	if computer == "rock":
		print("player1 wins!")
	elif computer == "scissors":
		print("computer wins!")
elif player1 == "scissors":
	if computer == "paper":
		print("player1 wins!")
	elif computer == "rock":
		print("computer wins!")	
else:
	print("something went wrong")


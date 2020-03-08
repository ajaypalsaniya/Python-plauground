#Simple game for Random number between 1-100 
import random
random_num = random.randint(1,100)

print("Welcome and Guess number between 1-100")
guess = None
count_left=10
count = 0
print(f"you have left {count_left} attempt only play wisely")
while guess!=random_num:
	guess =int(input())
	if guess<random_num:
		print(f"you have {count_left-1} attempt left ")
		print("your guess is too low")
		count_left-=1
		count+=1

	elif guess>random_num:
		print(f"you have {count_left-1} attempt left ")
		print("your guess is too high")
		count_left-=1
		count+=1
	else: 
		print(" congratulations! you win")
		count_left-=1
		count+=1
print(f"you took {count} attempt to win")
print(f'guess number was {random_num}')



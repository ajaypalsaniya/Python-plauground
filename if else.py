#if else statement 

print("enter your age:")
age = int(input())
if not ((age>=2 and age<=8) or age>=65):
	print("you have to pay 10$ for ticket")

elif (age >2 and age<8):
	print("hey! child you have to pay 2$ for movie")
else:
	print("hey! old man you have to pay 5$ for movie")
'''numbers = range(50)
def even_num():
	even = []
	for number in numbers:
		if number%2 == 0:
			even.append(number)
	return even

print(even_num())'''
 

def user_menu(choice = "Hello"):
	if choice == "a":
		return "add"
	elif choice == "q":
		return "quit"
	else:
		return "invalid choice"

print(user_menu("a"))
print(user_menu())

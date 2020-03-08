def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

def greet():
    print("My name is Ajay.")

def rage():
	print("I HATE YOU!")
@be_polite
def rub():
	print("rubbish")

# we are decorating our function 
# with politeness!
greet = be_polite(greet)
greet()

polite_rage = be_polite(rage)
polite_rage()



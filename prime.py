#Return prime number in given range

start = int(input("enter your start no.")) #starting number in range
end   = int(input("enter your end no."))   #range stops here
end   = int(input("enter your end no."))

for val in range(start,end + 1):

	if val>1:

		for num in range(2,val):		
			if (val % num) == 0:
				break
		else:
			print(val)
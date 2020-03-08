class Game:
	def __init__ (self,first,last,role,jursy_no):
		self.first = first
		self.last = last
		self.role = role
		self.jursy_no = jursy_no

	def full_name(self):
		self.full_name = self.first +' '+ self.last
		return self.full_name

	def jursy(self):
		return f"is a {self.role} and wears a jursy {self.jursy_no}"

player1 = Game("ajay","palsaniya","goalkeeper","7")
print(player1.full_name())
print(player1.jursy())
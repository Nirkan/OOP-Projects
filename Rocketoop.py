# Basics of Object Oriented Programming

class Rocket(): 		# Rocket simulates a rocket ship for a game
	def __init__(self):
		self.x = 0	# Each rocket has an (x, y) position
		self.y = 0

	def move_up(self):  
		self.y += 1	# Increment the y-position


my_rocket = Rocket()		# Creating a rocket object
print(my_rocket)

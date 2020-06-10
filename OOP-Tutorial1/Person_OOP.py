# class method

class Person:

	number_of_people = 0

	def __init__(self, name):
		self.name = name
		Person.add_person()

	@classmethod
	def number_of_peoplex(cls):
		return cls.number_of_people

	@classmethod
	def add_person(cls):
		cls.number_of_people += 1




p1 = Person("Bernie")
p2 = Person("Modi")


#print(Person.number_of_peoplex())




# Static methods


class Math:
	
	@staticmethod
	def add5(x):
		return x + 5


	@staticmethod
	def add10(x):
		return x + 10


	@staticmethod
	def pr():
		print("run")


Math.pr()

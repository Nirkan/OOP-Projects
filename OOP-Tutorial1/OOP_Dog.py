
# OOP in Python 


print(type("hello"))   # gives clss type string


def hello():
	print("hello")


print(type(hello))      # gives class type function



string = "hello"

print(string.upper())  # A method acting on object of type string.



# Creating a class

class Dog:

	def __init__(self, name, age):             # __init__ method
		self.name = name
		self.age  = age	                   # Attributes
		print(name)

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def set_age(self, age):
		self.age = age

	def add_one(self, x):
		return x+1
	
	def bark(self):			# Method
		print("bark")



d1 = Dog("Scooby", 20)
d2 = Dog("Tommy", 30)
print(d1.get_name())
d2.set_age(23)
print(d2.get_age())


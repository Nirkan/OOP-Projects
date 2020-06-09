
# OOP in Python 


print(type("hello"))   # gives clss type string


def hello():
	print("hello")


print(type(hello))      # gives class type function



string = "hello"

print(string.upper())  # A method acting on object of type string.



# Creating a class

class Dog:
	
	def bark(self):			# Method
		print("bark")



d = Dog() 
d.bark()                              # New instance of clase dog

print(type(d))

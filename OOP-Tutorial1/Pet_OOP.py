

class Pet:
	
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print("I am {} and I an {} years old".format(self.name, self.age))

	def speak(self):
		print("Do not know what it speaks") 


class Cat(Pet):

	def __init__(self, name, age, color):
		super().__init__(name, age)          # super to call from parent class Pet
		self.color = color

	def speak(self):
		print("Meow")

	def show(self):
		print("I am {} and I an {} years old and I am {}".format(self.name, self.age, self.color))



class Dog(Pet):
	def speak(self):
		print("Bark")







p = Pet("Jimmy", 19)
p.show()
p.speak()

c = Cat("malu", 12, "white" )
c.show()
c.speak()

d = Dog("Tommy", 20) 
d.show()
d.speak()



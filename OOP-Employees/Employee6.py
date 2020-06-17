
class Employee:

	def  __init__(self, first, last):
		self.first = first
		self.last  = last
		#self.email = first + '.' + last + '@email.com'

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first  = first
		self.last   = last


	@fullname.deleter
	def fullname(self):
		print('Delete Name !!!')
		self.first = None
		self.last = None


emp_1 = Employee('Tim', 'cena')

emp_1.first = 'John'


emp_1.fullname = 'Bill clinton'

del  emp_1.fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
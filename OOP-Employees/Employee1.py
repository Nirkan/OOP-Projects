
# Here we are typing each employee credentials manually. 
# This is prone to many erros and it is indeed  time consuming.


'''

class Employee:
	pass




emp_1 = Employee()
emp_2 = Employee()


print(emp_1)
print(emp_2)


emp_1.first = "Bill"
emp_1.last  = "clinton"
emp_1.email = "Bill.clinton@company.com"
emp_1.pay   = 50000


emp_2.first = 'sample'
emp_2.last  = 'employee'
emp_2.email  = 'sample.employee@company.com'
emp_2.pay    = 60000


print(emp_1.email)
print(emp_2.email)  


'''



# Thus we use __init__ method

	
class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last  = last
		self.pay   = pay
		self.email = first + '.' + last + '@company.com'


	def fullname(self):
		return '{} {}'.format(self.first, self.last)



emp_1 = Employee('Bill', 'clinton', 50000)
emp_2 = Employee('sample', 'employee', 60000)


#print(emp_1.email)
#print(emp_2.email)

#print('{} {}'.format(emp_1.first, emp_1.last))

#print(emp_1.fullname())

emp_1.fullname()
print(Employee.fullname(emp_1))
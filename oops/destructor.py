class A:
	def __init__(self):
		self.x = 10
		self.y = 20
		print 'i am a constructor'
	def __del__(self):
		print 'i am a destructor'
obj_name = A()
print obj_name.x
print obj_name.y
del obj_name
#print obj_name
#print obj_name.x       #NameError: name 'obj_name' is not defined
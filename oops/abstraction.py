class MyClass:
	x = 10
	__y = 20
	def add(self,a,b):
		return a+b
	def __Sub(self,a,b):
		return a-b
obj_name = MyClass()
print obj_name.x
#print obj_name.__y 	AttributeError: MyClass instance has no attribute '__y'
print obj_name._MyClass__y
#print dir(obj_name)
#print obj_name._MyClass__Sub
print obj_name._MyClass__Sub(5,4)
print obj_name._MyClass__Sub(10,5)
print obj_name._MyClass__Sub(10,20)
print obj_name.add(5,4)
print obj_name.add(10,20)

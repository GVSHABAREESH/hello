#mol
class A:
	def add(self):
		return a+b
	def add(self,a):
		return a+b
	def add(self,a,b):
		return a+b
obj = A()
#print obj.add() 	#TypeError: add() takes exactly 3 arguments (1 given)
#print obj.add(10)	#TypeError: add() takes exactly 3 arguments (2 given)
print obj.add(10,20)

#mol
class B:
	def add(self,a=1,b=2,c=5):
		return a+b+c
obj1 = B()
print obj1.add()
print obj1.add(5)
print obj1.add(5,6)
print obj1.add(5,6,7)

#mor

class MyClass1():
	def add(self,a,b,c):
		return a+b+c
class MyClass2():
	def add(self,a,b,c):
		return a*b*c
obj3 = MyClass1()
obj2 = MyClass2()
print obj3.add(1,2,3)
print obj2.add(1,2,4)

class MyClass1():
	def add(self,a=5,b=6,c=7):
		return a+b+c
obj3 = MyClass1()
print obj3.add(1,2)
class MyClass2():
	def add(self,a=4,b=5,c=6):
		return a*b*c
obj2 = MyClass2()
print obj2.add(7)
print obj2.add(7,8)
print obj2.add(7,8,9)
print obj3.add()



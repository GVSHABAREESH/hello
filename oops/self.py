class MyClass():
	x = 5
	y = 4
	def add(self):
		#print self
		return self.x + self.y
	def mul(self):
		#print self
		return self.x * self.y
obj = MyClass()
print obj.x
print obj.add()
print obj.mul()

print '=='*20



class MyBox:
	x = 2
	y = 9.5
	z = 'hello'
	#add = 10 + 20
objectname = MyBox()
print objectname
print objectname.x
print objectname.y
print objectname.z

objectname.x='hellllll'
print objectname.x
objectname.a = 'x'
print objectname.a

del objectname.a
#print objectname.a

'''def add(ele, l=[]):
	l.append(ele)
	return l
print add(10)
print add(20)
print add(30)
print add('hi',[40,50,60])'''

class A():
	x = 10
obj = A()
print obj.x
#print obj.y
obj.y = 10
print obj.y
obj.x=20
print obj.x


class B:
	x=1
	y=2
obj1 = B()
print obj1.x
print obj1.y
obj1.y = 10
print obj1.y
obj2 = B()
print obj2.x
print obj2.y
print obj1.y
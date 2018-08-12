class Parent():
	a = 10
	b = 20
	c = 30
class Child(Parent):
	c = 40
	e = 50
	f = 60
obj = Child()
print obj.a
print obj.f
print obj.c
#obj1 = Parent()
#print obj1.f 	#AttributeError: Parent instance has no attribute 'f'


#multiple

class Father():
	x = 'gold'
	y = 'silver'
	z = 'bronze'
	u = 'platinum'
class Mother():
	u = 'dosa'
	v = 'idly'
	w = 'upma'
	x = 'ravva'
class Son(Father,Mother):		#based on the MRO method
	m = 'biryani'
	n = 'noodles'
details = Son()
print details.u
print details.n
print details.x


class Father():
	x = 'gold'
	y = 'silver'
class Mother():
	x = 'dosa'
	v = 'idly'
class Son(Mother,Father):  #based on the MRO method
	m = 'biryani'
	n = 'noodles'
details = Son()
print details.x


#multilevel


class Gf():
	a = 10
	b = 20
	c = 30
class Father(Gf):
	d = 40
	e = 50
	f = 60
class Son(Father):
	g = 70
	h = 80
	i = 90
assests = Son()
print assests.a
print assests.b
print assests.c
print assests.d
print assests.f

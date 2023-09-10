# written by tata dinosaur 
# 08 - Sept - 2023 
# this line prints a text (basics)
text = "Today is a good day"
print(text)
# medium....now we have a function
def Print():
	print(text)
Print()
# switching gears now we have a class
class TextPrinting(object):
	def __init__(self, name):
		self.name = name
obj_print = TextPrinting('mudu')
obj_print.name = 'Mudu'
print(obj_print)
print(obj_print.name)
class main(object):
	def __init__(self, name, age):
		self.name= name
		self.age = age
	def __str__(self):
		pass


class Test:
	def __init__(self,a,b):
		self.a = a
		self.b=b
	def add(self):
		return self.a+self.b
	def __repr__(self):
		return "Testing"
obj = Test(10,20)
print(obj)
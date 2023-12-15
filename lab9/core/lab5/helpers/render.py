import math

class Renderer:
	def __init__(self):
		self.shades = ('.',':','!','*','o','e','&','#','%','@')

	def return_shades(self):
		return self.shades

	def normalize(self, v):
		len = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
		return (v[0]/len, v[1]/len, v[2]/len)

	def dot(self, x,y):
		d = x[0]*y[0] + x[1]*y[1] + x[2]*y[2]
		return -d if d < 0 else 0
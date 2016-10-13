from copy import *


class Mint:
	""" 
	Modulo int
	"""
	
	def __init__(self, value : int, mod : int):
		self.value = value
		self.mod = mod

	def refresh(self):
		self.value = self.value % self.mod

	def fast_exp(self,exp : int):
		"""
		exponentiation of a Mint computing by the fast exponentiation algorithm
		"""
		k = copy(exp)
		pointer = 1
		p = Mint(1,self.mod)
		while (k>0):
			if(pointer & exp):
				p.value = (p.value*self.value) 
				p.refresh()
			self.value = self.value * self.value
			self.refresh()
			k = k // 2
			pointer = pointer << 1
		self.value = p.value
	
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  testing.py
#  
#  Copyright 2020 Ferdinand Kamuzora <ferdinandkamuzora@outlook.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import numpy as np
import pandas as pd
import random
import secrets
import string
import fibonacci

class Randomizer:	
		
	def __init__ (self, type="",num=10,start=0, end=0, randn=0, pattern=3):
		
		#VARIABLES
		self.type = type
		self.num = num
		self.temp = ""
		self.randn = randn
		
		if type == "zeroes":	
			self.generate_zeroes(self.num)
		elif type == "randfloat":
			self.generate_float(self.num)
		elif type == "crypto":
			self.generate_crypto(self.num)
		elif type == "alphanumeric":
			self.generate_alphanumeric(self.num)
		elif type == "binarystring":
			self.generate_binarystring(self.num)
		elif type == "letters":
			self.generate_letters(self.num)
		elif type == "numbers":
			self.generate_numbers(self.num)
		elif type == "randompatterns":
			self.generate_randompatterns(self.num, self.randn)
		elif type == "float":
			self.generate_float(self.num)
		elif type == "fibonacci":
			self.generate_fibonacci(self.num)
		##elif type == "crypto":
		##	generat
			
		self.print_temp()
			
	def print_temp(self): print("type = "+self.type+"\nrandom = "+self.temp+"\n\n")
	
	def generate_zeroes(self, num):
		for i in range(num): self.temp += str(random.randint(0,0))		 
			
	def generate_binarystring(self,num):
		for i in range(num): self.temp += str(random.randint(0,1))
		 	
	def generate_float(self, num):
		for i in range(num):
			self.temp += str(random.uniform(0, 1))
		 
	def generate_letters(self, num):
		for i in range(round(num/50)):
			self.temp = str(''.join(random.sample(string.ascii_letters, 50)))
	
	def generate_numbers(self, num):
		self.temp = str(''.join(random.sample(string.digits, 10)))
	
	def generate_alphanumeric(self, num):
		for i in range (int(round(num/50,0))):
			self.temp  = str(''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, 50)))
		
	def generate_randompatterns(self, num=16, randn=5):
		## c = ''
		
		n = 3
		s = 0
		
		for i in range (num):
			c = random.sample(string.ascii_uppercase+string.ascii_lowercase, 1)	
			for j in range (n):
				
				n = random.randint(1, randn)
				s += 1
				##print(c)
				if s <= num: self.temp+=''.join(c)
				else: break
	
	def generate_fibonacci (self, num):
		for i in range(num):
			self.temp += str(fibonacci.fibo(i))
		
		
	def generate_crypto(self, num):
		self.temp = str(secrets.token_bytes(num))
		 
		
if __name__ == "__main__":
	n=20
	randn=5
	pattern = 3
	
	rand = Randomizer(type="alphanumeric", num=n)
	##rand = Randomizer(type="binary", num=n)
	rand = Randomizer(type="float", num=n)
	rand = Randomizer(type="letters", num=n)
	rand = Randomizer(type="binarystring", num=n)
	rand = Randomizer(type="zeroes", num=n)
	rand = Randomizer(type="crypto", num=n)
	rand = Randomizer(type="numbers", num=n)
	rand = Randomizer(type="randompatterns", num=n, randn=randn, pattern=pattern)
	rand = Randomizer(type="fibonacci", num=n)
	
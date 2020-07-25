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

#import numpy as np
#import pandas as pd
import random
import secrets
import string
import fibonacci

class Randomizer:	
		
	def __init__ (self, type="",num=10,start=0, end=0, randn=5, pattern=3):
		
		#VARIABLES
		self.type = type
		self.num = num
		self.temp = ""
		self.randn = randn
		self.start = start
		self.end = end
		self.pattern = pattern
		self.alg = {
				"A" : "zeroes",
				"B" : "binarystring",
				"C" : "digits",
				"D" : "lowercase",
				"E" : "letters",
				"F" : "randpatterns",
				"G" : "alpanumeric",
				"H" : "fibonacci",
				"I" : "randfloat",
				"J" : "crypto",
			}
		

	def options (self, type="",num=10,start=0, end=0, randn=5, pattern=3):
		#print(num)
		self.type=input("SELECT ALGORITHM\n\nA: zeroes\nB: binarystring\nC: digits\nD: lowercase\nE: letters\nF: randpatterns\nG: letters\nH: alphanumeric\nI: fibonacci\nJ: randfloat\nK: Gausee\nL: crypto\n\n\----> ")
		self.num=int(input("Amount: "))
		
		if self.type == "f" :
			self.randn
		
		self.generate(self.type, self.num)
		
		
	def generate(self, type, num, randn=3, pattern=3):
		
		
		if type == "A" or type == "a": 
			self.type="zeroes"
			self.generate_zeroes(num)
			print("zeroes")
			
		elif type == "B" or type == "b": 
			self.type="binarystring"
			self.generate_binarystring(num)
		
		elif type == "C" or type == "c": 
			self.type="digits"
			self.generate_numbers(num)
			
		elif type == "D" or type == "d": 
			self.type="lowercase"
			self.generate_lowercase(num)
			
		elif type == "E" or type == "e":
			self.type="letters"
			self.generate_letters(num)
			print(type)
			
		elif type == "F" or type == "f":
			self.type="randpatterns"
			self.generate_randompatterns(num, randn, pattern)
			
		elif type == "G" or type == "g": 
			self.type="letters"
			self.generate_letters(num)
			
		elif type == "H" or type == "h": 
			self.type="alphanumeric"
			self.generate_alphanumeric(num)
			
		elif type == "I" or type == "i": 
			self.type="fibonacci"
			self.generate_fibonacci(start, num)
			
		elif type == "J" or type == "j":
			self.type="randfloat"
			self.generate_float(num)
			
		elif type == "K" or type == "k":
			self.type = "gauss"
			
		elif type == "L" or type == "l": 
			self.type="crypto"
			self.generate_crypto(num)
			
		else:
			self.options(type="")
		
		
		##print("END")
		
		

	
	def print_temp(self): print("type = "+self.type+"\nrandom = "+self.temp+"\n\n")
	
	def get_result (self): return self.temp
	
	
	# GENERATE RANDOMS
	
	def generate_zeroes(self, num):  #generates a stream of zeroes
		for i in range(num): self.temp += str(random.randint(0,0))
		
		return self.temp
		
	def generate_binarystring(self,num):  #generates a stream of 1 and 0 (unicode strings) randomly
		for i in range(num): self.temp += str(random.randint(0,1)) 
		return self.temp
	
	def generate_float(self, num, start=0, end=1):
		for i in range(num):
			self.temp += str(random.uniform(start, end))
		
		return self.temp
		 
	def generate_letters(self, num):
		
		for i in range(num):
			self.temp += str(''.join(random.sample(string.ascii_letters, 1)))
		return self.temp
	
	def generate_numbers(self, num):
		for i in range (num):
			self.temp += str(''.join(random.sample(string.digits, 1)))
		return self.temp
	
	def generate_lowercase(self, num):
		for i in range (num):
			self.temp  += str(''.join(random.sample(string.ascii_lowercase, 1)))
		return self.temp
	
	def generate_alphanumeric(self, num):
		for i in range (num):
			self.temp  += str(''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, 1)))
		return self.temp
		
	def generate_randompatterns(self, num=16, randn=5, pattern=3):
		## c = ''
		
		n = pattern
		s = 0
		
		for i in range (num):
			c = random.sample(string.ascii_uppercase+string.ascii_lowercase, 1)	
			
			for j in range (n):
				
				n = random.randint(1, randn)
				s += 1
				##print(c)
				if s <= num:
					self.temp+=''.join(c)
				else: break
			
		return self.temp
	def generate_fibonacci (self, start=0, num=16):
		for i in range(start, start+num):
			self.temp += str(fibonacci.fibo(i))
		return self.temp
		
	def generate_crypto(self, num):
		self.temp = str(secrets.token_bytes(num))
		return self.temp
	 
	def generate_gauss(self, start=0, end=1, num=1):
		v=""
		v+=v
		 #for i in range(num):
		 #	  self.temp=str(''.join(random.gauss(self.start, self.end)))
		 #return self.temp
	  
	  
"""
if __name__ == "__main__":
	n=20
	randn=5
	pattern = 3
	
	rand = randomizer(type="alphanumeric", num=n)
	##rand = Randomizer(type="binary", num=n)
	rand = randomizer(type="float", num=n)
	rand = randomizer(type="letters", num=n)
	rand = randomizer(type="binarystring", num=n)
	rand = randomizer(type="zeroes", num=n)
	rand = randomizer(type="crypto", num=n)
	rand = randomizer(type="numbers", num=n)
	rand = randomizer(type="randompatterns", num=n, randn=randn, pattern=pattern)
	rand = randomizer(type="fibonacci", num=n)
"""
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

import os

class makefile:
	
	def __init__ (self, fname, dir=".\\", datastream="TESTING", end=False, new=False):
		
		self.fname = fname
		self.data = datastream
		self.end = end
		self.dir = ".\\Data\\" + dir
		self.tosave += self.dir + self.fname + ".data"
		self.f = ""
		
		
		
	def make_file(self, new):

		if new:
			self.f = open(self.tosave, "w")
		else:
			self.f = open(self.tosave, "a")
	
	def save_data(self, datastream, fname="test", sub=".//", new=True):
		
		self.fname = fname + ".data"
		self.tosave = self.dir + self.fname
		
		self.make_file(new)
		
		if not new:
			self.f.write(datastream, "a")
					
		else:
			self.f.write(datastream, "w")
			
		self.f.close()
		
		

## class getfile:
	
		
		
		
		
		
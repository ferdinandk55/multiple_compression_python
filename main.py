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

from classes.random_generator import Randomizer
#import file_generator as fileg



if __name__ == "__main__":
	
	print(os.sep)
	s=os.sep
	f=open("."+s+"Data"+s+"test.data","w")
	f.write("========TESTING=======")
	f.close()
	
	#rnd = Randomizer()
	
	#rnd.options()
	
	#rnd.print_temp()
	
	##print(data.temp)
	
	##fileg.makefile()
	
#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

"""
    author : Developed by Marc-Alexandre Blanchard
    date : 01 2016
    Progress bar

    installing [####################] 100%
"""

class ProgressBar(object):
	""" Define a progress bar for console use """

	__BARLENGTH = 28
	__NUMBEROFSUBDIVISION = 20

	__progressChar = ''
	__taskName = ''
	__value = 0

	def __init__(self,taskName,initValue,progressChar='#'):
		""" 
			taskName [progressChar*20] percentage% 
			installing [####################] 100%
		""" 
		if(len(progressChar)!=1):
			progressChar='#'
		self.__progressChar=progressChar
		self.__taskName=taskName
		self.__value=initValue
		self.__printBar()

	def __printBar(self):
		""" Display bar according to its actual value """
		divisionFilled = int(self.__value/5)
		divisionToFill = self.__NUMBEROFSUBDIVISION-divisionFilled
		bar = str(divisionFilled*self.__progressChar)+str(divisionToFill*' ')
		fullBar = '{0} [{1}] {2:3d}%'.format(self.__taskName,bar,self.__value)
		print(fullBar,end='' if self.__value<100 else '\n')
		
	def setValue(self,val):
		""" setValue to the ProgressBar and update display """
		if(isinstance(val,int) and val >= 0 and val <= 100):
			self.__value = val
			self.__clearBar()
			self.__printBar()

	def __clearBar(self):
		""" clear bar to redraw it after"""
		print ('\r'*(self.__BARLENGTH+len(self.__taskName)),end='')

def test():
	import time
	import sys
	a = ProgressBar('testing',0)
	for val in range(101):
		a.setValue(val)	
		time.sleep(0.001) 

def test2():
	import time
	import sys
	a = ProgressBar('installing',10,progressChar='=')
	for val in range(101):
		a.setValue(val)	
		time.sleep(0.001) 

def test3():
	import time
	import sys
	a = ProgressBar('installing',10,progressChar='ok')
	for val in range(121):
		a.setValue(val)	
		time.sleep(0.001)  

if __name__ == '__main__':
	test()
	test2()
	test3()

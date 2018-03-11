from signal_generator import  *
from today.py import * 
from encoding_top import *
import time 
import pigpio


def sender(st):
	retries = 3
	L = twostrings(st)
	generate(L[0])
	response = top(1)
	if response :
		print("Message Sent ")
	else: 	
		if(retries == 0):
			print("Failed")
		else:	
			while(retries!=0):
				generate(L[1])
				res2 = top(1)
				if res2 : 
					print("Message Sent")
					break
				else : 
					retries -= 1
	
	if(retries==0): 
		print("Message Unsuccessful")		



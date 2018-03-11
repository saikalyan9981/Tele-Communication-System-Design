import time 
import pigpio
from today import *
from signal_generator import * 
from decoding import *

pi = pigpio.pi()

def receive(k):
	if(k==0):
		print("Sender is sleeping? ")
	result=top(0)

	if not (result=="Timeout"):
		m = str(hamming_decoder(result))
		if not (m=="-1"):
			print(m)
			generate("111")
		else:
			receive(k-1)
	else:
		receive(k-1)
receiver(3)

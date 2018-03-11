import time
import pigpio


GPIO = 12

pi = pigpio.pi()

ack_wait = 2

tp = 0.1

mes = ""
def message():
	global mes
	def reading():
	  global mes
	  le = ""
	  i_le = 0
	  count = 0
	  while True:
	    	    	
	    message=str(pi.read(GPIO))
#	    print(message)
	    if(len(le)<6):
		le+=message
#		print("le "+le)
            else:
#               print(message)
                mes+=message
                count+=1

	    if(i_le==0 and  (len(le)==6)):
		i_le = int(le[1:],2)
#		print(le)
#		print(i_le)
	    if((count==i_le) and (len(le)==6)):
#		print(count)
#		print("l "+le)
#		print("mes "+mes)
		return mes

	    time.sleep(tp)

	pi.set_mode(GPIO,pigpio.INPUT)
	
	if pi.wait_for_edge(GPIO, pigpio.FALLING_EDGE,ack_wait+2 ):
	  time.sleep(tp/2)
	  return reading()
	else: 
		return "TimeOut"

def top( i ): 
	if(i==1):
		if pi.wait_for_edge(GPIO, pigpio.RISING_EDGE,ack_wait):
			return True
		else: 
			return False
 	else: 
		return message()

print(top(0))

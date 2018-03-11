import array
import math

def en_parity_bits_number(n):
	x=2
	while (1) :
		if(n+x < 2**x):
			return x
		x+=1

def extra_parity(m):
	sum = 0;
	for b in m:
		sum = sum + int(b)
	return str(sum % 2)

	
def hamming_encoding ( st ):
	length_data = len(st)
	length_parity = en_parity_bits_number(length_data) #int(math.log(length_data,2))
	parities = [0]*length_parity
	length_codeword = length_parity + length_data
	add_extra = 3
	for x in xrange(length_data):
		
		if(((add_extra+x) == (2 ** (add_extra-1))) ):
			add_extra+=1
		binary_position = ("{0:b}".format(x+add_extra))[::-1]
		
	#	print('x '+str(x) + ' add_extra '+ str(add_extra)+ ' value ' + st[x])
		i = 0

		for b in binary_position:
			if(int(b)==1 and st[x]=='1'):
	#			if(i==0):
	#				print(x+add_extra);
				parities[i]+=1
			i+=1

	#print('codeword ' + str(length_codeword))
	#print(parities)

	message = ''
	par_i = 0
	for e in xrange(1,length_codeword+1):
		if((e == (2 ** par_i))):
			message = str(parities[par_i]%2) + message
			par_i+=1
		else :
			message = st[e-par_i-1] + message
	message = extra_parity(message) + message
	#print(message)
	
	return message

#hamming_encoding('10110010101010101010')
#print(parity_bits_number(4))





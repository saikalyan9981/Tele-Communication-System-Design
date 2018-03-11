import array
import math

def dc_parity_bits_number(n):
	x = 0;
	while (1):
		if(n < (2**x)):
			return x
		x+=1

def dc_extra_parity(m):
	sum = 0;
	for b in m:
		sum = sum + int(b)
	return str(sum % 2)

def message(m):
	message = ''
	i_parity = 0

	for x in xrange(1,len(m)+1):
		if(x == (2** i_parity)):
			i_parity+=1
		else :
			message = m[x-1] + message
	return message[::-1]

		

def hamming_decoder( st ):
	extra_parity = st[0]
	st = (st[1:]) [::-1]
	length_codeword = len(st)
	length_parity = dc_parity_bits_number(length_codeword)
	length_data = length_codeword - length_parity
	g_parities = [0]*length_parity

	i_parity = 0
	for x in xrange(1,length_codeword+1):
		if(x == (2** i_parity)):
			#print('x '+str(x) + ' i_parity '+ str(i_parity)+ ' value ' + st[x-1])
		
			g_parities[i_parity] = g_parities[i_parity] + int(st[x-1])
			i_parity+=1
		else :
			binary_position = ("{0:b}".format(x))[::-1]
			i = 0
			for b in binary_position:
				if(int(b)==1 and st[x-1] == '1'):
#					if(i==0):
#					 	print('x '+str(x) + ' value ' + st[x-1])
					g_parities[i]+=1
				i+=1

	error_pos = ''
	for i in xrange(len(g_parities)):
		error_pos =  str(g_parities[i] % 2) + error_pos
	#print(error_pos)
	error_pos = int(error_pos,2)
	#print(error_pos)

	n_extra_parity = dc_extra_parity(st)

	if(n_extra_parity == extra_parity): 
		if(error_pos == 0) :
			#print('No error')
			return message(st)
		else:
			#print('2 bit error')
			return '-1'
	else:
		if(error_pos == 0):
			#print('No error')
			return message(st)
		else: 
			#error_pos=len(st)-error_pos 
			#print(error_pos) 
			#print("Before: "+message(st))
			return message((st[:error_pos-1]+str( (int(st[error_pos-1])+1)%2 ) + st[error_pos:]))
	

# m = '10101110101001110110'
# print(len(m))
# for x in range(19):
# 	error_bit = len(m) - x
# 	m1 = m[:error_bit-1]+str( (int(m[error_bit-1])+1)%2 ) + m[error_bit:]
# 	hamming_decoder(m1)
# #print(dc_parity_bits_number(7))

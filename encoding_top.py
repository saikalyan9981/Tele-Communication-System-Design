
from encoding import hamming_encoding


def alength(string):
	n =len(string)
	s="{0:b}".format(n)
	return "10"+s+string

def twostrings(inpstr):
	def replace(L1,L2):
	  i=0
	  j=0
	  for x in range(1,len(L1)):
	   # print(i)
	    #print(j)
	    if(x&(x-1)==0):
	      i+=1
	    else:
	      L1[i]=L2[j]
	      i+=1
	      j+=1
	  return L1


	output=[]

	corinplist = []
	wrninplist = []
	for x in range(1,len(inpstr)+1):
	  if(inpstr[x-1]=='e'):
	    m = len(corinplist)
	    corinplist[m-1]=str(int(not(int(corinplist[m-1]))))
	  else:
	    corinplist.append(inpstr[x-1])
	    wrninplist.append(inpstr[x-1])
	  
	print(str(corinplist))
	print(str(wrninplist))

	corinpstr ="".join(corinplist)

	wrninpstr ="".join(wrninplist)

	print(corinpstr)
	
	
	#print(wrninpstr)

	#print(hamming_encoding(corinpstr))
	output.append(hamming_encoding(corinpstr))	
	enc_list = list(output[0])
	print(enc_list)
	rev_enc_list = replace(enc_list[::-1],wrninplist)
	cor_enc_list = enc_list

	enc_list = rev_enc_list[::-1]
	output.insert(0,"".join(enc_list))
	output[0] = alength(output[0])
	output[1] = alength(output[1])
	return output

#twostrings("00000000000000000000")
#twostrings("10101")
	



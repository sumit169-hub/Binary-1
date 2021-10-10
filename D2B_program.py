print('This is a converter for Decimal number to Binary Number')
print('Press Enter for next example, otherwise enter "0"')
	
	

while True:
	 a=int(input('Enter a number:'))
	 def decimalToBinary(n): 
	 	return bin(n).replace("0b", "") 
	 if __name__ == '__main__':
	 	print(decimalToBinary(a))
	 if a==0:
	 	break
print('Thanks for using !!!!!')	
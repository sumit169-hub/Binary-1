print('This is a converter for Decimal number to Binary Number from 1 to 15')
print('Press "Enter" for another number, other wise, "q" for exit.')

u=[0,1,4,5,8,9,12,13]	
while True:
	N=int(input('Enter a number: \n'))		
	if N<=15:
		if N<8:
			p=0
		else:
			p=1
			
		if N<12:	
			
			if 7<N or N<4 :
				q=0
			else:
				q=1
		else:
			q=1
			
		if N in u:
			r=0
		elif N not in u:
			r=1
			
		if N%2==0:
			s=0
		else:
			s=1
		
		print('Binary output:\n',p,q,r,s)
	else:
		print('Working on Numbers greater than  15')
	action=input()
	if action=='q':
		break
		
	else:
		continue
print('Thanks for using !!!!!')			    
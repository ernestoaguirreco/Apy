h = float(raw_input("Enter Hours:"))
r= float(raw_input('Enter Rate: ' ))

def computepay(h,r):
    if h > 40: 
		pay=(40 + ((h-40) * 1.5)) * r
		return(pay)
    else:	
		pay=40 * 10.50
		return(pay)

print computepay(h,r)





		
		

	
	
	

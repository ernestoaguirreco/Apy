# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
y=0
z=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
        
    posblanco=line.find(" ")
   	
        
    x=float(line[posblanco+1:26])
    z=z+x
    y=y+1
    resultado=z/y
    # print posblanco,line,x,y,z,resultado
    
print 'Average spam confidence:',resultado
		





		
		

	
	
	

# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
	print 'No se pudo abrir el fichero:', fname
for lqs in fh:
	lqs=lqs.rstrip()
	print lqs.upper()
		
		





		
		

	
	
	

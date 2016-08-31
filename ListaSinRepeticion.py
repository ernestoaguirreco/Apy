fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()                       
for line in fh:                    
    palabra= line.rstrip().split()    
    for elemento in palabra:               
        if elemento in lst:         
            continue               
        else :                     
            lst.append(elemento)    
lst.sort()                         
print lst    
		
# en msdos se pone el nombre del archivo con toda su ruta
# en el simulador del curso solo ponemos el nombre del archivo
# en ambos casos el archivo lleva la extension py




		
		

	
	
	

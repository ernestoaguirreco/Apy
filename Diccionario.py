counts=dict()
print 'DIGITE UNA LINEA DE TEXTO:'
linea=raw_input('')
palabras=linea.split()
print 'Palbras',palabras
	
print 'Cuenta...'
for palabra in palabras:
	counts[palabra]=counts.get(palabra,0) + 1
	
print 'Cuenta',counts
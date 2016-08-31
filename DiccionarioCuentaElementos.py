counts=dict()
print 'DIGITE UNA LINEA DE TEXTO:'
linea=raw_input('')
palabras=linea.split()
print 'Palabras',palabras
	
print 'Cuenta...'
for palabra in palabras:
	counts[palabra]=counts.get(palabra,0) + 1
	
print 'Cuenta',counts

for key in counts:
	print key,counts[key]
	if key in counts:
		counts[key] = counts[key] + 1
		print key,counts[key],'Suma'
	else:
		counts[key] = 1
		print key,counts[key],'Uno'
		

	
print list(counts)
print counts.keys()
print counts.values()
print counts.items()

for aaa,bbb in counts.items():
	print aaa,bbb

	

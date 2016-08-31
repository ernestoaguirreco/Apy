
name = raw_input("Enter file:")
if len(name) < 1 : name = "c:\Apy\mbox-short.txt"
name = "c:\Apy\mbox-short.txt"
handle = open(name)
texto = handle.read()


palabras = list()

for linea in handle:
		if not linea.startswith("From:") : continue
		linea = linea.split()
		palabras.append(linea[1])
		print linea


cuenta = dict()

for palabra in palabras:
           cuenta[palabra] = cuenta.get(palabra, 0) + 1 

print cuenta       
maxvalor = None
maxllave = None
for llave,valor in cuenta.items() :	
	print llave,valor
	if valor > maxvalor:
			maxvalor = valor
			maxllave = llave
			print llave,valor
			

print maxllave, maxvalor
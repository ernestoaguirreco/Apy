ent = raw_input('Introduzca la Temperatura Fahrenheit:')
try:
	fahr = float(ent)
	cel = (fahr - 32.0) * 5.0 / 9.0
	print cel
except:
		x='PF introduzca un numero'
		print 'PF introduzca un numero'
	
	
	


def lee_ips(file):
	ips = []
	iguales=0
	for line in file:
		array= line.strip().split(';')
		if array[0] in ips:
			iguales=iguales+1
		else:
			ips.insert(0,array[0])
	print " Existen "+str(len(ips))+" Ips distintas"
	print " ____________________________________________\n"
	file.close()

def lee_ciudades(file):	
	ciudad = []
	ciudadcont=0
	for line in file:
		array= line.strip().split(';')
		print array 
		if array[3] in ciudad:
			ciudadcont=ciudadcont+1
		else:
			ciudad.insert(3,array[3])
	print " Existen "+str(len(ciudad))+" ciudades distintas"

	print " ____________________________________________\n"
	file.close()


		       
repetir = "y" 	
while repetir == "y":   
	print " "
	print " *************************************** "
	print " **           EJERCICIO  LOG          ** "
	print " *************************************** "
	print " "
	file = open('log.txt','r') 
	print " ____________________________________________\n"

	
	lee_ciudades(file)

	repetir = raw_input(" Desea repetir? (y/n): ")
	import os
	if repetir=="y":
		os.system('clear')
	else:
		print "\n Ejercicio creado por Alberto Buongiovanni. Adios \n _________________________________________________"
	



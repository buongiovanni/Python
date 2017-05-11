import random


def comprueba(sorteo,numeros):
	cont=0
	for bola in numeros:
		if (bola == sorteo[0] or bola == sorteo[1] or bola == sorteo[2] or bola == sorteo[3] or bola == sorteo[4] ):
			cont=cont+1
			print " Acertaste la bola numero "+str(bola)   
	
	if cont==5:
		print " \n Enhorabuena. Combinacion ganadora.\n"
	else:
		if cont==0:
			print " Hoy no es tu dia, no acertaste ninguna.\n"
		else:
			print " \n Combinacion NO ganadora.\n Solo acerto "+str(cont)+" bola/s \n"    		
		       
repetir = "y" 	
while repetir == "y":   
	print " "
	print " *************************************** "
	print " **        EJERCICIO  LA LOTERIA      ** "
	print " *************************************** "
	print " "
	a = random.randrange(50)        
	b = random.randrange(50)
	c = random.randrange(50)
	d = random.randrange(50)
	e = random.randrange(50)
	
	sorteo =[a,b,c,d,e]
	numero1 = int(input(" Introduzca numero1: "))
	numero2 = int(input(" Introduzca numero2: "))
	numero3 = int(input(" Introduzca numero3: "))
	numero4 = int(input(" Introduzca numero4: "))
	numero5 = int(input(" Introduzca numero5: "))
	numeros=[numero1,numero2,numero3,numero4,numero5]
	print "\n Tus numeros: "
	print numeros
	print "\n Sorteo: "
	print sorteo
	print " ____________________________________________\n"

	comprueba(sorteo,numeros)
	repetir = raw_input(" Desea repetir? (y/n): ")
	import os
	if repetir=="y":
		os.system('clear')
	else:
		print "\n Ejercicio creado por Alberto Buongiovanni. Adios \n _________________________________________________"
	



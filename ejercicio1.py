def calcula_cuadrado(numero1,numero2):
	if (numero1 > 0 and numero2 >0):
		if numero1>numero2:
			print " ERROR: El primer numero introducido es mayor al segundo.  \n"
	        else:
			cont=0
			while numero1<=numero2:
				cont=cont+numero1	
				numero1=numero1+1
			cont=cont*cont
			print " El resultado es el siguiente: "+str(cont)+"\n"
		        
	else:
		print " No ha introducido dos numeros positivos.\n"
	       		
		       
repetir = "y" 	
while repetir == "y":   
	print " "
	print " *************************************** "
	print " **   EJERCICIO CUADRADO DE SUMAS     ** "
	print " *************************************** "
	print " "

	numero1 = int(input(" Introduzca numero1: "))
	numero2 = int(input(" Introduzca numero2: "))
	print " ____________________________________________\n"

	calcula_cuadrado(numero1,numero2)
	repetir = raw_input(" Desea repetir? (y/n): ")
	import os
	if repetir=="y":
		os.system('clear')
	else:
		print "\n Ejercicio creado por Alberto Buongiovanni. Adios \n _________________________________________________"
	



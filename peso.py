def calcula_ideal(peso, sexo, altura):
	if sexo == 'h':
		ideal= 0.75*(int(altura)-150)+50
		if peso>ideal:
			print " Resultado: No posee un peso ideal. Peso ideal para hombre: "+str(ideal)+"\n"
	        else:
		        print " Resultado: Posee un peso ideal para hombre.Peso ideal para hombre: "+str(ideal)+"\n"
	else:
		if sexo == 'm':
			ideal= 0.70*(int(altura)-140)+40
			if peso>ideal:
				print " Resultado: No posee un peso ideal. Peso ideal para mujer: "+str(ideal)+"\n"
	       		else:
		        	print " Resultado: Posee un peso ideal para mujer.Peso ideal para mujer: "+str(ideal)+"\n"
		else:
			print " No ha elegido un sexo correcto, es usted muy raro.\n"
	
repetir = "y" 	
while repetir == "y":   
	print " "
	print " **************************** "
	print " **       PESO IDEAL       ** "
	print " **************************** "
	print " "

	peso = int(input(" Introduzca su peso (Kg): "))
	altura = int(input(" Introduzca su altura (cm): "))
	sexo = raw_input(" Introduzca su sexo (h/m): ")
	print " ____________________________________________\n"

	calcula_ideal(peso,sexo,altura)
	repetir = raw_input(" Desea repetir? (y/n): ")
	import os
	if repetir=="y":
		os.system('clear')
	else:
		print "\n Vale saborio. Adios \n _________________________________________________"
	



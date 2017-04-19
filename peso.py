def calcula_ideal(peso, sexo, altura):
	if sexo == 'h':
		ideal= 0.75*(int(altura)-150)+50
		if peso>ideal:
			print " Resultado: No posee un peso ideal. Peso ideal para hombre: "+str(ideal)+"\n"
	        else:
		        print " Resultado: Posee un peso ideal para hombre.Peso ideal para hombre: "+str(ideal)+\n"
	else:
		if sexo == 'm':
			ideal= 0.70*(int(altura)-140)+40
			if peso>ideal:
				print " Resultado: No posee un peso ideal. Peso ideal para mujer: "+str(ideal)+"\n"
	       		else:
		        	print " Resultado: Posee un peso ideal para mujer.Peso ideal para mujer: "+str(ideal)+\n"
	
salir = "n" 	
while salir == "n":
       
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
	salir = raw_input(" Desea salir (y/n): ")
	import os
	os.system('clear')
	



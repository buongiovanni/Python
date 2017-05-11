from datetime import  datetime,date

def ticket(fecha_inicial,fecha_final):
	diferencia = fecha_final-fecha_inicial
        print " Tiempo usado:"
	print diferencia
	dias= diferencia.days
	
	segundos= diferencia.seconds
	minutos=segundos/60
	precio=0
	
	if dias==0:	
		if minutos<31:
			precio=3
		else:
			if minutos < 61:
				precio=6		
			else:
				if minutos<91:
					precio=9
				else:
					if minutos<=120:
						precio=12
					else:
						if (minutos>120 and minutos<360):
							precio=30
						else:
							if(minutos>360 and minutos<=1440):
								precio=80
		print " El precio del ticket es de: "
		print precio
	else:
		if (dias>=1 and segundos>=1):
			print "LLamar grua"
		else:
			precio = 80
			print " El precio del ticket es de: "
			print precio
		

		       
repetir = "y" 	
while repetir == "y":   
	print " "
	print " *************************************** "
	print " **     EJERCICIO  APARCAMIENTO       ** "
	print " *************************************** "
	print " "
	

	fecha1 = raw_input(" Fecha Inicial (dd/mm/yyyy hh:mm): ")
	fecha2 = raw_input(" Fecha Final (dd/mm/yyyy hh:mm): ")
	diaI = int(fecha1[:2])
	mesI = int(fecha1[3:-11])
	yeaI = int(fecha1[6:-6])
	horI = int(fecha1[11:-3])
	minI = int(fecha1[-2:])
	
	diaF = int(fecha2[:2])
	mesF = int(fecha2[3:-11])
	yeaF = int(fecha2[6:-6])
	horF = int(fecha2[11:-3])
	minF = int(fecha2[-2:])
	

	fecha_inicial = datetime(yeaI,mesI,diaI,horI,minI,0)
        fecha_final = datetime(yeaF,mesF,diaF,horF,minF,0)


	
	ticket(fecha_inicial, fecha_final)

	repetir = raw_input(" Desea repetir? (y/n): ")
	import os
	if repetir=="y":
		os.system('clear')
	else:
		print "\n Ejercicio creado por Alberto Buongiovanni. Adios \n _________________________________________________"
	



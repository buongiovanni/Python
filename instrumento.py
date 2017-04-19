class Instrumento:
	def __init__(self,precio):
		self.precio = precio
		print "El instrumento cuesta "+str(self.precio)+" euros"
	def tocar(self):		
		print "Estamos tocando musica"
		
	def romper(self):	
		print "Eso lo pagas tu"
		print "Son "+ str(self.precio) + " euros"

class Trompeta(Instrumento):
	pass
class Guitarra (Instrumento):
	pass

Instrumento(3)

b= Trompeta(4)#Inicializa Trompeta
b.tocar()#Imprime estados tocando musica. Metodo heredado
b.romper()#Impreme eso lo pagas tu. Son 4 euros. Metodo heredado


class Trompeta(Instrumento):
	def __init__(self,precio):
		self.precio = precio
		print "La trompeta cuesta "+str(precio)

	def tocar_trompeta(self):
		print "Estamos tocando la trompeta"

b=Trompeta(50) #La trompeta cuesta 50 euros
b.tocar_trompeta()#Estamos tocando la trompeta
b.romper()

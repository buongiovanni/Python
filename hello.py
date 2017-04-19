#Ejercicio 1

l=['Julian','Marta','Alberto','Susana']

print "Nombre de chicos: "
print l[0]+" y "+l[2]
print "Nombre de chicas: "
print l[1]+" y "+l[3]


#Ejercicio 2

INVENTORY ={
'gold':500,
'pouch': ['flint','twine','gemstone'],
'backpack': ['xylopone','dagger','bedroll','bread loaf']
}



print INVENTORY["backpack"]
m= INVENTORY["backpack"]
m.sort()
print INVENTORY["backpack"]

#Ejercicio 3

print "Ejercicio 3 "

F=['xylopone','dagger','bedroll','bread loaf']
print F
F.append('hola')
F.insert(2,'pepe')
F.remove (F[3])

print F

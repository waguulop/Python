#Recorre los usuarios o un conjunto de palabras usando bucle for.

check = True
usuarios = ["NULL", "Guille", "Luis", "Alberto", "David", "Nice", "Manolo"]

while check == True:
	#En funcion de la cantidad que introduzca el usuario se generan esa cantidad de usuarios.
	nusuarios = input("Introduce el numero de usuarios a generar: ")
	if nusuarios > 0:
		check = False
	
for x in range(nusuarios):
	print usuarios[x]
		

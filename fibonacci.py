res = 0
anterior = 1
anterioranterior = 1
contador = 0

nveces = input("Introduce la cantidad de sucesiones de fibonacci que quieres visualizar: ")

while contador <= nveces:
	res = anterior + anterioranterior
	anterioranterior = anterior
	anterior = res
	print(res)
	contador = contador + 1
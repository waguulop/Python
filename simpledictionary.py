print("Welcome to a simple dictionary")
users = {"Guille" : "Admin", "David" : "Admin", "Jaime" : "Profesor"}
print("Guille, David, Jaime")
nombre = raw_input("Please, type the name to see credentials: ")
print(users.get(nombre))

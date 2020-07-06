#Variables
option = True

#Menú del programa agenda
print("")
print("Esta es mi primer agenda en phyton")
print("1. Agregar contacto")
print("2. Eliminar contacto")
print("3. Mostrar contacto")
print("4. Salir del programa")
print("")

while option==True:   
    print("Selecciona una opcion")
    menu = input()
    if menu == "1":
        print("opcion agregar contacto")
        agregar = input()
    elif menu == "2":
        print("Opcion Eliminar contacto")
    elif menu == "4":
        print("Good bye")
        option=False
    else:
        print("Opcion NO válida")

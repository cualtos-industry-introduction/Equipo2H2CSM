<<<<<<< HEAD
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
=======
from agenda import Agenda
from contacto import Contacto

agenda = Agenda('nueva_agenda')
contactos = agenda.obtenerContactos()


    
    while(salida == "1"):

def mostrar_menu():
    print("Agenda")
    print("Selecciona la acción que desees efectuar")
    print("1. Agregar contactos")
    print("2. Mostar contactos")
    print("3. Consulta de contactos")
    print("4. Actualizar contactos")
    print("3. Eliminar contactos")
    print("9. Salir")

    entrada = input ("Escribe la opcion: ")
    
    if entrada == "Agregar":
        agregarContacto()
        print("Agregar contactos")
    elif entrada == "Mostrar":
        print(lista[])
    elif entrada == "Consulta":
        print(lista[])   
    elif entrada == "Actualizar":
        print(lista[])     
    elif entrada == "Eliminar":
        print(lista[])
    elif entrada ==  "Salir":
        exit()
    else:
        print("Opcoin no valida")
>>>>>>> 999c11f7a3111e19902ebbf48b352af9646a4788

from agenda import Agenda
from contacto import Contacto

agenda = Agenda('nueva_agenda')
contactos = agenda.obtenerContactos()

def mostrar_menu():
    print("Agenda")
    print("Selecciona la acción que desees efectuar")
    print("1. Agregar contactos")
    print("2. Mostar contactos")
    print("3. Consulta de contactos")
    print("4. Actualizar contactos")
    print("3. Eliminar contactos")
    print("9. Salir")

salida = "1"
while(salida == "1"):
    mostrar_menu()
    entrada = input ("Escribe la opcion: ")
    
    if entrada == "Agregar":
        agregarContacto()
        print("Agregar contactos")
    elif entrada == "Mostrar":
        mostrarContactos()exit
    elif entrada == "Consulta":
        print(lista[])   
    elif entrada == "Actualizar":
        print(lista[])     
    elif entrada == "Eliminar":
        print(lista[])
    elif entrada ==  "Salir":
        exit()
    else:
        print("Opcion no valida")
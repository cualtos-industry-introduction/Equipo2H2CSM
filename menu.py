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

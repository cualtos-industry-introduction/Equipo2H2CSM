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
        
    elif entrada == "Mostrar":
         mostrarcontactos()
    elif entrada == "Consulta":
         print("")
    elif entrada == "Actualizar":
         print("")
    elif entrada == "Eliminar":
         print("")
    elif entrada ==  "Salir":
        exit()
    else:
        print("Opcoin no valida")

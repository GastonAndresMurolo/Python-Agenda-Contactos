
def mostrar_menu():
    print("\n ---Agenda de Contactos----")
    print("1.Agregar un contacto")
    print("2.Buscar un contacto")
    print("3.Eliminar un contacto")
    print("4.Lista de contactos")
    print("5.Salir")
    print("\n")
    
def agregar_contacto(agenda): 
       nombre=input("Ingrese el nombre completo del contacto")
       telefono=input("Ingrese el telefono del contacto")
       email=input("Ingrese el email del contacto")
       
       agenda[nombre]={"telefono": telefono,"email":email}
       print(f"El contacto {nombre} ha sido agregado exitosamente")
       
def eliminar_contacto(agenda):
        nombre=input("Ingrese el contacto que desea eliminar")
        if nombre in agenda:
            del agenda[nombre]
            print(f"El contacto {nombre}  ha sido eliminado correctamente")
        else:
            print("El contacto no se encuentra dentro la agenda")    

def buscar_contacto(agenda):
    nombre=input("Ingrese el nombre del contacto a buscar")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Telefono: {agenda[nombre]["telefono"]}") 
        print(f"Email:{agenda[nombre]["email"]}")
    else:
        print("El nombre del contacto no existe")    

def listar_contactos(agenda):
    if agenda:
        print("\n Lista de contactos")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info["telefono"]}")
            print(f"Email: {info["email"]}")      
            print("-" * 20)
    else:
        print("La agenda aun esta vacia")    
        
          

def agenda_contacto():
    agenda={}
    
    while True:
        mostrar_menu()
        print("\n")
        
        opcion=(input("Elija una opcion"))
        
        
        if opcion=="1":
            agregar_contacto(agenda)
        elif opcion=="2":
            buscar_contacto(agenda)
        elif opcion=="3":
           eliminar_contacto(agenda)
        elif opcion=="4":
            listar_contactos(agenda)
        elif opcion=="5":
            print("Saliendo del programa")
            break
        else:
            print("No es una opcion valida.")
            
agenda_contacto()
          
            
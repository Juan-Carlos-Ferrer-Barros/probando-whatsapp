from menu_de_contactos import menu_contactos
from menu_de_grupos import menu_grupos
def menu_chats(usuario, usuarios_listados):
    programa = True
    while programa:
        print("\n")
        print(" Menú de Chats ".center(25,"*"))
        print("\nSelecciona una opción:\n\n[1] Ver contactos\n[2] Ver grupos\n[0] Volver")
        opcion = input("Indique su opción (0, 1 o 2): ")
        if opcion == "1":
            x = menu_contactos(usuario, usuarios_listados)
        elif opcion == "2":
            x = menu_grupos(usuario, usuarios_listados)
        elif opcion == "0":
        	return
        else:
            print("\nOpción inválida")
            continuar = input("\n[Enter] para continuar")




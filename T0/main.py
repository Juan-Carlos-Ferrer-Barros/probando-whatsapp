from menu_de_chats import menu_chats
import os

def menu_inicio():
    programa = True
    while programa:
        print("\n")
        print(" Menú de Inicio ".center(26,"*"))
        print("\nSelecciona una opción:\n\n[1] Crear usuario\n[2] Iniciar sesión\n[3] Mostrar Usuarios\n[0] Salir")
        with open("usuarios.csv","r", encoding = "utf-8") as file:
            archivo = file.readlines()
        with open("usuarios.csv","r", encoding = "utf-8") as file:
            usuarios_listados = file.readlines()
        opcion = input("Indique su opción (0, 1 o 2): ")
        if opcion == "1":
            nombre = input("\nIngrese su nuevo nombre de usuario:\n(este debe tener entre 3 a 15 caracteres, y no puede contener comas ´,´)\n\n")
            a = True
            for i in archivo:
                if nombre not in i:
                    continue
                else:
                    a = False
            if a and 3 <= len(nombre) <= 15 and "," not in nombre:
                archivo.append("\n" + nombre)
                usuarios_listados.append("\n" + nombre)
                archivo = "".join(archivo)
                with open("usuarios.csv","w", encoding = "utf-8") as file:
                    file.write(archivo)
                x = menu_chats(nombre, usuarios_listados)
            elif len(nombre) < 3 or len(nombre) > 15:
                print("El nombre no cumple con los requisitos mencionados")
            else:
                print("Este usuario ya existe")
        elif opcion == "2":
            nombre = input("\nIngrese nombre de usuario:\n\n")
            a = False
            for i in archivo:
                if nombre not in i:
                    continue
                else:
                    a = True
            if a:
                x = menu_chats(nombre, usuarios_listados)
            else:
                print("\nEste usuario no existe")
        elif opcion == "3":
            print("\n", "".join(usuarios_listados))
        elif opcion == "0":
            programa = False
        else:
            print("\nOpción inválida")
            continuar = input("\n[Enter] para continuar")



print(menu_inicio())



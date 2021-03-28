from ver_contactos import ver_contactos
from añadir_contacto import añadir_contacto

def menu_contactos(usuario, usuarios_listados):
    programa = True
    while programa:
        with open("contactos.csv", "r", encoding = "utf-8") as file:
            datos = file.readlines()
        datos_listados = []
        for linea in datos:
            linea = linea.strip("\n")
            linea = linea.split(",")
            datos_listados.append(linea)
        print("\n")
        print(" Menú de Contactos ".center(29,"*"))
        print("\nSelecciona una opción:\n\n[1] Ver contactos\n[2] Añadir contacto\n[0] Volver")
        opcion = input("Indique su opción (0, 1 o 2): ")
        if opcion == "1":
            x = ver_contactos(usuario, usuarios_listados, datos_listados)
        elif opcion == "2":
            x = añadir_contacto(usuario, usuarios_listados, datos_listados)
        elif opcion == "0":
            return
        else:
            print("\nOpción inválida")
            continuar = input("\n[Enter] para continuar")

#print(menu_contactos("lily416"))
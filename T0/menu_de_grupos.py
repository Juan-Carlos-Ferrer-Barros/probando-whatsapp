from ver_grupos import ver_grupos
from crear_grupo import crear_grupo

def menu_grupos(usuario, usuarios_listados):
    programa = True
    while programa:
        with open("grupos.csv", "r", encoding = "utf-8") as file:
            grupos_completos = file.readlines()
        grupos_listados = []
        for linea in grupos_completos:
            linea = linea.split(",")
            linea[1] = linea[1].strip("\n")
            grupos_listados.append(linea)
        print("\n")
        print(" Menú de Grupos ".center(26,"*"))
        print("\nSelecciona una opción:\n\n[1] Ver grupos\n[2] Crear grupo\n[0] Volver")
        opcion = input("Indique su opción (0, 1 o 2): ")
        if opcion == "1":
            x = ver_grupos(usuario)
        elif opcion == "2":
            x = crear_grupo(usuario, usuarios_listados, grupos_completos)
        elif opcion == "0":
            return
        else:
            print("\nOpción inválida")
            continuar = input("\n[Enter] para continuar")
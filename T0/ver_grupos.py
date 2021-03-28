from historial import historial

def ver_grupos(usuario):
    programa = True
    while programa:
        with open("grupos.csv", "r", encoding = "utf-8") as file:
            grupos_completos = file.readlines()
        grupos_listados = []
        for linea in grupos_completos:
            linea = linea.split(",")
            linea[1] = linea[1].strip("\n")
            grupos_listados.append(linea)
        cont = {}
        llave = 1
        for i in grupos_listados:
            if usuario == i[1]:
                cont[llave] = i[0]
                llave += 1
        print("\n")
        print(" Ver Grupos ".center(22,"*"))
        print("\nSelecciona un grupo para \nver tus conversaciones, \no 0 para volver atrás:\n")
        for i in cont:
            print(f"[{i}] {cont[i]}")
        print("[0] Volver\n")
        opcion = int(input("Indique su opción: "))
        if opcion == 0:
            return
        elif opcion in cont:
            x = historial("grupo", usuario, cont[opcion], grupos_completos)
        else:
            print("\nOpción inválida")
            continuar = input("\n[Enter] para continuar")
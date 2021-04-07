from historial import historial

def ver_contactos(usuario, usuarios_listados, datos_listados):
    programa = True
    while programa:
        cont = {}
        llave = 1
        for i in datos_listados:
            if usuario == i[0]:
                cont[llave] = i[1]
                llave += 1
        print("\n")
        print(" Ver Contactos ".center(25,"*"))
        print("\nSelecciona un usuario para \nver tus conversaciones, \no 0 para volver atrás:\n")
        for i in cont:
            print(f"[{i}] {cont[i]}")
        print("[0] Volver\n")
        opcion = int(input("Indique su opción: "))
        if opcion == 0:
            return
        elif opcion in cont:
            x = historial("regular", usuario, cont[opcion], [])
        else:
            print("\nOpción inválida")
            continuar = input("\n[Enter] para continuar")





#print(ver_contactos("lily416"))
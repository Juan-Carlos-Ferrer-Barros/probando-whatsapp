def añadir_contacto(usuario, usuarios_listados, datos_listados):
    programa = True
    d = []
    for i in usuarios_listados:
        i = i.strip("\n")
        d.append(i)
    usuarios_listados = d
    while programa:
        with open("contactos.csv", "r", encoding = "utf-8") as file:
            datos = file.readlines()
        a = True
        print("\n")
        print(" Añadir Contactos ".center(28,"*"))
        nombre = input("\nIngrese nombre de usuario\nel cual desea agregar:\n\n")
        if nombre in usuarios_listados and nombre != usuario:
            amigos = []
            for i in datos_listados:
                if usuario == i[0]:
                    amigos.append(i[1])
            if nombre not in amigos:
                cont1 = f"{usuario},{nombre}"
                cont2 = f"{nombre},{usuario}"
                datos.append("\n" + cont1)
                datos.append("\n" + cont2)
                datos = "".join(datos)
                with open("contactos.csv","w", encoding = "utf-8") as file:
                    file.write(datos)
            else:
                print("\nYa tienes agregado ese contacto")
                continuar = input("\n[Enter] para continuar")
                a = False
        elif nombre == usuario:
            print("\nNo puedes agregarte a ti mismo")
            continuar = input("\n[Enter] para continuar")
        elif a:
            print("\nEl usuario ingresado no existe")
            continuar = input("\n[Enter] para continuar")

        return 






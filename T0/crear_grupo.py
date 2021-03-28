def crear_grupo(usuario, usuarios_listados, grupos_completos):
    programa = True
    d = []
    for i in usuarios_listados:
        i = i.strip("\n")
        d.append(i)
    usuarios_listados = d
    while programa:
        print("\n")
        print(" Crear Grupo ".center(23,"*"))
        nombre = input("\nIngrese nombre del nuevo grupo:\nRequisitos:\n- No debe existir ya en grupos\n- Sin comas (´,´)\n- Mínimo 1 caracter\n\n")
        original = True
        for i in grupos_completos:
            if nombre in i:
                original = False
        if original and len(nombre) >= 1 and "," not in nombre:
            integrantes = input("\nIngrese los integrantes del grupo:\n(Éstos deben ser mínimo 2 y deben\nir separados por ´;´)\n\n")
            integrantes = integrantes.split(";")
            if len(integrantes) >= 2:
                existen = True
                for i in integrantes:
                    if i not in usuarios_listados:
                        existen = False
                if existen:
                    for i in integrantes:
                        agregar = f"{nombre},{i}\n"
                        grupos_completos.append(agregar)
                    grupos_completos = "".join(grupos_completos)
                    with open("grupos.csv","w", encoding = "utf-8") as file:
                        file.write(grupos_completos)
                    return
                else:
                    print("No todos los integrantes existen")
                    continuar = input("\n[Enter] para continuar")
            else:
                print("No se ingresaron suficientes integrantes")
                continuar = input("\n[Enter] para continuar")
        else:
            print("El nombre no cumple con los\nrequisitos mencionados")
            continuar = input("\n[Enter] para continuar")



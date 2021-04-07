import datetime
from parametros import ABANDONAR_FRASE
from parametros import VOLVER_FRASE
import time
import git

def historial(tipo_chat, emisor, receptor, grupos_completos):
    programa = True
    while programa:
        try:
            repo = git.Repo("https://github.com/Juan-Carlos-Ferrer-Barros/probando-whatsapp.git")
            repo.remotes.origin.pull()
        except (git.exc.InvalidGitRepositoryError, git.exc.NoSuchPathError):
            print("Invalid repository: {}".format(local_path)
        with open("mensajes.csv", "r", encoding = "utf-8") as file:
            msj = file.readlines()
        mensajes_listados = []
        for i in msj:
            i = i.split(",", maxsplit=4)
            mensajes_listados.append(i)
        chat_listado = []
        print("\n")
        if tipo_chat == "regular":
            for i in mensajes_listados:
                if i[1] == emisor and i[2] == receptor:
                    chat_listado.append(i)
                if i[2] == emisor and i[1] == receptor:
                    chat_listado.append(i)
            print(f"Historial con {receptor}".center(len(receptor)+26, "*"))
        elif tipo_chat == "grupo":
            for i in mensajes_listados:
                if i[2] == receptor:
                    chat_listado.append(i)
            print(f"Historial de {receptor}".center(len(receptor)+25, "*"))
        for i in chat_listado:
            i[4] = i[4].strip("\n")
            print(f"\n{i[3]}, {i[1]}: {i[4]}")
        print("")
        print("".center(len(receptor)+26, "*"))
        x = input("Enviar mensaje: ")
        if tipo_chat == "grupo":
            if x == ABANDONAR_FRASE:
                for i in grupos_completos:
                    i = i.split(",")
                    i[1] = i[1].strip("\n")
                    if receptor == i[0] and emisor == i[1]:
                        i = ",".join(i) + "\n"
                        grupos_completos.remove(i)
                grupos_completos = "".join(grupos_completos)
                with open("grupos.csv", "w", encoding = "utf-8") as file:
                    file.write(grupos_completos)
                return
        if x == VOLVER_FRASE:
                return
        tiempo = str(datetime.datetime.now())
        tiempo = tiempo.split(" ")
        tiempo[0] = tiempo[0].split("-")
        tiempo[0] = "/".join(tiempo[0])
        tiempo[1] = tiempo[1].split(".")[0]
        tiempo = " ".join(tiempo)
        msj.append(f"\n{tipo_chat},{emisor},{receptor},{tiempo},{x}")
        msj = "".join(msj)
        with open("mensajes.csv", "w", encoding = "utf-8") as file:
            file.write(msj)
        repo.index.add(".")
        repo.index.commit("test wasa")
        repo.remotes.origin.push()
        



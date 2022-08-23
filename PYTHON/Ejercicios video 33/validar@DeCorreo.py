while True:
    correo = input("Digite su correo por favor: ")

    arroba = correo.count("@")

    if arroba == 1:
        if correo.startswith("@"):
            print("Dirección de correo incorrecta.\nIntente de nuevo por favor")

        elif correo.endswith("@"):
            print("Dirección de correo incorrecta.\nIntente de nuevo por favor")
        
        else:
            print("Dirección de correo válida.")
            break
    else:
        print("Dirección de correo incorrecta.\nIntente de nuevo por favor")
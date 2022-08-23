password=input("Escriba la contraseña: ")

x=0
for i in range (len(password)):

    if password[i]==" ":
        x=1
if len(password)<8 or x>0:
    print("Contraseña errónea")
else:
    print("Contraseña OK")
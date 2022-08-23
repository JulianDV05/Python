x=0
y=0
email=input("Introduzca su email: ")

for i in range(len(email)):

    if email[i]=="@":
        x=x+1
    elif email[i]==".":
        y=1

if x>0 and x<2 and y>0:
    print("Dirección de correo válida")
else:
    print("Dirección de correo NO Válida")
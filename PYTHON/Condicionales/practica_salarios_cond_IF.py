salario_pres=int(input("Introduzca salario del presidente: "))
print("salario del presidente: ",salario_pres)

salario_direc=int(input("Introduzca salario del director: "))
print("salario del director: ",salario_direc)

salario_jefea=int(input("Introduzca salario del Jefe de Área: "))
print("salario del Jefe de Área: ",salario_jefea)

salario_admin=int(input("Introduzca salario administrativo: "))
print("salario administrativo: ",salario_admin)

if salario_admin<salario_jefea<salario_direc<salario_pres:
    print("\nSalarios correctos")
else:
    print("\nSalarios no coinciden.")
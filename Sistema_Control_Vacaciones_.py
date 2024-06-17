print("================================================")
print("* Sistema Control DE Vacaciones de los 3 Dptos *")
print("================================================\n")
nombre_empleado = input("Ingrese el nombre del empleado: ")
clave_dpto =int( input("Ingrese la clave del Departamento: "))
antig_empleado =float( input("Ingrese la antiguedad en años del empleado: "))


if clave_dpto == 1:
    print("\nMODULO DEPARTAMENTO 1\n")
    if antig_empleado >=1 and antig_empleado < 2:
        print("El empleado : ",nombre_empleado,"Tiene derecho a 6 dias de Vacaciones")
    elif antig_empleado > 2 and antig_empleado < 6:
        print("El empleado : ",nombre_empleado,"Tiene derecho a 14 dias de Vacaciones")
    elif antig_empleado >= 7:
        print("El empleado : ",nombre_empleado,"Tiene derecho a 20 dias de Vacaciones")
    else:
        print("El empleado : ",nombre_empleado,"No Tiene derecho Vacaciones")
elif clave_dpto == 2:
    print("\nMODULO DEPARTAMENTO 2\n")
    if antig_empleado >=1 and antig_empleado < 2:
        print("El empleado : ",nombre_empleado,"Tiene derecho a 7 dias de Vacaciones")
    elif antig_empleado > 2 and antig_empleado < 6:
        print("El empleado : ",nombre_empleado,"Tiene derecho a 15 dias de Vacaciones")
    elif antig_empleado >= 7:
        print("El empleado : ",nombre_empleado,"Tiene derecho a 25 dias de Vacaciones")
    else:
        print("El empleado : ",nombre_empleado,"No Tiene derecho Vacaciones")
elif clave_dpto == 3:
    print("\nMODULO DEPARTAMENTO 3\n")
    if antig_empleado >=1 and antig_empleado < 2:
        print("El empleado : ",nombre_empleado,"Tiene derecho a 10 dias de Vacaciones")
    elif antig_empleado > 2 and antig_empleado < 6:
        print("El empleado : ",nombre_empleado,"Tiene derecho a 20 dias de Vacaciones")
    elif antig_empleado >= 7:
        print("El empleado : ",nombre_empleado,"Tiene derecho a 30 dias de Vacaciones")
    else:
        print("El empleado : ",nombre_empleado,"No Tiene derecho Vacaciones")
else:
    print('La clave del dpto no existe, vuelva a intentarlo')
print('Fin ')    

  


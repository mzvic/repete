from sys import platform
import sys
import os

def cls():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        return os.system("clear")
    elif platform == "win32":
        return os.system("cls")

cls()
repete = 0.4
if len(sys.argv) > 1:
    repete = float(sys.argv[1])/10
else:
    pass

try:
    print("Hola! Este es un script de Python que te ayuda a calcular la nota que necesitas obtener en el 'Repete' para aprobar un ramo")
    print("Cualquier consulta no dudes en escribirme a vmontesinos2021@udec.cl, suerte en este fin de semestre! \n") 
    n = int(input("Ingresa la cantidad de evaluaciones que has tenido: "))

except ValueError:
    print("ERROR: Ingresa un valor numérico")
    exit()
cls()

notas = []
porcentajes = []
promedio = 0

for i in range(n):
    try:
        notas.append(int(input("Ingresa la nota de la evaluación {} (entre 10 y 70): ".format(i+1))))
        if notas[i] < 10 or notas[i] > 70:
            print("ERROR: Ingresa un valor entre 10 y 70")
            exit()

    except ValueError:
        print("ERROR: Ingresa un número entero (ej: si te sacaste un 3.4, ingresa 34)")
        exit()

print('\n')

for i in range(n):
    try:
        porcentajes.append(int(input("Ingresa el porcentaje de la evaluación {} (sin el símbolo %): ".format(i+1))))
        if sum(porcentajes) > 100:
            print("ERROR: El porcentaje se sobrepasa de 100")
            exit()

    except ValueError:
        print("ERROR: Ingresa un número entero (ej: si te sacaste un 3.4, ingresa 34)")
        exit()

if sum(porcentajes) != 100:
    print("ERROR: El porcentaje debe sumar 100, tus porcentajes suman {}".format(sum(porcentajes)))
    exit()

print('\n')

for i in range(n):
    promedio = promedio + (notas[i] * (porcentajes[i])/100)

ecuacion_para_obtener_40 = (40 - promedio*(1.0-repete))/repete

if promedio > 40:
    print('Ya pasaste el ramo con el promedio {}, felicidades!'.formatstr(int(round(promedio, 0))/10).replace('.', ','))

else:
    print('Tu promedio es {}'.format(str(int(round(promedio, 0))/10).replace('.', ',')))
    print('Considerando que debido al redondeo 3,95 = 4,0 y el repete vale un {}%'.format(str(int(repete*100))))
    print('Necesitarías un {} para aprobar el ramo. Suerte, tú te la puedes!'.format(str(round(ecuacion_para_obtener_40, 1)/10).replace('.', ',')))
    print('\n')


import os
from particula import Particula
from mainclass import MainClass

main = MainClass()

while True:
    print("1. Ingresar datos")
    print("2. Mostrar datos")
    print("0. Salir")
    op = input()
    if op == '1':
        id = int(input("Ingresa el id: "))
        origen_x = int(input("Ingresa el origen en x: "))
        origen_y = int(input("Ingresa el origen en y: "))
        destino_x = int(input("Ingresa el destino en x: "))
        destino_y = int(input("Ingresa el destino en y: "))
        velocidad = int(input("Ingresa la velocidad: "))
        red = int(input("Red: "))
        green = int(input("Green: "))
        blue = int(input("Blue: "))
        p = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        os.system("cls")
        while True:
            print("1. Ingresar al inicio de la lista")
            print("2. Ingresar al final de la lista ")
            a = input()
            if a == '1':
                main.agregar_inicio(p)
                break
            elif a == '2':
                main.agregar_final(p)
                break
            else:
                print("\nLa opcion no es valida")
    elif op == '2':
        main.imprimir()
    elif op == '0':
        break
    else:
        print("\nLa opcion no es valida...\n")
    os.system("pause")
    os.system("cls")
    
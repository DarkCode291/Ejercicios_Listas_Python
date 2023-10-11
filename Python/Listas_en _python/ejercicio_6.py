'''
Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros
cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

'''
lista1 = []
lista2 = []
lista3 = []

def pedir():
    for i in range(5):
        numero = int(input(f"\nIngrese el numero {i+1} para la lista #1: "))
        lista1.append(numero)
        numero2 = int(input(f"Ingrese el numero {i+1} para la lista #2: "))
        lista2.append(numero2)
    lista3 = (sum(lista1) + sum(lista2))    
    print(f"La suma de las dos listas es {lista3}")           

if __name__=="__main__":
    pedir()    
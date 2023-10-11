import random
'''
Ejercicio 5

Hacer un programa que inicialice una lista de números con valores
aleatorios (10 valores), y posterior ordene los elementos de menor a
mayor.

'''

numeros = []

def main():
    for i in range(10):
        num = random.randint(1,100)
        numeros.append(num)
    ordenado =numeros.sort()    
    print("\nnormal")
    for i in numeros:
        print(i,end =" | ")
    print("\nOrdenado Mayor a Menor")
    for i in ordenado:
        print(i,end=" | ")

    
    
if __name__=="__main__":
    main()    
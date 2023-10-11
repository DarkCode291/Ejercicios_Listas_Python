'''
Queremos guardar los nombres y las edades de los alumnos de un curso.
Realiza un programa que introduzca el nombre y la edad de cada alumno.
El proceso de lectura de datos terminará cuando se introduzca como
nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:

• Todos los alumnos mayores de edad.
• Los alumnos mayores (los que tienen más edad)

'''

mostrar =[]

def pedir():
    cont =0
    while(True):
        nombre = input(f"Ingrese el nombre del alumno #{cont + 1}: ")
        if nombre != '*':
            edad = input(f"Ingrese la edad del alumno #{cont + 1}: ")
            mostrar.append([nombre,edad])
            cont +=1
        else:
            break
    validarmayores()
    
    
mayores =[]
def validarmayores():
    for i in mostrar:
        if (int(i[1]) > 18):
            mayores.append(i)
    validarmayoria()
    
mayoria =[]       
def validarmayoria(): 
        
    mayores.sort(reverse=True) 
    if len(mayores) > 0:
        mayoria.append(mayores[0])

    print("Las personas mayores de edad son:")
    for i in mayores:
        nombre, edad = i
        print(f"Nombre: {nombre}, Edad: {edad}")

    print("Las personas con mayor edad son:")
    for i in mayoria:
        nombre, edad = i
        print(f"Nombre: {nombre}, Edad: {edad}")


if __name__=="__main__":
    pedir()        
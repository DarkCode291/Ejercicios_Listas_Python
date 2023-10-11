'''
Ejercicio 5

Crea un programa que pida un número al usuario un número de mes (por
ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del
mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero
tiene 28 días.
'''


dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def pedir():
# Pedir al usuario que ingrese un número de mes
    numero_mes = int(input("Ingresa un número de mes (1-12): "))

# Verificar si el número de mes es válido
    if 1 <= numero_mes <= 12:
    # Obtener el número de días y el nombre del mes
        numero_dias = dias_por_mes[numero_mes]
        nombre_mes = [
        "Error",
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ][numero_mes]

    # Mostrar el resultado
        print(f"{nombre_mes} tiene {numero_dias} días.")
    else:
        print("Número de mes inválido. Debe estar entre 1 y 12.")           
    
        
if __name__=="__main__":
    pedir()
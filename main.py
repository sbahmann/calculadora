import openpyxl
book = openpyxl.load_workbook('C:\\Users\\2499311\\Desktop\\datosphyton.xlsx')
tabelle1 = book.active
celdas = tabelle1['A1':'D4']
lista_empleados = []
factor=3
for fila in celdas:
    empleado = [celda.value for celda in fila]
    lista_empleados.append(empleado)
for empleado in lista_empleados:
    print(f'don {empleado[0]} es el {empleado[1]} y gana {empleado[2]*factor}')

from matplot import pyplot

archivo = open('../Unidad 3/Archivos/ejemplo.csv', 'w')
listaNombres = [
    ['Adan', 26],
    ['Cristobal', 17],
    ['Ana', 5],
    ['Poncho', 30],
    ['Alan', 8],
    ['Jorge', 72],
    ['Aquino', 13],
    ['Badillo', 37],
    ['Segoviano', 40],
    ['Jeremy', 75],
    ['Moises', 50],
    ['Natalia', 12],
    ['Rodrigo', 11],
    ['Bonilla', 99],
    ['Amando', 69],
    ['Raul', 14],
    ['Lexiss', 3],
    ['Sofia', 33],
    ['Angel', 10],
    ['Emmanuel', 51],
    ['Isaac', 70],
    ['Sheko', 85],
    ['Paniagua', 82]
]

print(listaNombres)
for datos in listaNombres:
    for dato in datos:
        archivo.write(str(dato) + ',')
    archivo.write('\n')

archivo.flush()
archivo.close()
def cargarArchivo():
    archivo = open('../Unidad 3/Archivos/ejemplo.csv', 'r')
    contenido = archivo.readlines()

    lines = [i[:-2].split(',') for i in contenido]

    # for line in lines:
        # line[-1] = int(line[-1])

    lines = [[i[0], int(i[1])] for i in lines]

    return lines

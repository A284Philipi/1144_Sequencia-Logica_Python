numero = int(input())
cont = int(1)
while cont <= numero:
    lista = []
    quadrado = int(cont * cont)
    cubo = int(quadrado *cont)
    lista.append(cont)
    lista.append(quadrado)
    lista.append(cubo)
    separador = ' '
    print(separador.join(map(str, lista)))
    lista = []
    quadrado = int((cont * cont) + 1)
    cubo = int((cont * cont * cont) + 1)
    lista.append(cont)
    lista.append(quadrado)
    lista.append(cubo)
    separador = ' '
    print(separador.join(map(str, lista)))
    cont = cont + 1
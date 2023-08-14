def removeStringDaLista(lista):
    i = 0
    while i < len(lista):
        # ver se o tipo é str e remover da lista
        if type(lista[i]) == str:
            lista.pop(i)
        else:
            i += 1

    return lista


lista = [1, 2, 3, '5', '4', 3, 6, '9', '10',  7, 8]
print(lista)
print(removeStringDaLista(lista))

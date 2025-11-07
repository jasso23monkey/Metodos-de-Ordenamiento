def ordenamiento_seleccion(lista):
    # 'i' recorre la lista, y marca el inicio de la porción no ordenada
    for i in range(len(lista)):
        
        # Asumimos que el elemento actual es el más pequeño
        indice_minimo = i
        
        # Buscamos el elemento más pequeño en el resto de la lista (porción no ordenada)
        # 'j' va desde i+1 hasta el final
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                # Si encontramos un valor más pequeño, actualizamos el índice
                indice_minimo = j
        
        # Intercambiamos el elemento más pequeño encontrado con el elemento en la posición 'i'
        # Esto coloca el elemento más pequeño en su posición final correcta
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
        
    return lista

# --- Ejemplo de Uso ---

numeros = [64, 25, 12, 22, 11]

print(f"Lista original: {numeros}")

lista_ordenada = ordenamiento_seleccion(numeros)

print(f"Lista ordenada: {lista_ordenada}")
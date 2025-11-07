def ordenamiento_insercion(lista):
    # Recorremos la lista desde el segundo elemento (índice 1) hasta el final
    for i in range(1, len(lista)):

        # El elemento que queremos 'insertar' en la sublista ordenada
        valor_actual = lista[i]
        
        # 'j' es el índice del elemento inmediatamente anterior al valor_actual
        j = i - 1

        # Movemos los elementos de la sublista ordenada que son mayores 
        # que 'valor_actual' una posición hacia adelante (a la derecha)
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]
            j -= 1

        # Encontramos la posición, e insertamos el valor_actual
        lista[j + 1] = valor_actual
    
    return lista

# --- Ejemplo de Uso ---

numeros = [12, 11, 13, 5, 6]

print(f"Lista original: {numeros}")

lista_ordenada = ordenamiento_insercion(numeros)

print(f"Lista ordenada: {lista_ordenada}")
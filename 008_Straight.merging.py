def straight_merging(lista):
    n = len(lista)
    k = 1  # El tamaño inicial de las secuencias a mezclar (grupos de 1 elemento)
    
    # Repetimos el proceso hasta que el tamaño de la secuencia (k) sea mayor o igual al tamaño de la lista
    while k < n:
        # Usamos una lista temporal para almacenar la mezcla de esta pasada
        lista_temp = []
        i = 0  # Puntero para el inicio de la lista
        
        # Recorremos la lista mezclando secuencias de tamaño 'k'
        while i < n:
            # Definir los límites de la primera secuencia (izquierda)
            inicio_izq = i
            fin_izq = min(i + k, n)
            
            # Definir los límites de la segunda secuencia (derecha)
            inicio_der = fin_izq
            fin_der = min(i + 2 * k, n)
            
            # Obtener las secuencias a mezclar
            izquierda = lista[inicio_izq:fin_izq]
            derecha = lista[inicio_der:fin_der]
            
            # Mezclar las dos secuencias ordenadas
            mezclado = merge_listas_aux(izquierda, derecha)
            
            # Añadir el resultado de la mezcla a la lista temporal
            lista_temp.extend(mezclado)
            
            # Avanzar el puntero para el siguiente par de secuencias
            i += 2 * k
            
        # Reemplazar la lista original con la lista temporal (resultado de esta pasada)
        lista[:] = lista_temp
        
        # Duplicar el tamaño de la secuencia para la próxima pasada
        k *= 2
        
    return lista

def merge_listas_aux(izquierda, derecha):
    """Función auxiliar para mezclar dos listas ordenadas."""
    
    lista_final = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            lista_final.append(izquierda[i])
            i += 1
        else:
            lista_final.append(derecha[j])
            j += 1

    lista_final.extend(izquierda[i:])
    lista_final.extend(derecha[j:])
    
    return lista_final

# --- Ejemplo de Uso ---

numeros = [29, 10, 14, 37, 13, 8]

print(f"Lista original: {numeros}")

lista_ordenada = straight_merging(numeros)

print(f"Lista ordenada: {lista_ordenada}")
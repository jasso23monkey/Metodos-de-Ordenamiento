def merge_sort(lista):
    # Caso base: Si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista

    # 1. DIVIDE
    # Encuentra el punto medio de la lista
    medio = len(lista) // 2
    
    # Divide la lista en dos mitades
    mitad_izquierda = lista[:medio]
    mitad_derecha = lista[medio:]

    # Llama a merge_sort recursivamente en cada mitad
    izquierda_ordenada = merge_sort(mitad_izquierda)
    derecha_ordenada = merge_sort(mitad_derecha)

    # 2. VENCERÁS (Mezcla)
    # Combina las mitades ordenadas usando la función merge_listas
    return merge_listas(izquierda_ordenada, derecha_ordenada)


def merge_listas(izquierda, derecha):
    """Función auxiliar para mezclar dos listas ordenadas en una sola lista ordenada."""
    
    lista_final = []
    i = j = 0  # Punteros para la lista izquierda (i) y derecha (j)

    # Mientras haya elementos en ambas listas, compara y añade el menor
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            lista_final.append(izquierda[i])
            i += 1
        else:
            lista_final.append(derecha[j])
            j += 1

    # Añade los elementos restantes de la lista izquierda (si los hay)
    lista_final.extend(izquierda[i:])
    
    # Añade los elementos restantes de la lista derecha (si los hay)
    lista_final.extend(derecha[j:])
    
    return lista_final

# --- Ejemplo de Uso ---

numeros = [29, 10, 14, 37, 13]

print(f"Lista original: {numeros}")

lista_ordenada = merge_sort(numeros)

print(f"Lista ordenada: {lista_ordenada}")
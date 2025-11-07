def quick_sort(lista):
    # Caso base: una lista con 0 o 1 elemento ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # 1. Seleccionar un pivote (tomamos el primer elemento por simplicidad)
    pivote = lista[0]
    
    # 2. Particionar la lista en tres sub-listas:
    # - Menores que el pivote
    menores = [x for x in lista[1:] if x <= pivote]
    
    # - Mayores que el pivote
    mayores = [x for x in lista[1:] if x > pivote]
    
    # 3. Aplicar Quick Sort recursivamente a las sub-listas
    # y combinarlas: [menores ordenados] + [pivote] + [mayores ordenados]
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

# --- Ejemplo de Uso ---

numeros = [10, 7, 8, 9, 1, 5]

print(f"Lista original: {numeros}")

lista_ordenada = quick_sort(numeros)

print(f"Lista ordenada: {lista_ordenada}")
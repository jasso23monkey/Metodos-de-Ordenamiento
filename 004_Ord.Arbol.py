import heapq

def ordenamiento_heap(lista):
    # 1. Convertir la lista en un Min-Heap
    # Esto reorganiza la lista en el lugar para que cumpla la propiedad de montículo
    heapq.heapify(lista)
    
    # 2. Extraer los elementos uno por uno
    # La lista final contendrá los elementos en orden ascendente
    lista_ordenada = []
    while lista:
        # heapq.heappop() extrae y devuelve el elemento más pequeño de la raíz
        lista_ordenada.append(heapq.heappop(lista))
        
    return lista_ordenada

# --- Ejemplo de Uso ---

numeros = [4, 1, 7, 3, 8, 16]

print(f"Lista original: {numeros}")

lista_ordenada = ordenamiento_heap(numeros)

print(f"Lista ordenada: {lista_ordenada}")
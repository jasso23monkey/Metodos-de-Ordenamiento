import heapq

def merge_multiway(segmentos_ordenados):
    """
    Simula la fase de mezcla de múltiples vías.
    
    segmentos_ordenados: Una lista de listas (o iterables), donde cada lista
                         es un segmento de datos ya ordenado (una "vía").
    """
    
    # heapq.merge es la función de Python para realizar la mezcla de múltiples vías.
    # Recibe una colección de iterables (nuestras vías) y devuelve un solo iterable ordenado.
    lista_ordenada_final = list(heapq.merge(*segmentos_ordenados))
    
    return lista_ordenada_final

# --- Ejemplo de Uso ---

# En un sistema de disco real, estos "segmentos" serían los archivos temporales.
# Asumimos que ya han sido generados y ordenados en una fase previa.
via_1 = [1, 5, 8, 12]
via_2 = [2, 6, 9, 10]
via_3 = [3, 7, 11]

vias_de_entrada = [via_1, via_2, via_3]

print(f"Segmentos de entrada (Vías): {vias_de_entrada}")

lista_ordenada = merge_multiway(vias_de_entrada)

print(f"Lista ordenada (Mezcla de {len(vias_de_entrada)} vías): {lista_ordenada}")
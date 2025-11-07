import heapq

def merge_multiway_final(vias_de_entrada):
    """
    Función que realiza la mezcla de múltiples vías. 
    En Polyphase, esta función se llama repetidamente hasta que solo queda una vía.
    """
    # heapq.merge combina eficientemente todos los segmentos ordenados
    lista_ordenada_final = list(heapq.merge(*vias_de_entrada))
    return lista_ordenada_final

def polyphase_sort_simulacion(lista_de_runs):
    """
    Simulación de la mezcla polifásica.
    Asume que 'lista_de_runs' ya tiene la distribución Fibonacci óptima.
    """
    print("--- Simulación Polyphase Sort ---")
    
    # 1. Fase Inicial (Los runs ya han sido generados y distribuidos de forma óptima)
    print(f"Número inicial de vías: {len(lista_de_runs)}")
    
    # En un sistema real, mezclaríamos runs de dos vías a una tercera,
    # y repetiríamos hasta que todos los runs estuvieran en una sola vía.
    
    # 2. Mezcla de Múltiples Vías
    # El algoritmo sigue realizando mezclas 2-a-1 hasta condensar todo en una vía.
    while len(lista_de_runs) > 1:
        
        # En el Polyphase, se mezclan las dos vías con más runs (Vía A y Vía B) 
        # y el resultado va a la vía "vacía" o con menos runs (Vía C).
        # Aquí, simplemente mezclamos todos los runs en una gran lista ordenada.
        lista_ordenada = merge_multiway_final(lista_de_runs)
        
        # Simulación de la finalización: La lista completa es el resultado final.
        print(f"Mezclando {len(lista_de_runs)} vías en una sola...")
        
        # Rompemos el bucle porque ya simulamos la mezcla final
        return lista_ordenada
        
    return lista_de_runs[0] if lista_de_runs else []

# --- Ejemplo de Uso ---

# Ejemplo de 5 runs distribuidos en 3 vías (Fibonacci: 3, 2, 0 runs)
runs_via_A = [1, 5, 8]  # Un run
runs_via_B = [2, 6]     # Un run
runs_via_C = [3, 7]     # Otro run

# Para la simulación de mezcla, necesitamos que cada run sea su propia lista ordenada.
# En este ejemplo, tenemos 3 runs, cada uno en una "vía" simulada.
vias_iniciales = [runs_via_A, runs_via_B, runs_via_C]

print(f"Vías de entrada: {vias_iniciales}")

lista_ordenada = polyphase_sort_simulacion(vias_iniciales)

print(f"Lista completamente ordenada: {lista_ordenada}")
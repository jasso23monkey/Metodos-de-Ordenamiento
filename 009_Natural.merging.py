def merge_natural(lista):
    n = len(lista)
    
    # Bucle principal: se repite hasta que toda la lista sea una sola secuencia ordenada
    while True:
        # La lista de secuencias (runs) se llena en cada pasada
        runs = []
        i = 0
        
        # 1. IDENTIFICAR SECUENCIAS (RUNS)
        while i < n:
            # Encontrar el inicio de la secuencia
            inicio = i
            # Encontrar el final de la secuencia ordenada (el 'run')
            while i < n - 1 and lista[i] <= lista[i + 1]:
                i += 1
            # Añadir la secuencia (run) actual a la lista de runs
            runs.append(lista[inicio : i + 1])
            i += 1
        
        # Si solo hay una secuencia (run), la lista está completamente ordenada
        if len(runs) <= 1:
            # Reemplazar la lista original con la única secuencia ordenada y terminar
            lista[:] = runs[0] if runs else [] 
            break
            
        # 2. MEZCLAR PARES DE SECUENCIAS
        nueva_lista = []
        # Recorremos la lista de runs de dos en dos para mezclarlos
        for k in range(0, len(runs), 2):
            run_izq = runs[k]
            # Si hay un run derecho, lo mezclamos. Si no, solo añadimos el izquierdo.
            if k + 1 < len(runs):
                run_der = runs[k + 1]
                mezcla = merge_listas_aux(run_izq, run_der)
                nueva_lista.extend(mezcla)
            else:
                nueva_lista.extend(run_izq)
        
        # La lista original ahora es el resultado de la mezcla de pares
        lista[:] = nueva_lista

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

# Fíjate en el 10, 15, 8. Las secuencias naturales son [10, 15] y [8, 20, 5, 2]
numeros = [10, 15, 8, 20, 5, 2]

print(f"Lista original: {numeros}")

lista_ordenada = merge_natural(numeros)

print(f"Lista ordenada: {lista_ordenada}")

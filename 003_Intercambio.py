def ordenamiento_burbuja(lista):
    n = len(lista)
    
    # Recorre todos los elementos de la lista
    for i in range(n):
        # El último 'i' elemento ya está en su lugar
        # Por eso el segundo bucle solo va hasta n-i-1
        for j in range(0, n - i - 1):
            
            # Compara elementos adyacentes
            if lista[j] > lista[j + 1]:
                # Si el elemento actual es mayor que el siguiente, ¡intercámbialos!
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
    return lista

# --- Ejemplo de Uso ---

numeros = [5, 1, 4, 2, 8]

print(f"Lista original: {numeros}")

lista_ordenada = ordenamiento_burbuja(numeros)

print(f"Lista ordenada: {lista_ordenada}")
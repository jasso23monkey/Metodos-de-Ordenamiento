def counting_sort_por_digito(lista, exponente):
    """Ordena la lista según el dígito representado por 'exponente'."""
    
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10  # Para los dígitos 0 a 9

    # 1. Almacenar el conteo de ocurrencias del dígito
    for i in range(n):
        digito = (lista[i] // exponente) % 10
        conteo[digito] += 1

    # 2. Modificar el conteo para que contenga la posición real del dígito en 'salida'
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # 3. Construir el arreglo de salida (se recorre hacia atrás para mantener la estabilidad)
    i = n - 1
    while i >= 0:
        digito = (lista[i] // exponente) % 10
        conida_index = conteo[digito] - 1
        salida[conida_index] = lista[i]
        conteo[digito] -= 1
        i -= 1

    # Copiar el arreglo de salida a la lista original
    for i in range(n):
        lista[i] = salida[i]

# ---
def radix_sort(lista):
    # Encontrar el número máximo para determinar el número de dígitos (pasadas)
    max_num = max(lista)
    
    # Inicializar el exponente para el dígito actual (1 para unidades, 10 para decenas, etc.)
    exponente = 1
    
    # Repetir el Counting Sort para cada dígito
    # El bucle termina cuando 'exponente' es mayor que el número más grande
    while max_num // exponente > 0:
        counting_sort_por_digito(lista, exponente)
        exponente *= 10
    
    return lista

# --- Ejemplo de Uso ---

numeros = [170, 45, 75, 90, 802, 24, 2, 66]

print(f"Lista original: {numeros}")

lista_ordenada = radix_sort(numeros)

print(f"Lista ordenada: {lista_ordenada}")
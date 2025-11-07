def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci."""
    a, b = 0, 1
    if n == 0: return a
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def distribucion_polyphase_fibonacci(total_runs):
    """
    Calcula la distribución óptima de 'total_runs' en 3 vías (A, B, C)
    para el Polyphase Sort.
    """
    if total_runs <= 0:
        return {"Via A": 0, "Via B": 0, "Via C": 0}

    n = 0
    # Encontrar el número de Fibonacci Fn que es mayor o igual al total_runs
    while fibonacci(n) < total_runs:
        n += 1
    
    Fn = fibonacci(n)
    Fn_menos_1 = fibonacci(n - 1)
    
    # Calcular cuántos runs 'dummy' (ficticios) necesitamos para alcanzar el Fn
    dummy_runs = Fn - total_runs
    
    # Calcular la distribución real de runs (no ficticios)
    
    # La Vía A debe tener Fn runs
    runs_via_A = Fn - dummy_runs
    
    # La Vía B debe tener Fn-1 runs
    runs_via_B = Fn_menos_1 - dummy_runs
    
    # La Vía C es la vía de salida inicial, por lo tanto, tiene 0 runs.
    runs_via_C = 0

    return {
        "Total Runs Necesarios (Fn)": Fn,
        "Runs Ficticios (Dummy)": dummy_runs,
        "Distribucion Optima": {
            "Via A": runs_via_A,  # Mayor número de runs
            "Via B": runs_via_B,  # Siguiente número más alto
            "Via C": runs_via_C   # Cero
        }
    }

# --- Ejemplo de Uso ---

# Supongamos que generamos 10 runs (secuencias ordenadas) en la fase inicial.
runs_generados = 10 
distribucion = distribucion_polyphase_fibonacci(runs_generados)

print(f"Número de runs generados: {runs_generados}")
print("\n--- Distribución para Polyphase Sort ---")
for clave, valor in distribucion.items():
    print(f"{clave}: {valor}")
def encontrar_palabra_mas_larga(palabras):
    return max(palabras, key=lambda x: len(x))

# Ejemplo de uso
palabras = ["python", "es", "divertido"]
print(encontrar_palabra_mas_larga(palabras))  # Output: "divertido"
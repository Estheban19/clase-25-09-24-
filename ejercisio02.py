def fibonacci(n):
    a, b = 0, 1
    fibonacci = [a, b]
    for i in range(2, n):
        a, b = b, a + b
        fibonacci.append(b)
    return fibonacci

# Ejemplo de uso
n = 10
print(fibonacci(n))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
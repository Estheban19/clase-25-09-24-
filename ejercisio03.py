def verificar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if not any(char.isupper() for char in contraseña):
        return False
    if not any(char.islower() for char in contraseña):
        return False
    if not any(char.isdigit() for char in contraseña):
        return False
    if any(char.isspace() for char in contraseña):
        return False
    return True

# Ejemplo de uso
contraseña = input("Ingrese su contraseña: ")
if verificar_contraseña(contraseña):
    print("La contraseña es válida")
else:
    print("La contraseña no es válida")
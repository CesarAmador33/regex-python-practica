import re

def validar_contrasena_segura(contrasena: str) -> tuple[bool, list[str]]:
    """
    Verifica si una contraseña cumple con los criterios de seguridad 
    y lista los requisitos que no se cumplen.

    Args:
        contrasena (str): La cadena de texto a validar.

    Returns:
        tuple[bool, list[str]]: Una tupla con (es_valida, lista_de_errores).
    """
    
    # Lista para almacenar los errores de la contraseña
    errores = []

    # Criterios de la contraseña segura:
    
    # 1. Mínimo 8 caracteres de longitud
    if len(contrasena) < 8:
        errores.append("Mínimo 8 caracteres de longitud")

    # 2. Al menos una letra mayúscula
    if not re.search(r"[A-Z]", contrasena):
        errores.append("Al menos una letra mayúscula")

    # 3. Al menos una letra minúscula
    if not re.search(r"[a-z]", contrasena):
        errores.append("Al menos una letra minúscula")

    # 4. Al menos un número
    if not re.search(r"\d", contrasena):
        errores.append("Al menos un número")

    # 5. Al menos un carácter especial (@$!%*?&#)
    caracteres_especiales = r"[@$!%*?&#]"
    if not re.search(caracteres_especiales, contrasena):
        errores.append("Al menos un carácter especial (@$!%*?&#)")

    # Si la lista de errores está vacía, la contraseña es válida
    es_valida = len(errores) == 0
    
    return es_valida, errores

# Casos de Prueba 
print("--- Validador de Contraseñas Seguras ---")

casos = [
    "Segura123!",       #  Válida
    "contrasena",       #  Falta Mayúscula, Número, Especial
    "MAYUSCULA123!",    #  Falta Minúscula
    "P@ssw0rd",         #  Válida
    "Corta1!",          #  Falta Longitud
    "SoloLetras",       #  Falta Número, Especial
    "Numeros12345678"   #  Falta Mayúscula, Minúscula, Especial
]

for contrasena in casos:
    valida, fallos = validar_contrasena_segura(contrasena)
    
    print(f"\nContraseña: '{contrasena}'")
    if valida:
        print("ESTADO: ✅ VÁLIDA (Cumple todos los requisitos)")
    else:
        print("ESTADO: ❌ INVÁLIDA")
        print("  Criterios NO cumplidos:")
        for fallo in fallos:
            print(f"    - {fallo}")
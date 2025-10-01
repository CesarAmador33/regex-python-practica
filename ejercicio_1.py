import re

def es_correo_valido_simple(correo: str) -> bool:
    """
    Valida si una cadena de texto es un correo electrónico válido 
    siguiendo los requisitos básicos: usuario@dominio.extensión

    Args:
        correo (str): La cadena de texto a validar.

    Returns:
        bool: True si el correo es válido, False en caso contrario.
    """
    # Expresión regular simple:
    # 1. ^\S+       -> Inicia con uno o más caracteres que no sean espacios. (Usuario)
    # 2. @          -> Contiene el símbolo arroba.
    # 3. \S+\.      -> Sigue con uno o más caracteres no espaciales, y luego un punto. (Dominio)
    # 4. [a-zA-Z]{2,4}$ -> Termina con una extensión de 2 a 4 letras al final de la cadena.
    patron = r"^\S+@\S+\.[a-zA-Z]{2,4}$"
    
    # re.match() intenta aplicar el patrón al inicio de la cadena. 
    # Si encuentra una coincidencia, devuelve un objeto match; de lo contrario, None.
    return re.match(patron, correo) is not None

# --- Casos de Prueba ---
print("--- Casos de Prueba ---")

# Casos Válidos 
caso_valido_1 = "usuario@ejemplo.com"
caso_valido_2 = "nombre.apellido@dominio.mx"

print(f"'{caso_valido_1}' es válido: {es_correo_valido_simple(caso_valido_1)}")
print(f"'{caso_valido_2}' es válido: {es_correo_valido_simple(caso_valido_2)}")

# Casos Inválidos 
caso_invalido_1 = "usuarioejemplo.com" # Falta el @
caso_invalido_2 = "@ejemplo.com"       # Falta texto antes del @
caso_invalido_3 = "usuario@.com"       # Falta texto después del @
caso_invalido_4 = "usuario@ejemplo"    # Falta el punto y la extensión

print(f"'{caso_invalido_1}' es válido: {es_correo_valido_simple(caso_invalido_1)}")
print(f"'{caso_invalido_2}' es válido: {es_correo_valido_simple(caso_invalido_2)}")
print(f"'{caso_invalido_3}' es válido: {es_correo_valido_simple(caso_invalido_3)}")
print(f"'{caso_invalido_4}' es válido: {es_correo_valido_simple(caso_invalido_4)}")
import re

def extraer_telefonos(texto: str) -> list[str]:
    """
    Encuentra y extrae todos los números de teléfono mexicanos de 10 dígitos 
    en varios formatos de una cadena de texto.

    Args:
        texto (str): La cadena de texto de entrada.

    Returns:
        list[str]: Una lista de las cadenas de texto que coinciden con los números de teléfono.
    """
    
    # Expresión Regular para cubrir los 4 formatos:
    # 1. (\(\d{3}\)\s*|\d{3}[\s-]*): 
    #    - Coincide con el código de área entre paréntesis, opcionalmente seguido de espacio: (\(\d{3}\)\s*)
    #    - O (\s*|):
    #    - Coincide con el código de área seguido de un espacio o guion, opcionalmente: (\d{3}[\s-]*)
    # 2. \d{3}[\s-]*: Coincide con el siguiente bloque de 3 dígitos, opcionalmente seguido de espacio o guion.
    # 3. \d{4}: Coincide con los últimos 4 dígitos.
    
    # Unificando el patrón para simplificar y capturar todos los casos de 10 dígitos:
    patron = r"""
        (?:             # Grupo no capturador
            \(          # Paréntesis de apertura literal: (
            \d{3}       # Tres dígitos: XXX
            \)          # Paréntesis de cierre literal: )
            [\s-]?      # Un espacio o guion opcional: ' ' o '-'
        |               # O (Alternativa 1: Formato con paréntesis)
            \d{3}       # Tres dígitos: XXX
            [\s-]?      # Un espacio o guion opcional: ' ' o '-'
        )               # Fin del grupo de prefijo
        \d{3}           # Tres dígitos: XXX
        [\s-]?          # Un espacio o guion opcional: ' ' o '-'
        \d{4}           # Cuatro dígitos: XXXX
    """
    
    # Simplificación: Una expresión más compacta que usa '?' para hacer los separadores opcionales
    # Este patrón cubre mejor la variedad requerida, incluyendo el formato sin separadores (10 dígitos seguidos):
    patron_simplificado = r'\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}'
    
    # re.findall busca todas las coincidencias del patrón en el texto y devuelve una lista de ellas.
    return re.findall(patron_simplificado, texto)

# Caso de Prueba 
texto_entrada = "Contacta a Juan al 646-123-4567 o a María al (664) 987-6543. También puedes llamar al 5551234567. Aquí hay otro 999 000 1111 y uno inválido 123456789."

telefonos_encontrados = extraer_telefonos(texto_entrada)

print(f"Texto de entrada:\n'{texto_entrada}'\n")
print(f"Teléfonos encontrados: {telefonos_encontrados}")

# Verificación de formatos individuales
print("\n--- Verificación Individual ---")
print(f"6461234567: {extraer_telefonos('6461234567')}")
print(f"646-123-4567: {extraer_telefonos('646-123-4567')}")
print(f"646 123 4567: {extraer_telefonos('646 123 4567')}")
print(f"(646) 123-4567: {extraer_telefonos('(646) 123-4567')}")
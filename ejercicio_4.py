import re

def extraer_y_analizar_urls(texto: str):
    """
    Extrae todas las URLs de un texto y descompone cada URL en 
    Protocolo, Dominio y Ruta.
    
    Args:
        texto (str): La cadena de texto de entrada.
    """
    
    # 1. Patrón para ENCONTRAR todas las URLs
    # Cubre http://, https://, y www. al inicio. 
    # Luego captura el resto de caracteres válidos para una URL.
    url_patron_general = r"(?:https?://|www\.)[^\s]+"
    
    # re.findall() encuentra todas las URLs que coinciden con el patrón
    urls_encontradas = re.findall(url_patron_general, texto)
    
    # 2. Patrón para DESCOMPONER una URL (usando grupos de captura)
    # Grupo 1 (Protocolo): (https?://)? - Captura http:// o https:// de forma opcional.
    # Grupo 2 (Dominio): ([a-zA-Z0-9.-]+) - Captura el dominio y subdominios (ej. www.google.com).
    # Grupo 3 (Ruta): (/[^\s]*) - Captura la ruta/path opcionalmente (ej. /pagina).
    descomposicion_patron = re.compile(
        r"^(https?://)?"  # Grupo 1: Protocolo (opcional)
        r"([a-zA-Z0-9.-]+)" # Grupo 2: Dominio/Subdominio (requerido)
        r"(/.*)?$",        # Grupo 3: Ruta (opcional)
        re.IGNORECASE      # Ignorar mayúsculas/minúsculas en el protocolo/dominio
    )
    
    print(" Análisis de URLs ")
    
    for i, url in enumerate(urls_encontradas):
        # Limpiar la URL de caracteres finales no deseados (como comas o puntos)
        url_limpia = url.rstrip('.,\'\"')
        
        # Intentar descomponer la URL
        match = descomposicion_patron.match(url_limpia)
        
        if match:
            protocolo = match.group(1) if match.group(1) else "N/A (Implícito)"
            dominio = match.group(2)
            ruta = match.group(3) if match.group(3) else "N/A"
            
            # Formateo de la salida
            print(f"\nURL {i+1}: {url_limpia}")
            
            # Ajustar el formato del protocolo para los casos 'www.'
            if url_limpia.startswith('www.') and protocolo == "N/A (Implícito)":
                protocolo = "http/https (Implícito)"

            print(f"  Protocolo: {protocolo.rstrip('://')}")
            print(f"  Dominio: {dominio}")
            if ruta != "N/A":
                print(f"  Ruta: {ruta}")
        else:
            print(f"\nURL {i+1}: {url_limpia} (No se pudo descomponer completamente)")


# Caso de Prueba 
texto_entrada = "Visita https://www.google.com o http://github.com/usuario. También puedes ir a www.python.org/downloads para más info. Mira este enlace sin protocolo: www.ejemplo.com/pagina, y otro: http://test.net."

extraer_y_analizar_urls(texto_entrada)

#AMADORCESAR
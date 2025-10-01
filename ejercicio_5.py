import re
from datetime import datetime

def analizar_y_formatear_fechas(texto: str):
    """
    Encuentra fechas en varios formatos dentro de un texto y las convierte 
    al formato estándar YYYY-MM-DD.

    Args:
        texto (str): La cadena de texto de entrada.
    """
    
    # Mapeo de meses abreviados y completos para la localización en español
    # Nota: Los patrones de 're' solo capturarán los nombres o abreviaciones.
    meses_espanol = {
        'Ene': '01', 'Feb': '02', 'Mar': '03', 'Abr': '04', 
        'May': '05', 'Jun': '06', 'Jul': '07', 'Ago': '08', 
        'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dic': '12',
        'Enero': '01', 'Febrero': '02', 'Marzo': '03', 'Abril': '04',
        'Mayo': '05', 'Junio': '06', 'Julio': '07', 'Agosto': '08',
        'Septiembre': '09', 'Octubre': '10', 'Noviembre': '11', 'Diciembre': '12'
    }
    
    # 1. Definición de Patrones de Regex
    
    # DD/MM/YYYY: \d{2}/\d{2}/\d{4}
    patron_1 = r"\d{2}/\d{2}/\d{4}"
    
    # YYYY-MM-DD: \d{4}-\d{2}-\d{2}
    patron_2 = r"\d{4}-\d{2}-\d{2}"
    
    # DD-MMM-YYYY: \d{2}-[A-Za-z]{3}-\d{4}
    patron_3 = r"\d{2}-(" + "|".join(meses_espanol.keys()) + r")-\d{4}"
    
    # Mes DD, YYYY: [A-Za-z]+ \d{1,2}, \d{4}
    nombres_meses = "|".join(re.escape(m) for m in meses_espanol if len(m) > 3)
    patron_4 = r"(" + nombres_meses + r")\s+\d{1,2},\s+\d{4}"

    # Combinar todos los patrones con una tubería (|)
    patron_combinado = re.compile(f"({patron_1})|({patron_2})|({patron_3})|({patron_4})", re.IGNORECASE)

    # Buscar todas las coincidencias
    fechas_encontradas = patron_combinado.findall(texto)

    print("Fechas encontradas y convertidas:")
    
    for match_tuple in fechas_encontradas:
        # El resultado de findall para patrones con grupos es una tupla,
        # donde solo un elemento (la fecha coincidente) no estará vacío.
        fecha_original = next(s for s in match_tuple if s)
        
        try:
            # 2. Determinar el formato original y parsear
            
            fecha_dt = None
            formato_dt = None
            
            if re.match(patron_1, fecha_original):
                formato_dt = "%d/%m/%Y"
            elif re.match(patron_2, fecha_original):
                formato_dt = "%Y-%m-%d"
            elif re.match(patron_3, fecha_original, re.IGNORECASE):
                # Para DD-MMM-YYYY, primero reemplazamos el nombre del mes con su número 
                # (ya que strptime puede tener problemas con nombres localizados)
                partes = re.split(r'[-]', fecha_original)
                dia = partes[0]
                mes_str = partes[1]
                anio = partes[2]
                
                mes_num = meses_espanol.get(mes_str.capitalize(), meses_espanol.get(mes_str.lower().capitalize()))
                if mes_num:
                    fecha_dt = datetime(int(anio), int(mes_num), int(dia))
                
            elif re.match(patron_4, fecha_original, re.IGNORECASE):
                # Para Mes DD, YYYY, reemplazamos el nombre del mes
                partes = re.split(r'[,\s]+', fecha_original.strip())
                mes_str = partes[0]
                dia = partes[1]
                anio = partes[2]
                
                mes_num = meses_espanol.get(mes_str.capitalize(), meses_espanol.get(mes_str.lower().capitalize()))
                if mes_num:
                    fecha_dt = datetime(int(anio), int(mes_num), int(dia))
                    
            
            # Si se pudo determinar el formato simple (patron 1 y 2), usar strptime
            if formato_dt:
                fecha_dt = datetime.strptime(fecha_original, formato_dt)

            # 3. Formatear la fecha al estándar YYYY-MM-DD
            if fecha_dt:
                fecha_estandar = fecha_dt.strftime("%Y-%m-%d")
                print(f"- Formato original: {fecha_original} → Estándar: {fecha_estandar}")
            else:
                print(f"- Formato original: {fecha_original} → Estándar: ERROR (No se pudo parsear el mes)")

        except ValueError:
            print(f"- Formato original: {fecha_original} → Estándar: ERROR (Formato inválido o fecha inexistente)")


# --- Caso de Prueba ---
texto_entrada = "La reunión es el 15/03/2024. El proyecto inicia el 2024-04-20 y termina en Junio 30, 2024. La entrega final es 01-Jul-2024. Otro evento en Diciembre 01, 2024."

analizar_y_formatear_fechas(texto_entrada)
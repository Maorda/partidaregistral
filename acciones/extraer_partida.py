# Archivo: acciones/extraer_partida.py
import nodriver as uc

# Importación ultra limpia gracias a __init__.py
from acciones import (
    seleccionar_oficina,
    seleccionar_area,
    configurar_criterio_partida,
    ejecutar_busqueda_y_esperar_spinner,
    verificar_estado_y_previsualizar
)

async def extraer_partida(page: uc.Tab, oficina: str, area: str, partida: str) -> bool:
    print(f"\n=========================================")
    print(f"PROCESANDO PARTIDA: {partida} en {oficina}")
    print(f"=========================================")
    
    try:
        # El flujo se mantiene idéntico y seguro
        await seleccionar_oficina(page, oficina)
        await seleccionar_area(page, area)
        await configurar_criterio_partida(page, partida)
        await ejecutar_busqueda_y_esperar_spinner(page)
        
        exito = await verificar_estado_y_previsualizar(page)
        return exito
            
    except Exception as e:
        print(f"[-] Error crítico en la orquestación: {e}")
        await page.save_screenshot("error_critico_orquestador.png")
        return False
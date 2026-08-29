import random
import nodriver as uc

async def verificar_estado_y_previsualizar(page: uc.Tab) -> bool:
    print("[Acción] Validando respuestas del servidor...")
    await page.sleep(0.5)
    
    # Comprobar si saltó el modal con el error ORA de base de datos
    modal_error = await page.select('.modal-body, .alert-danger, snack-bar-container')
    
    if modal_error and "bad SQL grammar" in modal_error.text:
        print(f"\n[-] ERROR DETECTADO: El servidor devolvió un fallo SQL.")
        await page.save_screenshot("error_sql_sunarp.png")
        
        boton_cerrar = await page.select('.modal-footer button, .btn-close')
        if boton_cerrar:
            await boton_cerrar.click()
        return False # Detiene el flujo de este registro
        
    print("[Acción] Todo limpio. Procediendo a Previsualizar...")
    boton_previsualizar = await page.select('button.btn-preview')
    await boton_previsualizar.click()
    await page.sleep(3.0)
    return True

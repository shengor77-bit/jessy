# Proyecto de Automatización de Pruebas para SauceDemo

## Propósito del Proyecto
Este proyecto automatiza pruebas de funcionalidad en el sitio web www.saucedemo.com, específicamente el proceso de login y la interacción con el carrito de compras. Utiliza Selenium WebDriver para simular interacciones del usuario y Pytest para estructurar y ejecutar las pruebas.

## Tecnologías Utilizadas
- **Python**: Lenguaje principal de programación.
- **Pytest**: Framework para la ejecución de pruebas.
- **Selenium WebDriver**: Para la automatización de navegadores web.
- **Webdriver Manager**: Para la gestión automática de drivers de navegador.
- **Git y GitHub**: Para control de versiones.

## Instalación de Dependencias
1. Asegúrate de tener Python instalado (versión 3.8 o superior).
2. Instala las dependencias ejecutando:
   ```
   pip install -r requirements.txt
   ```

## Estructura del Proyecto
- `tests/`: Contiene los archivos de pruebas separados (test_login.py, test_cart.py).
- `utils/`: Funciones auxiliares (helpers.py).
- `reports/`: Reportes HTML generados por Pytest.
- `datos/`: Carpeta para datos externos (si aplica).
- `requirements.txt`: Lista de dependencias.
- `README.md`: Este archivo.

## Cómo Ejecutar las Pruebas
Para ejecutar las pruebas y generar un reporte HTML:
```
pytest tests/ -v --html=reports/reporte.html
```

Esto ejecutará todas las pruebas en el directorio `tests/` en modo verbose y generará un reporte en `reports/reporte.html`.

## Casos de Prueba
1. **Login Exitoso** (test_login.py): Valida el login con credenciales válidas y redirección a la página de inventario.
2. **Añadir al Carrito** (test_cart.py): Añade un producto, verifica el contador del carrito, navega al carrito y confirma el producto.

## Notas
- Las pruebas están diseñadas para ser independientes.
- Se utilizan esperas explícitas para asegurar la carga de elementos.
- El código incluye comentarios descriptivos para mayor legibilidad.
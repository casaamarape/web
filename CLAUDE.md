# Casa Amara · Tienda web

Tienda online de Casa Amara (regalos personalizados, flores y boxes en Lima). Página estática publicada en Netlify desde este repositorio: cada cambio en la rama `main` se publica solo en 1–2 minutos.

## Estructura
- `index.html` → la página publicada. **No se edita a mano**: se genera con `python3 fuente/construir.py`.
- `fuente/plantilla.html` → diseño, estilos y código de la página (tiene los marcadores `__PRODUCTS__` y `__MENU__`).
- `fuente/productos.json` → catálogo: `id`, `name`, `price`, `old` (precio anterior, opcional), `items` (contenido), `grp`/`sub` (grupo original), `home` (categoría principal para migas y relacionados), `cumple` (orden en Cumpleaños), `pm: 1` (solo turno tarde), `variants` (opciones con precio), `lead` (días de anticipación).
- `fuente/menu.json` → menú: categorías (`k`, `l` nombre, `d` descripción, `cover` foto de portada, `more: true` si va dentro de "Más") con subcategorías (`subs`) y la lista de productos (`ids`). Un producto puede estar en varias.
- `img/<id>.jpg` → foto de cada producto (el nombre del archivo es el `id`).
- `assets/` → logos del manual de marca.
- `netlify/functions/chat.js` → chat con Google Gemini. La clave va SOLO en la variable de entorno `GEMINI_API_KEY` de Netlify. **Nunca escribir la clave en ningún archivo.**
- `netlify/functions/catalog.json` → catálogo que usa el chat. Se genera junto con `index.html`.

## Cómo hacer un cambio
1. Editar `fuente/plantilla.html`, `fuente/productos.json` o `fuente/menu.json`.
2. Ejecutar `python3 fuente/construir.py` (valida que el menú solo use productos existentes y avisa si falta alguna foto).
3. Guardar en el repositorio `index.html`, `netlify/functions/catalog.json` y los archivos fuente que cambiaron.

- Producto nuevo: agregarlo a `productos.json`, poner su foto en `img/<id>.jpg` y agregar su `id` en las categorías y subcategorías que correspondan de `menu.json`.
- Borrar un producto: quitarlo de `productos.json` y de todas las listas de `menu.json`.
- Cambiar un precio: editar `price` en `productos.json`.

## Reglas de marca
- Mantener la paleta, las fuentes (Bodoni Moda para títulos y Poppins para textos) y el estilo minimalista y elegante. Nada recargado ni "vulgar".
- Todos los textos van en español de Perú, con tono cálido.
- La página debe verse bien en celular: menú ☰ debajo de 1060 px y 3 productos por fila en celular. Comprobar siempre en un ancho de 390 px.
- Las compras se envían por WhatsApp al 51988869994. La dedicatoria tiene un máximo de 400 caracteres.
- Contacto: casaamara.pe@gmail.com · Instagram @casaamaraperu · TikTok @casaamara.pe · Facebook casaamaraperu.
- Turnos de entrega: primero de 9 a. m. a 1 p. m. y segundo de 12 m. a 6 p. m. Los productos con `pm: 1` solo se entregan en el segundo turno.

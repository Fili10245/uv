# Portal Académico — notas para Claude

Sitio estático (HTML + CSS) publicado con GitHub Pages desde `main`: https://fili10245.github.io/uv

## Estructura
- `index.html` — portada con tarjetas de cursos.
- Cursos: `FTMomentum.html`, `fluidos.html`, `reactores.html`, `numericos.html`.
- `assets/style.css` — estilos compartidos por todas las páginas (tema oscuro, encabezado blanco, acento teal `--accent`).
- `assets/site.js` — pestañas de código, botón copiar, resaltado de la semana visible.
- `codigo/matlab/`, `codigo/python/` — programas; `pdf/<curso>/` — PDFs publicados; `notas/` — apuntes .md (por crear).

## Convenciones
- Cada semana es `<section id="sN" class="week">` con su enlace `#sN` en la barra lateral.
- Botones de recursos: `class="res"` (activo) o `class="res pending"` (archivo aún no subido: se ve "próximamente" y no es clicable). Al subir el archivo, quitar `pending`.
- Fórmulas con MathJax (`$...$`, `$$...$$`), notación de Fogler (Θ_i, ν_i, Q̇g, Q̇r).
- Componentes: `.formula`, `.pair` (dos columnas, p. ej. balance de moles | energía), `.callout` (condición de validez), `table.stoich`, `figure.fig`, `.code-block` con pestañas MATLAB/Python.
- Ecuaciones verificadas contra Fogler (5.ª ed., 2016) y Froment (3.ª ed.); citar número de ecuación.

## Flujo de trabajo
- Mostrar los cambios (abrir la página en el navegador) y publicar (commit + push) solo cuando el profesor lo pida.
- Publicar solo versiones para alumnos: nunca claves de respuestas.
- Si un material puede ir en más de un lugar, preguntar.

# Portal Académico de Ingeniería

Sitio web académico desarrollado para la organización y distribución de material educativo en cursos de ingeniería impartidos por **Prof. Fili**.

---

## 🌐 Sitio web

Accede al portal en:

👉 https://fili10245.github.io/uv/

---

## 👨‍🏫 Profesor

**Prof. Fili**  
Universidad Veracruzana  

---

## 📚 Cursos disponibles

El portal está estructurado en tres cursos principales:

### 🔹 Fundamentos de Transferencia de Momentum
- Conceptos básicos: esfuerzo y viscosidad  
- Ecuaciones de transporte  
- Balance de cantidad de movimiento  

### 🔹 Mecánica de Fluidos
- Propiedades de los fluidos  
- Estática de fluidos  
- Análisis de presión y fuerzas  

### 🔹 Métodos Numéricos
- Métodos de raíces (Bisección, Newton-Raphson)  
- Sistemas de ecuaciones  
- Técnicas computacionales  

---

## 🧱 Estructura del sitio

El sitio sigue una arquitectura tipo plataforma educativa:

- **Página principal (`index.html`)**  
  Portal de entrada con acceso a cada curso  

- **Páginas por curso**  
  - `FTMomentum.html`  
  - `fluidos.html`  
  - `reactores.html`  
  - `numericos.html`  

Cada curso incluye:

- Organización por semanas  
- Notas (`.md`), PDF, video y código MATLAB/Python  
- Bibliografía, software y criterios de evaluación  

---

## 📁 Estructura del repositorio

```
uv/
├── index.html          # portada con acceso a cada curso
├── FTMomentum.html
├── fluidos.html
├── reactores.html
├── numericos.html
├── CauchyDeriv.png
│
├── assets/
│   ├── style.css       # estilos compartidos por TODAS las páginas
│   └── site.js         # pestañas de código, copiar, resaltado de semana
│
├── codigo/
│   ├── matlab/         # scripts .m
│   └── python/         # scripts .py
│
├── notas/              # (por crear) apuntes .md por semana
└── pdf/                # (por crear) lecturas, guías y tareas
```

### Agregar un recurso

Los botones con borde punteado (`class="res pending"`) aparecen como
**“próximamente”** y no son clicables. Al subir el archivo correspondiente,
quita `pending` de la clase del botón para activarlo.

---

## ⚙️ Tecnologías utilizadas

- HTML5  
- CSS compartido (`assets/style.css`) · diseño oscuro con acento teal  
- MathJax para fórmulas  
- GitHub Pages  

---

## 🚀 Despliegue

El sitio se publica automáticamente mediante GitHub Pages desde la rama `main`.

---

## 🎯 Objetivo del proyecto

- Centralizar contenido académico  
- Facilitar el acceso a materiales de curso  
- Apoyar el aprendizaje en ingeniería  
- Proveer una estructura clara tipo plataforma educativa  

---

## 🎨 Características del diseño

- Estética moderna en tonos negro, gris y blanco  
- Sección principal (hero) con fondo visible y overlay claro  
- Navegación intuitiva tipo plataforma (inspirada en sitios educativos)  
- Estructura escalable por cursos  

---

## 📌 Notas

- Los enlaces a PDFs y tareas están en desarrollo  
- Los archivos `.md` funcionan como base del contenido académico  
- El sitio está diseñado para crecer hacia una plataforma educativa completa  

---

## 📄 Licencia

Uso educativo.

# SOS Software

Este es un proyecto Django con integración de Bootstrap para crear una aplicación web moderna y responsiva.

## Estructura del Proyecto

```
SOS_software/
├── base/                      # Aplicación principal
│   ├── templates/             # Plantillas HTML
│   │   └── base/              # Plantillas específicas de la app base
│   │       ├── base.html      # Plantilla base (layout principal)
│   │       └── home.html      # Plantilla de inicio que extiende base.html
│   ├── views.py               # Vistas de la aplicación
│   └── urls.py                # URLs de la aplicación
├── core/                      # Configuración del proyecto Django
│   ├── settings.py            # Configuración general
│   └── urls.py                # URLs del proyecto
├── static/                    # Archivos estáticos
│   ├── css/                   # Hojas de estilo
│   │   └── styles.css         # Estilos personalizados
│   ├── js/                    # JavaScript
│   │   └── main.js            # Scripts personalizados
│   └── img/                   # Imágenes
└── manage.py                  # Script de gestión de Django
```

## Cómo Integrar un Template de Bootstrap

### 1. Preparación

Cuando descargues un template de Bootstrap, generalmente contendrá:

- Archivos HTML
- Carpeta CSS con estilos
- Carpeta JS con scripts
- Carpeta de imágenes o assets

### 2. Organización de Archivos

1. **Archivos CSS**: Coloca los archivos CSS del template en `static/css/`
2. **Archivos JavaScript**: Coloca los archivos JS en `static/js/`
3. **Imágenes y otros assets**: Colócalos en `static/img/` o crea subcarpetas según sea necesario

### 3. Adaptación del HTML

Para integrar el HTML del template en el proyecto Django:

1. **Modifica la plantilla base**: Actualiza `base/templates/base/base.html` con la estructura del template
   - Mantén los bloques `{% block %}` para permitir la extensión
   - Usa `{% load static %}` y `{% static 'ruta/archivo' %}` para referencias a archivos estáticos
   - Usa `{% url 'nombre_url' %}` para enlaces internos

2. **Crea plantillas específicas**: Para cada página del template, crea un archivo HTML que extienda base.html
   ```html
   {% extends 'base/base.html' %}
   
   {% block title %}Título de la Página{% endblock %}
   
   {% block content %}
   <!-- Contenido específico de esta página -->
   {% endblock %}
   ```

### 4. Personalización

Para personalizar el template a tu gusto:

1. **Modifica los estilos**: Edita `static/css/styles.css` o agrega nuevos archivos CSS
2. **Personaliza los scripts**: Edita `static/js/main.js` o agrega nuevos archivos JS
3. **Actualiza las vistas**: Modifica `base/views.py` para renderizar las plantillas adecuadas
4. **Configura las URLs**: Actualiza `base/urls.py` para mapear URLs a vistas

### 5. Consejos para la Integración

- **Mantén la estructura de bloques**: Usa el sistema de bloques de Django para hacer tu código modular
- **Separa contenido de presentación**: Usa la herencia de plantillas para evitar duplicación
- **Usa componentes reutilizables**: Crea inclusiones con `{% include 'ruta/componente.html' %}` para elementos que se repiten
- **Aprovecha el contexto**: Pasa datos desde las vistas a las plantillas para contenido dinámico

## Ejecución del Proyecto

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor de desarrollo
python manage.py runserver
```

Visita http://127.0.0.1:8000/ en tu navegador para ver el sitio.

## Docker

También puedes ejecutar el proyecto usando Docker:

```bash
# Construir la imagen
docker-compose build

# Iniciar los contenedores
docker-compose up
```

Visita http://localhost:8000/ en tu navegador para ver el sitio.

## Cambios Realizados

### Configuración de Archivos Estáticos

Se ha configurado correctamente el manejo de archivos estáticos en Django:

```python
# En settings.py
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

### Imágenes SVG

Se han creado imágenes SVG personalizadas para reemplazar las imágenes de placeholder:

- `static/img/banner.svg`: Banner principal para la página de inicio
- `static/img/avatar.svg`: Avatar genérico para los testimonios

### Animaciones CSS

Se ha agregado una animación de pulso para los botones:

```css
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.pulse {
    animation: pulse 0.5s ease;
}
```

### Próximos Pasos

1. Agregar más páginas al sitio (Acerca de, Servicios, Contacto, etc.)
2. Implementar formularios de contacto
3. Mejorar la responsividad en dispositivos móviles
4. Agregar más animaciones y efectos visuales
# Biblioteca Saber y Conocimiento

## Descripción del proyecto

El proyecto consiste en desarrollar un sitio web para la **Biblioteca Saber y Conocimiento**, utilizando Flask y HTML. El sitio permite consultar información general de la biblioteca, explorar su catálogo de materiales, conocer los servicios disponibles y encontrar los medios de contacto.

## Tecnologías utilizadas

- **Python:** lenguaje de programación utilizado para desarrollar la aplicación.
- **Flask:** framework utilizado para crear el servidor y administrar las rutas.
- **HTML:** lenguaje utilizado para estructurar las páginas web.
- **Bootstrap:** herramienta utilizada para organizar y dar formato al contenido.
- **Jinja2:** motor de plantillas que permite utilizar variables y reutilizar estructuras HTML.

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

```text
appweb01/
├── server.py
├── README.md
└── templates/
    ├── layout.html
    ├── index.html
    ├── catalogo.html
    ├── servicios.html
    └── contacto.html
```

## Requisitos técnicos implementados

### 1. Archivo `server.py`

Es el punto de entrada de la aplicación. En este archivo se importa Flask, se crea la aplicación y se definen las rutas que permiten acceder a las diferentes páginas.

### 2. Creación de cuatro rutas

Se implementaron cuatro rutas principales:

- **Inicio (`/`):** presenta el nombre de la biblioteca, el mensaje de bienvenida, su propósito y el horario de atención.
- **Catálogo (`/catalogo`):** muestra las categorías de materiales disponibles: libros, revistas, tesis y recursos digitales.
- **Servicios (`/servicios`):** describe los servicios de préstamo de libros, consulta en sala, acceso a recursos digitales y orientación bibliográfica.
- **Contacto (`/contacto`):** muestra una dirección ficticia, un correo electrónico institucional ficticio y el horario de atención.

### 3. Uso de `render_template()`

La función `render_template()` permite cargar las plantillas HTML almacenadas en la carpeta `templates`.

Ejemplo de uso:

```python
return render_template(
    'index.html',
    titulo='Inicio',
    mensaje='Bienvenido a nuestra biblioteca'
)
```

### 4. Variables `titulo` y `mensaje`

Las funciones de las rutas envían las variables `titulo` y `mensaje` a las plantillas.

- **`titulo`:** contiene el título de la página.
- **`mensaje`:** contiene el mensaje introductorio de la sección.

Estas variables se muestran mediante la sintaxis de Jinja2:

```html
<h1>{{ titulo }}</h1>
<p>{{ mensaje }}</p>
```

### 5. Plantilla base `layout.html`

La plantilla `layout.html` contiene la estructura general del sitio web y los elementos compartidos por todas las páginas, como el menú de navegación y los recursos de estilo.

Su objetivo es evitar la repetición de código y mantener un diseño uniforme.

### 6. Herencia de plantillas con `extends`

Las cuatro plantillas hijas utilizan la instrucción:

```html
{% extends "layout.html" %}
```

Esta instrucción permite reutilizar la estructura definida en `layout.html` sin tener que escribirla nuevamente en cada archivo.

### 7. Bloque `content`

Cada plantilla hija utiliza el bloque `content` para definir su contenido particular.

```html
{% block content %}
    <div class="container-fluid">
        <h1>{{ titulo }}</h1>
        <p>{{ mensaje }}</p>
    </div>
{% endblock %}
```

De esta manera, cada página presenta información diferente mientras conserva la estructura general del sitio.

### 8. Menú de navegación

El menú de navegación se encuentra en `layout.html` y permite acceder a las cuatro páginas del sitio.

Se utiliza la función `url_for()` para generar los enlaces de navegación a partir de los nombres de las funciones definidas en Flask.

Ejemplo:

```html
<a href="{{ url_for('index') }}">Inicio</a>
```

Esto facilita la navegación y evita escribir manualmente las direcciones de las páginas.

### 9. Uso de `container-fluid`

La clase `container-fluid` de Bootstrap permite organizar el contenido utilizando todo el ancho disponible de la ventana del navegador.

Ejemplo:

```html
<div class="container-fluid">
    <h1>{{ titulo }}</h1>
    <p>{{ mensaje }}</p>
</div>
```

Esta clase facilita la distribución del contenido en diferentes tamaños de pantalla.

### 10. Verificación del funcionamiento

Se debe comprobar que todos los elementos del sitio funcionen correctamente.

- [ ] El servidor inicia mediante `server.py`.
- [ ] La página de Inicio muestra la información de bienvenida.
- [ ] El Catálogo presenta las cuatro categorías de materiales.
- [ ] Servicios muestra las descripciones de los servicios disponibles.
- [ ] Contacto presenta la dirección, el correo y el horario.
- [ ] El menú permite navegar entre las cuatro páginas.
- [ ] Las plantillas muestran correctamente las variables `titulo` y `mensaje`.

## Instrucciones de ejecución

Para ejecutar el proyecto, sigue estos pasos:

1. Abrir una terminal en la carpeta principal del proyecto.
2. Activar el entorno virtual, si se utiliza uno.
3. Instalar Flask si todavía no está instalado:

   ```bash
   pip install flask
   ```

4. Ejecutar el archivo principal:

   ```bash
   python server.py
   ```

5. Abrir el navegador y acceder a la siguiente dirección:

   `http://127.0.0.1:5000/`

## Conclusión

Este proyecto permite practicar los fundamentos del desarrollo web con Flask, incluyendo la creación de rutas, el envío de variables a las plantillas, la reutilización de código mediante herencia de
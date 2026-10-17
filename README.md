# Componente Práctico 1: Inicialización y flujo de trabajo en Django

**Asignatura:** Estructura de Datos, UNEMI (Carrera de Ingeniería de Software)
**Docente:** Ing. Guevara Reyes Rodrigo Josue
**Integrantes:** Alfredo Josua Cruz Chalen

Demostración introductoria de Django 5.2: un proyecto (`proyecto_demo`) con una aplicación (`inicio`) que recibe una petición, prepara un contexto en la vista y renderiza una plantilla HTML.

## Cómo ejecutarlo (Windows / PowerShell)

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abrir **http://127.0.0.1:8000/** en el navegador.

## Estructura

```
demo_django/
├── manage.py
├── requirements.txt
├── proyecto_demo/        ← proyecto (configuración y rutas principales)
│   ├── settings.py       ← "inicio" registrado en INSTALLED_APPS
│   ├── urls.py           ← path('', include('inicio.urls'))
│   ├── asgi.py
│   └── wsgi.py
└── inicio/               ← aplicación
    ├── urls.py           ← creado manualmente: path('', views.inicio)
    ├── views.py          ← vista con render() y diccionario de contexto
    ├── models.py
    ├── admin.py
    ├── apps.py
    ├── tests.py
    ├── migrations/
    └── templates/inicio/inicio.html   ← plantilla con {{ titulo }} y {{ mensaje }}
```

## Flujo petición → respuesta

Navegador → `proyecto_demo/urls.py` → `inicio/urls.py` → `views.inicio` → plantilla + contexto → respuesta HTML → navegador.

## Referencias

- https://docs.djangoproject.com/en/5.2/intro/tutorial01/
- https://docs.djangoproject.com/en/5.2/intro/tutorial03/
- https://docs.djangoproject.com/en/5.2/faq/general/

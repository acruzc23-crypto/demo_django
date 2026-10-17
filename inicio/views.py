from django.shortcuts import render


def inicio(request):
    """Vista que recibe la petición, prepara el contexto y devuelve HTML con render."""
    contexto = {
        'titulo': 'Componente Práctico - Estructura de Datos',
      'mensaje': 'Hola, somos los estudiantes de Estructura de Datos - UNEMI',
        'flujo': [
            'Navegador',
            'urls.py del proyecto',
            'urls.py de la aplicación',
            'views.py (vista)',
            'Plantilla + contexto',
            'Respuesta HTML',
        ],
    }
    # Si se necesitaran datos de una base de datos, aquí se consultaría
    # un modelo definido en models.py (por ejemplo: Estudiante.objects.all()).
    return render(request, 'inicio/inicio.html', contexto)

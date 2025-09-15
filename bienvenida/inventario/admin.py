from django.contrib import admin

# importar un modelo para aplicarlo en localhost:8000/admin
from .models import Producto
# una vez importado vamos a registralo en la vista
admin.site.register(Producto)

# Para acceder al panel de admin
# debes de aplicar los siguientes comandos:
# python manage.py createsuperuser
# username: admin
# email: (vacio)
# password: admin

#!/bin/sh

exec python3 cargar_precios.py &
exec python3 "pagina-django/manage.py" runserver 0.0.0.0:6555 --verbosity 0

#exec python3 prueba.py
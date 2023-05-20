# preentrega_pabloz
## Plataforma Python - Preentrega

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Intrucciones para ejecutar el servidor.
+ Comando para ejecutar el servidor:
```
python manage.py runserver
```
+ Ahora podras acceder a la pagina via:
```
127.0.0.1:8000/
```

## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```

# Superusuario de pruebas
username:admin
contraseña:admin
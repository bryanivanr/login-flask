# Login con Flask

Es una página web donde un usuario puede crear una cuenta, iniciar sesión
y ver un mensaje de que entró correctamente. Las contraseñas se guardan
protegidas con hash, asi que nadie puede leerlas en la base de datos.

## Qué necesitas
- Python instalado

## Cómo usarlo
1. Abre una terminal en la carpeta del proyecto.
2. Instala lo necesario:
   pip install -r requirements.txt
3. Inicia la página:
   python app.py
4. Abre en tu navegador: http://127.0.0.1:5000

## Cómo funciona
1. Pulsa "Regístrate" y crea una cuenta (la contraseña debe tener mínimo 9 caracteres).
2. Inicia sesión con ese usuario y contraseña.
3. Verás un mensaje de que el inicio de sesión fue exitoso.
4. Pulsa "Cerrar sesión" para salir.

## Archivos principales
- app.py: el programa principal
- templates: las páginas (login, registro y mensaje de éxito)
- static: los estilos y el código de validación del formulario


# API REST con Flask para gestión de mensajes con autenticación JWT
-Api Restfull para procesar mensajes de plataforma de chat , procesamiento , validación de mensajes, y autenticacion JWT
## 🚀 Instalación

### 1. Base de datos (MySQL)
- Descarga e instala **XAMPP** desde [https://www.apachefriends.org/es/index.html](https://www.apachefriends.org/es/index.html)
- Abre XAMPP y haz clic en los botones **Start** de **Apache** y **MySQL**.
- Da clic en **Admin** en MySQL para abrir **phpMyAdmin**.
- Crea una base de datos llamada `api_messages_seti`.
- Importa el script SQL ubicado en la carpeta `backup-db` del proyecto si existe.

### 2. Backend con Flask
- Asegúrate de tener **Python 3.10 o superior** instalado.
- Crea y activa un entorno virtual:

  ```bash
  python -m venv venv
  venv\Scripts\activate  # En Windows
  source venv/bin/activate  # En Linux/Mac




pip install -r requirements.txt

python app.py

las pruebas test se encuentran en la carpeta pruebas

Uso
Accede a http://localhost:5000/api/messages para usar la API.

Para rutas protegidas, primero realiza login para obtener un token JWT.

Agrega el token en el encabezado Authorization como:
Authorization: Bearer tu_token_jwt

Puedes probar los endpoints fácilmente con Postman o alguna herramienta similar.
aca esta la documentación del api en swagger: http://localhost:5000/api-docs



# API REST con Flask para gestión de mensajes con autenticación JWT
-Api Restfull para procesar mensajes de plataforma de chat , procesamiento , validación de mensajes, y autenticacion JWT
## 🚀 Instalación

### 1. Base de datos (MySQL)
Eh configurado una base de datos mysql(pruebas) en aws Ec2, para simplicidad de no tener que instalar nada sino solo ejecutar el proyecto.
El proyecto tiene en el archivo config.py configurada la conexion a mysql en aws asi que no 
se debe intalar mysql ni servidores esta es la conexion que alli tengo:
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Pru3b4setic2025**@18.216.244.41/api_messages_seti'
SQLALCHEMY_TRACK_MODIFICATIONS = False

la url para ver visualmente la base de datos con las tablas e insersiones(gestor de base de datos phpmyadmin):
http://18.216.244.41/phpmyadmin/index.php
usuario: root
pass: Pru3b4setic2025**

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



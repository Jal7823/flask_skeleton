# 🐍 Crear Proyecto Flask

Este script permite crear un esqueleto básico para un proyecto Flask con la estructura de carpetas necesaria y configuraciones iniciales.

## 📋 Requisitos

- Python 3.x
- Virtualenv
- Flask
- Flask-RESTx
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Loginw
- python-dotenv

## 🚀 Instalación

1. **Clona este repositorio** o descarga el script.
2. **Ejecuta el script** en tu terminal:
   ```bash
   python crear_proyecto.py
   ```
3. **Sigue las instrucciones** en la consola para ingresar el nombre del proyecto.

## 🗂 Estructura del Proyecto

El script creará la siguiente estructura de carpetas:

```
nombre_proyecto/
│
├── src/
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── utils/
│   ├── static/
│   │   ├── js/
│   │   ├── img/
│   │   ├── css/
│   │   └── libs/
│   ├── index.py
│   └── app.py
│
└── env/  # Entorno virtual
```

## 📄 Archivos Generados

- **index.py**: Archivo principal para ejecutar la aplicación Flask.
- **app.py**: Configuración inicial de la aplicación Flask y conexiones a la base de datos.
- **db.py**: Configuración de la base de datos con SQLAlchemy.
- **password_manager.py**: Funciones para gestionar contraseñas.
- **ma.py**: Configuración de Marshmallow para serialización.

## ⚙️ Uso

1. Una vez creado el proyecto, navega a la carpeta del proyecto:
   ```bash
   cd nombre_proyecto
   ```
2. Activa el entorno virtual:
   ```bash
   source env/bin/activate
   ```
3. Instala las dependencias requeridas:
   ```bash
   pip install -r requirements.txt
   ```
4. Abre el proyecto en Visual Studio Code:
   ```bash
   code .
   ```

## 📝 Notas

- Asegúrate de tener PostgreSQL configurado y en ejecución para la conexión de base de datos.
- Modifica las configuraciones según sea necesario en `app.py`.

## 📫 Contacto

Si tienes alguna pregunta, no dudes en contactarme.

# Servicio de Notificaciones - Sistema de Gestión de Empleados

Servicio de notificaciones por correo electrónico desarrollado en Flask

## Tecnologías Utilizadas

- Python 3.8+
- Flask
- Waitress
- SMTPLIB

## Requisitos

- Python 3.8 o superior
- pip
- Cuenta de Gmail o cualquier proveedor bajo SMTP (con contraseña de aplicación)

## Instalación

1. Clona el repositorio:

```bash
git clone <repositorio>
cd notification-service
```

2. Crea y activa el entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno:

```env
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=
```

5. Inicia el servidor:

```bash
waitress-serve --listen=127.0.0.1:5000 app:app
```

## Endpoints

### Envío de Correos

`POST /send-email`

Payload:

```json
{
  "email": "destinatario@email.com",
  "firstName": "Nombre",
  "lastName": "Apellido",
  "position": "Cargo"
}
```

## Estructura del Proyecto

```
├── app.py              # Aplicación principal
├── requirements.txt    # Dependencias
└── .env               # Variables de entorno
```

## Autor

Steven Varela - Desarrollador Senior Python

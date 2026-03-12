# Sarita - Sistema Integral de Turismo

Este es el repositorio del proyecto "Sarita", una plataforma de turismo de triple vía desarrollada con Django (backend) y Next.js (frontend).

## Estado del Proyecto

El proyecto ha sido auditado y estabilizado. Los problemas críticos de arranque han sido solucionados y ambos servidores (backend y frontend) se inician correctamente. La funcionalidad principal de autenticación y la estructura de los módulos ERP están operativas.

## Requisitos

- Python 3.10+
- Node.js 18+
- `pip` y `npm`

## Guía de Inicio Rápido

Siga estos pasos para configurar y ejecutar el entorno de desarrollo local.

### 1. Backend (Django)

**a. Instalar Dependencias de Python:**

Navegue a la raíz del proyecto y ejecute:

```bash
pip install -r backend/requirements.txt
```

**b. Preparar la Base de Datos:**

Una vez instaladas las dependencias, genere y aplique las migraciones de la base de datos:

```bash
python backend/manage.py makemigrations companies api prestadores
python backend/manage.py migrate
```

**c. Crear un Superusuario (Opcional pero Recomendado):**

Para acceder al panel de administración de Django, cree un superusuario:

```bash
python backend/manage.py createsuperuser --username admin --email admin@example.com --noinput
echo "from django.contrib.auth import get_user_model; User = get_user_model(); u = User.objects.get(username='admin'); u.set_password('admin'); u.save()" | python backend/manage.py shell
```
(La contraseña será `admin`).

**d. Ejecutar el Servidor del Backend:**

```bash
python backend/manage.py runserver
```

El servidor del backend estará disponible en `http://127.0.0.1:8000`.

### 2. Frontend (Next.js)

**a. Instalar Dependencias de Node.js:**

En una nueva terminal, navegue al directorio del frontend e instale las dependencias:

```bash
cd frontend
npm install
```

**b. Ejecutar el Servidor de Desarrollo del Frontend:**

Una vez instaladas las dependencias, inicie el servidor de desarrollo:

```bash
npm run dev
```

El servidor del frontend estará disponible en `http://localhost:3000`.

---

Una vez completados estos pasos, la aplicación Sarita estará completamente funcional en su entorno local.

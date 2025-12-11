## Paso 1: Petición de Login\n\n```bash
curl -X POST -H "Content-Type: application/json" -d '{"email": "empresario@example.com", "password": "password123"}' http://127.0.0.1:8000/api/auth/login/
```\n\n## Respuesta de Login\n\n```json
{"key":"8a2ef08d874ab1cc0fe3e8cfaf4ce95326495ed2","user":{"pk":1,"username":"empresario","email":"empresario@example.com","role":"PRESTADOR","profile":null}}```
\n\n**Token extraído:** 8a2ef08d874ab1cc0fe3e8cfaf4ce95326495ed2
\n\n## Paso 2: Petición de Perfil\n\n```bash
curl -H "Authorization: Token 8a2ef08d874ab1cc0fe3e8cfaf4ce95326495ed2" http://127.0.0.1:8000/api/v1/mi-negocio/operativa/perfil/me/
```\n\n## Respuesta de Perfil\n\n```json
{"detail":"Perfil no encontrado."}```\n\n## Logs del Backend\n\n```
DEBUG: Antes de importar api.signals
DEBUG: Antes de importar api.signals
DEBUG: Después de importar api.signals
DEBUG: Después de importar api.signals
Performing system checks...

December 10, 2025 - 15:36:00
Django version 5.2.6, using settings 'puerto_gaitan_turismo.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
DEBUG: Antes de importar api.signals
DEBUG: Antes de importar api.signals
DEBUG: Después de importar api.signals
DEBUG: Después de importar api.signals
/home/jules/.pyenv/versions/3.12.12/lib/python3.12/site-packages/dj_rest_auth/registration/serializers.py:228: UserWarning: app_settings.USERNAME_REQUIRED is deprecated, use: app_settings.SIGNUP_FIELDS['username']['required']
  required=allauth_account_settings.USERNAME_REQUIRED,
/home/jules/.pyenv/versions/3.12.12/lib/python3.12/site-packages/dj_rest_auth/registration/serializers.py:230: UserWarning: app_settings.EMAIL_REQUIRED is deprecated, use: app_settings.SIGNUP_FIELDS['email']['required']
  email = serializers.EmailField(required=allauth_account_settings.EMAIL_REQUIRED)
/home/jules/.pyenv/versions/3.12.12/lib/python3.12/site-packages/dj_rest_auth/registration/serializers.py:288: UserWarning: app_settings.EMAIL_REQUIRED is deprecated, use: app_settings.SIGNUP_FIELDS['email']['required']
  email = serializers.EmailField(required=allauth_account_settings.EMAIL_REQUIRED)
System check identified some issues:

WARNINGS:
?: (account.W001) ACCOUNT_LOGIN_METHODS conflicts with ACCOUNT_SIGNUP_FIELDS
?: (staticfiles.W004) The directory '/app/backend/static' in the STATICFILES_DIRS setting does not exist.

System check identified 2 issues (0 silenced).
/home/jules/.pyenv/versions/3.12.12/lib/python3.12/site-packages/dj_rest_auth/serializers.py:62: UserWarning: app_settings.AUTHENTICATION_METHOD is deprecated, use: app_settings.LOGIN_METHODS
  if allauth_account_settings.AUTHENTICATION_METHOD == allauth_account_settings.AuthenticationMethod.EMAIL:
[10/Dec/2025 16:35:06] "POST /api/auth/login/ HTTP/1.1" 200 157
[10/Dec/2025 16:35:07] "POST /api/auth/login/ HTTP/1.1" 200 157
[10/Dec/2025 16:35:50] "GET /api/v1/mi-negocio/operativa/perfil/me/ HTTP/1.1" 404 34
```

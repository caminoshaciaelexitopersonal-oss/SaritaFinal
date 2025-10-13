# Estructura de Roles y Permisos en SARITA

## 1. Roles de Usuario

El sistema SARITA define un conjunto de roles jerárquicos diseñados para delegar responsabilidades y asegurar el acceso controlado a las diferentes funcionalidades de la plataforma.

| Rol                          | Descripción                                                                                                  | Herencia de Permisos                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| **Administrador General**    | Superusuario con acceso total al sistema. Gestiona configuraciones globales, usuarios y todas las dependencias. | -                                                    |
| **Administrador de Dependencia** | Rol asignado a un `FUNCIONARIO_DIRECTIVO` que tiene permisos de gestión sobre una dependencia específica.     | `Funcionario Directivo`                              |
| **Funcionario Directivo**    | Personal de alto nivel. Aprueba contenido, gestiona usuarios de menor nivel y supervisa la dependencia.        | `Funcionario Profesional`                            |
| **Funcionario Profesional**  | Personal que crea y gestiona contenido (publicaciones, atractivos), pero requiere aprobación para publicar.    | `Funcionario Técnico`                                |
| **Funcionario Técnico**      | Personal con permisos básicos, principalmente para tareas de verificación y soporte.                             | `Turista` (con acceso al panel de administración)    |
| **Prestador de Servicios**   | Dueño de un negocio turístico. Gestiona su propio perfil, servicios y galería de imágenes.                     | -                                                    |
| **Artesano**                 | Artesano local que gestiona su propio perfil, productos y galería.                                           | -                                                    |
| **Turista**                  | Usuario público registrado. Puede guardar favoritos, escribir reseñas y interactuar con la plataforma.         | -                                                    |

## 2. Jerarquía de Agentes

El sistema de agentes sigue una estructura jerárquica que refleja la organización administrativa, permitiendo una supervisión y coordinación eficientes.

```
+--------------------------+
|     SaritaNacionGeneral  | (Controla toda la red)
+------------+-------------+
             |
             | Supervisa
             v
+--------------------------+
| SaritaDepartamentoGeneral| (Uno por cada dependencia)
+------------+-------------+
             |
             | Delega Tareas
             v
+--------------------------+
|     TurismoCoronel       | (Agente especializado en turismo)
+--------------------------+
```

-   **SaritaNacionGeneral:** El agente central que recibe todos los comandos iniciales. Delega las tareas a los agentes de departamento correspondientes.
-   **SaritaDepartamentoGeneral:** Gestiona las tareas dentro de una dependencia (ej. Secretaría de Turismo de un departamento).
-   **TurismoCoronel:** Ejecuta tareas específicas relacionadas con el turismo, como buscar información sobre atractivos, generar descripciones, etc.

## 3. Matriz de Permisos (Simplificada)

| Acción                                       | Admin | Func. Directivo | Func. Profesional | Func. Técnico | Prestador/Artesano | Turista |
| -------------------------------------------- | :---: | :-------------: | :---------------: | :-----------: | :----------------: | :-----: |
| **Gestión de Usuarios**                      |       |                 |                   |               |                    |         |
| - Crear/Editar/Eliminar cualquier usuario    |   ✅   |        ❌        |         ❌         |       ❌       |         ❌          |    ❌    |
| - Crear/Editar/Eliminar usuarios de menor rol|   ✅   |        ✅        |         ❌         |       ❌       |         ❌          |    ❌    |
| **Gestión de Contenido**                     |       |                 |                   |               |                    |         |
| - Crear/Editar contenido                     |   ✅   |        ✅        |         ✅         |       ❌       |         ✅ (propio)   |    ❌    |
| - Aprobar/Publicar contenido                 |   ✅   |        ✅        |         ❌         |       ❌       |         ❌          |    ❌    |
| **Configuración del Sitio**                  |   ✅   |        ❌        |         ❌         |       ❌       |         ❌          |    ❌    |
| **Escribir Reseñas**                         |   ✅   |        ✅        |         ✅         |       ✅       |         ✅          |    ✅    |
| **Guardar Favoritos**                        |   ✅   |        ✅        |         ✅         |       ✅       |         ✅          |    ✅    |
| **Interactuar con Agentes**                  |   ✅   |        ✅        |         ✅         |       ✅       |         ✅          |    ✅    |
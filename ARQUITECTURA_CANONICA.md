# Diseño de Arquitectura Canónica y Grafo de Dependencias
... (secciones 1, 2 y 3 sin cambios) ...

---

## 4. Orden Canónico Teórico de Migraciones

Una vez que los modelos hayan sido refactorizados para eliminar las dependencias cruzadas según las estrategias de la sección 3, el siguiente procedimiento de "hard reset" garantizará una reconstrucción limpia y consistente de la base de datos.

### **Paso 1: Preparación del Entorno**

1.  Verificar que el archivo `db.sqlite3` (o la base de datos correspondiente) ha sido eliminado.
2.  Verificar que **todos** los directorios `migrations/` dentro de las apps del proyecto han sido eliminados.

### **Paso 2: Generación de Migraciones (`makemigrations`)**

El comando `makemigrations` debe ejecutarse en el orden de las capas, desde la más baja a la más alta.

1.  **Capa 1 (Núcleo):**
    ```bash
    python backend/manage.py makemigrations companies api
    ```
    *(Estas pueden generarse juntas ya que no dependen entre sí, solo de la Capa 0)*

2.  **Capa 2 (Sistemas Base):**
    ```bash
    python backend/manage.py makemigrations prestadores gestion_contable
    ```
    *(Se pueden generar juntas, ya que ambas dependen solo de la Capa 1)*

3.  **Capa 3 (Sistemas Derivados y Subdominios):**
    ```bash
    python backend/manage.py makemigrations gestion_financiera gestion_comercial nomina empresa ...
    ```
    *(Todas las apps restantes que dependen de las capas inferiores)*

4.  **Capa 4 (Servicios Transversales):**
    ```bash
    python backend/manage.py makemigrations gestion_archivistica audit
    ```
    *(Al no tener `ForeignKey` a otros módulos, estas pueden generarse en cualquier momento, pero por orden lógico se dejan al final.)*

**Alternativa Simplificada:** Si el desacoplamiento es exitoso, un único comando debería ser suficiente para resolver el árbol correctamente:
```bash
python backend/manage.py makemigrations
```

### **Paso 3: Aplicación de Migraciones (`migrate`)**

De manera similar, el comando `migrate` debe respetar el orden de dependencia.

1.  **Capa 1:**
    ```bash
    python backend/manage.py migrate companies
    python backend/manage.py migrate api
    ```

2.  **Resto de las Capas:** Una vez que las capas base están migradas, un `migrate` general debería resolver el resto.
    ```bash
    python backend/manage.py migrate
    ```

Este procedimiento teórico, basado en una arquitectura desacoplada, elimina la ambigüedad y previene los errores de `NodeNotFoundError`.

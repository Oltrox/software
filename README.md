# Ingeniería de Software
### Lecciones de GIT

* [Link a la playlist de YouTube](https://www.youtube.com/watch?v=hWglK8nWh60&list=PLPl81lqbj-4I8i-x2b5_MG58tZfgKmJls)

### Lecciones de FLASK

- ✔️ Lección 1: La primera aplicación Flask                
- ✔️ Lección 2: Uso de plantillas para las páginas HTML
- ✔️ Lección 3: Uso de formularios en Flask
- ✔️ Lección 4: Login de usuarios en Flask
- ✔️ Lección 5: Añadiendo una base de datos: SQLAlchemy
- ✔️ Lección 6: Estructura de un proyecto con Flask. Blueprints
- ✔️ Lección 7: Parámetros de configuración de un proyecto Flask
- ✔️ Lección 8: Gestión y manejo de errores y excepciones
- ❌ Lección 9: Logs en Flask
- 👁‍🗨 Lección 10: Añadiendo seguridad en las vistas
- ❌ Lección 11: Actualizar la base de datos SQLAlchemy
- ❌ Lección 12: Test con Flask
- ✔️ Lección 13: Paginar las consultas de base de datos
- ❌ Lección 14: Enviar emails con Flask
- ✔️ Lección 15: Trabajar con Fechas en Flask
- ✔️ Lección 16: Procesar ficheros en Flask
- ❌ Lección 17: Desplegar una aplicación Flask en producción con Nginx + Gunicorn

> Para la Lección 16 no es necesario hacer lo de la migración, pues se borra la base de datos y ya

### Arreglar llaves de GIT

1. Identificar la carpeta donde esta la llave. Abrir GIT BASH y buscar la carpeta (en mi caso estan en /d/Proyectos/software/ y se llama id_rsa_software) y utilizar:

        cp /d/Proyectos/software/id_rsa_sofware ~/.ssh/id_rsa_software

2. Luego crear un archivo llamado config y colocar lo siguiente:

        touch ~/.ssh/config
        chmod 600 ~/.ssh/config

3. Abrir con nano el archivo:

        nano ~/.ssh/config

4. Modificar el archivo config de esta forma (en lugar de Oltrox colocar el usuario que utilizan ustedes):

        Host github.com
            User Oltrox
            IdentityFile ~/.ssh/id_rsa_software

5. Guardar y salir de nano:

        CTRL + O y luego ENTER  ->  GUARDAR
        CTRL + X                ->  SALIR

6. De aqui en adelante ya se puede utilizar el repositorio desde GIT BASH sin necesidad de agregar las llaves.
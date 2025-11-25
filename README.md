# To-Do-List
Aplicación web de gestión de tareas desarrollada con **Django**.
Permite a cada usuario registrarse, iniciar sesión y administrar sus propias tareas del día a día.

---

## Características

- Registro e inicio de sesión de usuarios.
- Cada tarea pertenece a un usuario: nadie puede ver/editar/borrar tareas de otros.
- CRUD completo de tareas:
  - Crear nueva tarea
  - Listar tareas
  - Ver detalles
  - Editar
  - Eliminar
- Campos de cada tarea:
  - Título
  - Descripción
  - Estado: Pendiente / En progreso / Completada
  - Prioridad: Baja / Media / Alta
  - Fecha (vencimiento o día objetivo)
  - Categoria

---

## Tecnologías utilizadas

- Python 3
- Django 5
- HTML5 / CSS3
- Sistema de autenticación de Django (`django.contrib.auth`)
- Plantillas de Django (template engine)

---

## Como utilizarlo

1. Clonar el repositorio:

```bash

   git clone https://github.com/giova77/To-Do-List.git
   cd To-Do-List/todo_app
    
   python -m venv venv
   source venv/bin/activate 
 ```

2. Instalar las dependencias:
```bash
    pip install -r requirements.txt
 ```

3. Aplicar las migraciones
```bash
   python manage.py migrate
```


4. Ejecutarlo
```bash
    python manage.py runserver
```



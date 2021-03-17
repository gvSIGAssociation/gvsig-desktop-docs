{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Configuracion modelo {% endcomment %}

(**en contruccion**)
 
Configurar un modelo de datos en *VCSGis* requiere cierto análisis y organización. No esta pensado 
para crearse sin una planificación previa. Antes de añadir las tablas que forman el modelo se deben tener 
bien claras y declaradas las relaciones entre ellas, así como las restricciones que se buscan aplicar a 
los atributos de estas. Adicionalmente, también hy que declarar como se deben presentar los datos de las 
distintas tablas al usuario, normalmente en forma de *formularios*. 

Para realizar toda esta tarea hay que apoyarse en las herramientas de gvSIG desktop de *Crear nueva tabla o capa*
y el *Gestor de columnas*. Una vez declarada la información que define el modelo de datos, es posible añadir
las tablas que lo componen al repositorio de la herramienta de control de versiones *VCSGis*.

Ahora solo queda indicar a *VCSGis* que tablas de las que hay en el repositorio forman parte de un
modelo de datos. Para ello se necesita disponer de acceso de escritura a la base de datos en la
que reside el repositorio donde estan las tablas que forman el modelo. Cargaremos en el proyecto
de *gvSIG desktop* la tabla *PUBLIC.VCSGISREPO_ENTITIES* y, bien directamente sobre la tabla o en el formulario 
asociado a ella, indicaremos para cada "entidad" a que modelo de datos pertenece.

Para abrir la tabla *PUBLIC.VCSGISREPO_ENTITIES* hay que realizarlo desde el *Gestor de proyectos* situado en 
el menú *Mostrar* de *gvSIG Desktop*. El proceso de abrir una tabla es el genérico a abrir cualquier archivo, 
primero se selecciona *Tabla* como tipo de datos a abrir, se selecciona la opción de *Nuevo*, lo que habilita una 
ventana donde se tiene que seleccionar la pestaña *Base de datos*. Esa pestaña muestra en su zona superior
un desplegable donde hay que especificar la base de datos donde se encuentra la tabla. 
Una vez seleccionada la base de datos, en la lista de tablas de esta hay que marcar la tabla 
en cuestión y pulsa el botón *Aceptar*.

>
> Aqui ejemplo
> 
> Preparar ejemplo con tablas de continentes y paises (y alguna lista de valores). 
> Tener las dos tablas en CVS junto a la documentacion para poder descargarlas y probarlo.
>

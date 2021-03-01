{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Añadir capa VCSGis usando el diálogo "Añadir Capa" de gvSIG Desktop {% endcomment %} 


Una vez en la ventana de añadir capa existen 2 maneras de proceder para cargar un capa/tabla con control de versiones VCSGis;
 * Seleccionar la capa como si fuera un archivo de base de datos genérico utilizando la conexión a la base de datos asociada a la *Copia de trabajo*.
 * Utilizar la pestaña VCSGis que permite cargar de manera automática este tipo de archivos con control de versiones. Opción más lógica.

A continuación, se muestra el aspecto de dicha ventana al seleccionar la pestaña *VCSGis* y cargar una capa la cual ya estaba en local pero que fue eliminada de la vista.

![añadirCapaVCSGis1](img/55_load_capa_prexistente_copia_tra.png)

Como se puede apreciar hay que identificar la copia de trabajo y tras eso seleccionar ( marcar el check) en el área de elección de tablas la tabla/capa en cuestión. A parte de lo anterior, es importante cumplimentar la información de campos de información presentes.

En el caso de que la copia de trabajo nunca halla presentado la capa que se pretende cargar, la ventana muestra un comportamiento diferentes. Ver siguiente ilustración.

![añadirCapaVCSGis2](img/56_load_capa_no_prexistente_copia_tra.png)

Se puede ver que la capa aparece deshabilitada, para poder cargarla hay que seleccionarla, lo cual habilita el icono que obtiene la copia local (checkout). Tras ejecutar dicho proceso al pulsar dicho icono la ventana presenta el mismo aspecto que si la copia local hubiera tenido en algún momento dicha tabla/capa. Solo queda pulsar *Aceptar* para terminar el proceso.

![añadirCapaVCSGis3](img/57_load_capa_no_prexistente_copia_tra_comb.png)



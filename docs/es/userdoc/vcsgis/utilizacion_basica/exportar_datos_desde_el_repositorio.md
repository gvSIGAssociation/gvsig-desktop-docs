{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Exportar datos desde el repositorio {% endcomment %} 

La herramienta de control de versiones VCSGis dispone de la posibilidad de exportar una capa/tabla de la copia de trabajo como un archivo. Este nuevo fichero posee la característica de ser un conjunto de datos normal, es decir, sin control alguno de sus cambios y por tanto de sus revisiones.

Para realizar el proceso anterior se tiene que ejecutar el comando *Exportar* situado en la opción *Herramientas* del menú de gvSIG Desktop, pestaña *VCSGgis*.

![exportar](exportar_datos_desde_el_repositorio_files/40_exportar.png)

Tras la ejecución de comando se presenta la siguiente ventana.

![exportarVentana](exportar_datos_desde_el_repositorio_files/41_exportar_win.png)

El funcionamiento de esta es simple, en primer lugar hay que seleccionar la *Copia de Trabajo* de la cual obtener la capa que se busca exportar. Tras esto aparecerán en la ventana de capas la lista de capas de la copia en cuestión, debiendo seleccionar la deseada. 

Concretado lo anterior solo queda indicar a que fecha se quiere la capa exportada. Para ello disponemos de dos opciones:
 * Fecha de entrada en vigor. Esta opción proporciona una imagen de la cartografía a una determinada fecha indicada por el usuario.
 * Revisión. Con esta opción se descarga la capa/tabla con los cambios presentes hasta la citada revisión. La gestión para la selección de revisión se realiza de igual manera que en apartado anterior.
  
Tras selección de la capa y la "fecha" de la información que queremos exportar de esta solo queda en la ventana una serie de parámetros que permiten la visualización y gestión de esta en las vistas.

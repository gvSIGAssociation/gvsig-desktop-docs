{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Añadir una capa del repositorio {% endcomment %} 


El procedimiento de añadir una capa del repositorio a la copia de trabajo puede llevarse a cabo de dos manera diferentes.

La primera forma, muy similar a *Añadir capa al repositorio*, se realiza ejecutando el comando *Obtener copia local* (checkout) situado en la opción Herramientas  del menú de *gvSIG Desktop*, pestaña *VCSGgis*.

![mostrarCapaRepositorio1](img/28_checkout.png)

Como resultado de la ejecución anterior se obtiene la siguiente ventana:

![mostrarCapaRepositorio2](img/29_checkout_win.png)

En la ventana hay que indicar la copia de trabajo a la que se quiere añadir la capa procedente del repositorio y la capa en cuestión, seleccionando esta de la lista presente. Además de lo anterior, la ventana presenta varias opciones en función si la tabla/capa ya se encuentra en la *Copia de Trabajo*.

Si la Tabla/capa se encuentra ya en la copia en cuestión, se puede utilizar la opción *Sobreescribir tabla*. dicha opción borra la información local de la tabla y vuelve a descarga la tabla desde el repositorio. En el caso de que la tabla nunca haya existido en la copia la opción sobreescribir aparecerá deshabilitada y se podrá cargar esta cumplimentando el resto de parámetros; *No añadir la tabla/capa al proyecto*, *Añadir capa a la vista* y *Añadir la tabla al proyecto*.

Otra cosa a destacar es la posibilidad de cargar la capa en la copia para una determinada revisión, para ello se dispone de un parámetro específico.

Hacer hincapié también en una idea importante, si en el proceso de obtener una copia local, es decir una capa del repositorio no se marca la opción *Añadir capa a la vista*, seleccionando la vista deseada, la capa se almacena en la copia de trabajo pero no se representará en la vista. Llegado a este punto se tendría que cargar la capa mediante mediante el dialogó estandard de *Añadir capa* de gvSIG Desktop.

 La segunda manera de realizar el proceso se realiza con el diálogo genérico de *Añadir capa* de gvSIG Desktop. Esta forma de proceder puede verse en el apartado **Añadir capa VCSGis usando el diálogo "Añadir Capa" de gvSIG Desktop**.



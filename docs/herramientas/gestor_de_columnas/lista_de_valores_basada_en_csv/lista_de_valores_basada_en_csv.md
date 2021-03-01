{% comment %} encoding: utf-8 {% endcomment %}

{% comment %} Como asignar a un campo un lista de valores cerrada basada en los contenidos de un archivo csv {% endcomment %}

Este documento forma parte de la serie que detalla ciertos funcionamientos a configurar con el gestor de columnas de *gvSIG Desktop*. Concretamente este documento detalla el procedimiento de importar un archivo en formato *csv* de una tabla, la cual posteriormente presentará relación con otras mediante configuración con el gesto de columnas.

Como ejemplo en este documento se va a abrir un archivo con extensión *csv* con la información de los modelos de las señales verticales y la *tabla vertical_signal*, la cual forma parte de una base de datos.

En primer lugar hay que abrir las tablas. Lo anterior se realiza desde el ***Gestor de proyectos*** situado en el ***menú Mostrar*** de *gvSIG Desktop*. El proceso de abrirlas es el genérico a abrir cualquier archivo, primero se selecciona ***Tabla*** como tipo de datos a  abrir, se selecciona la opción de ***Nuevo***. La ejecución de lo anterior  habilita una ventana donde en pestañas se enumeran las diferentes formas de introducir tablas en el software. 

![1_newTable_128](lista_de_valores_basada_en_csv_files/1_newTable_128.png)

Para empezar se selecciona la ***pestaña Archivo*** y tras pulsar el ***botón Añadir***, se despliega un cuadro de diálogo donde se selecciona el fichero *csv* en cuestión. Una vez seleccionada se pulsa el *botón Aceptar* cerrando la ventana anterior y rellenando el panel de la pestaña archivo del ***cuadro de diálogo Nueva capa***.

![2_newTableFileAdd_128](lista_de_valores_basada_en_csv_files/2_newTableFileAdd_128.png)

Tras o anterior hay que configurar la importación del archivo *csv* seleccionando el archivo en el panel y pulsando el ***botón Propiedades*** situado en el margen derecho de la ventana. 

![3_newTableFileProp_128](lista_de_valores_basada_en_csv_files/3_newTableFileProp_128.png)

Este comando despliega la ***ventana Parámetros de carga del csv***, la cual presenta dos pestaña.
* Básica.
* Avanzada.

![4_newTableProperties_128](lista_de_valores_basada_en_csv_files/4_newTableProperties_128.png)

La ***pestaña básica*** se muestra en la siguiente ilustración.

![5_newTableBasicProperties_128](lista_de_valores_basada_en_csv_files/5_newTableBasicProperties_128.png)

En el panel de esta pestaña se muestran 5 componentes, 4 de estos son desplegables y un check o opción, detallados a continuación de descendente.

* **Desplegable archivo**; Detalla la ruta del archivo.
* **Desplegable  perfil**;
* **Desplegable quotePolicy**;
* **Desplegable Idioma.**
* **Opción firstLineHeader**; Identifica si la primera linea del archivo es la cabecera con la información de los campos o no.

La configuración de los parámetros del archivo  utilizado en la realización del ejemplo es la siguiente.

* Desplegable archivo → Propia de cada pc.
* Desplegable  perfil -->
* Desplegable quotePolicy -->
* Desplegable Idioma -->
* Opción firstLineHeader → MARCADA

La otra pestaña del **diálogo Parámetros de carga del csv** es la  ***pestaña de parámetros avanzados*** y se muestra en la siguiente imagen.

![6_newTableAdvancedProperties_128](lista_de_valores_basada_en_csv_files/6_newTableAdvancedProperties_128.png)

El panel de esta pestaña presenta opciones entre las que destacan el nombre del proveedor, en este caso CSV, el separador de registros, delimitador, la posibilidad de detectar campos de manera automática o los campos necesarios para la definición d campos de manera manual, el tipo de codificación…

La configuración de esta pestaña para el caso concreto del ejemplo se muestra en la imagen anterior.

Tras cargar la capa en formato *csv* solo queda repetir lo anterior con la excepción de seleccionar la ***pestaña Base de datos*** en el cuadro de dialogo que se presenta tras pulsar la opción de ***Nuevo***. 

![7_openTableBBDD_128](lista_de_valores_basada_en_csv_files/7_openTableBBDD_128.png)

Esa pestaña muestra en su zona superior un desplegable donde hay que especificar la base de datos donde se encuentra la tabla. Una vez seleccionada la base de datos, en la lista de tablas de esta hay que marcar la tabla en cuestión y pulsa el ***botón Aceptar***.

![8_openTableBBDD_128](lista_de_valores_basada_en_csv_files/8_openTableBBDD_128.png)

A continuación se muestra las dos tablas en cuestión.

![9_tables_128](lista_de_valores_basada_en_csv_files/9_tables_128.png)

El proceso de establecer la relación de las tablas es maestro – detalle y queda detallado en el documento [Como establecer una relacion maestro detalle entre dos tablas.](https://github.com/gvSIGAssociation/gvsig-desktop-docs-es/blob/master/docs/herramientas/gestor_de_columnas/maestro_detalle/maestro_detalle.md)


{% comment %} encoding: utf-8 {% endcomment %}

{% comment %} Como establecer lista de valores cerrada basada en los contenidos de una tabla {% endcomment %}

Este documento define el procedimiento de creación de una nueva tabla de valores, los cuales son las opciones para los campos de otras. En otras palabras, en este documento se detalla la forma de crear diccionarios o tablas de datos desde cero con las diferentes opciones que presentan determinados campos de otras capas.

Para realizar la explicación se utilizara como ejemplo la creación de la *tabla materiales*. Esta tabla con dos elementos unicamente almacena el tipo de material del que están construidas las placas de las señales presentes en la *tabla vertical_signal*.

El proceso comienza tras iniciar *gvSIG Desktop* ejecutando en la ***pestaña Vista*** el comando ***new layer***.

![New_layer](lista_de_valores_basada_en_tabla_files/1_new_layer.png)

Como resultado de lo anterior se obtiene la siguiente ventana que nos permite seleccionar la creación de una ***nueva capa Shape*** o una ***nueva tabla de un base de datos (using JDBC)***. Seleccionando esta última opción de entre los dos.

![New_layer_win_1](lista_de_valores_basada_en_tabla_files/2_new_layer_win_1.png)

Se pulsa el botón ***Siguiente*** situado en la zona inferior de la ventana para continuar el proceso. 

La siguiente ventana esta destinado a evitar problemas a la hora de definir el nombre de la taba así como los campos que la componen. Con esta ventana se asegura que los nombres de los campos estén en minúsculas, presenten guión bajo (“_”) en vez de espacios y guiones (“-”).

![New_layer_win_2](lista_de_valores_basada_en_tabla_files/3_new_layer_win_2.png)

Se seleccionan las tres opciones y se pulsa el botón ***Siguiente*** situado en la zona inferior de la ventana para continuar el proceso. 

En esta ventana hay que especificar la base de datos donde se va a almacenar la nueva tabla. Hay que decir que la base de datos tiene que estar creada de antemano. El proceso de selección se basa en identificar la base de datos en el primer desplegable o especificar un nombre, tipo de conector y fichero en los desplegables Nombre de conexión, Conector y Fichero respectivamente si la base de datos no se encuentra.

En el caso del ejemplo, se dispone de una base de datos llamada *crearCapa*. 

![New_layer_win_3](lista_de_valores_basada_en_tabla_files/4_new_layer_win_3.png)

Se pulsa el botón ***Siguiente*** situado en la zona inferior de la ventana para continuar el proceso.

La siguiente ventana define el esquema de la base de datos donde se quiere almacenar la tabla y el nombre de esta.

Se especifica el esquema PUBLIC y como nombre de *tabla materiales*. Tras esto, se pulsa el botón ***Siguiente*** situado en la zona inferior de la ventana para continuar el proceso. 

![New_layer_win_4](lista_de_valores_basada_en_tabla_files/5_new_layer_win_4.png)

En la siguiente ventana se detalla los campos o columnas de la tabla. Sin duda es la ventana más importante a la hora de la creación de la tabla ya que define el esquema de datos de esta.

![New_layer_win_5](lista_de_valores_basada_en_tabla_files/6_new_layer_win_5.png)

El proceso se inicia con la creación de un nuevo campo. Para realizar esto hay que pulsar el botón ***Nuevo*** situado en el margen derecho de la ventana.

![New_layer_win_6](lista_de_valores_basada_en_tabla_files/7_new_layer_win_6.png)

Como resultado de la ejecución y tal y como se muestra en la imagen anterior se crea un campo por defecto llamado *Campo1*, de tipo *String*, *tamaño 50*, *tipo de relación igual a ninguno*….

Tras la creación de este, se ha puesto la capa en edición de manera automática y se permite cambiar los parámetros que lo definen. De modo que, siguiendo el ejemplo, el nuevo campo tiene que llamarse *name*, ser de tipo *String*.

Todos los valores anteriores pueden detallarse en la ***pestaña Campos básicos***. Concretamente el nombre name se puede definir en la ***barra de texto Nombre de campo***, el tipo de campo se detalla en el **desplegable Tipo de Campo o el icono adyacente*** a este que ofrece una mayor colección de tipo de datos. 

Tras modificar lo anterior aceptamos guardar los cambios sobre el campo name pulsando el botón ***Aceptar*** del margen derecho, lo cual hace que este presente los parámetros correctos en la lista de campos del Gestor de columnas.

A parte de ese campo name se crea otro de iguales características llamado *value*. El resultado final de la ventana es el siguiente.

![New_layer_win_7](lista_de_valores_basada_en_tabla_files/8_new_layer_win_7.png)

Se pulsa el botón ***Siguiente*** situado en la zona inferior de la ventana para continuar el proceso.

En esta ventana se especifica si se desea crear un índice espacial que optimice los cálculos en caso de que la tabla presente geometrías. 

![New_layer_win_8](lista_de_valores_basada_en_tabla_files/9_new_layer_win_8.png)

En el caso del ejemplo, como no se dispone de geometría se pulsa el botón ***Siguiente*** para continuar con el proceso.

La siguiente ventana configura los permiso de la tabla.

![New_layer_win_9](lista_de_valores_basada_en_tabla_files/10_new_layer_win_9.png)

En el caso del ejemplo se pulsa el botón ***Siguiente*** para continuar con el proceso.

En esta ventana se especifican las secuencias a realizar después de la creación de la tabla.

![New_layer_win_10](lista_de_valores_basada_en_tabla_files/11_new_layer_win_10.png)

En el caso del ejemplo se pulsa el botón ***Siguiente*** para continuar con el proceso ya que no queremos ejecutar sentencia alguna.

En esta última ventana termina el proceso de creación y se indica si se desea añadir la tabla a la vista.

![New_layer_win_11](lista_de_valores_basada_en_tabla_files/12_new_layer_win_11.png)

En el caso del ejemplo se desmarca añadirla a la vista puesto que la capa no posee geometrías y se pulsa el botón ***Terminar*** para finalizar con el proceso. En el cao de que la tabla presente geometrías puede optarse por cargar en la vista.

El siguiente paso lógico es tras la creación de la tabla materiales es rellenar esta con la lista de valores. Para realizar lo anterior, en primer lugar hay que abrirla. Para abrir la tabla hay que realizarlo desde el ***Gestor de proyectos*** situado en la ***pestaña Mostrar*** de *gvSIG Desktop*. 

El proceso de abrir una tabla es el genérico a abrir cualquier archivo, primero se selecciona Tabla como tipo de datos a abrir, se selecciona la opción de ***Nuevo***, lo que habilita una ventana donde se tiene que seleccionar la opción ***Base de datos***. Esa pestaña muestra en su zona superior un desplegable donde hay que especificar la base de datos donde se encuentra la tabla. Una vez seleccionada la base de datos, en la lista de tablas de esta hay que marcar la tabla en cuestión y pulsa el botón ***Aceptar***. 

![Abrir_tabla](lista_de_valores_basada_en_tabla_files/13_abrir_tabla.png)

Tras la selección de este la tabla se muestra en una ventana del software. La siguiente ilustración muestra la *tabla materiales* con las que se va a realizar el proceso, actualmente vacía.

![Materiales_vacia](lista_de_valores_basada_en_tabla_files/14_materiales_vacia.png)

Una vez abierta se pone en edición ejecutando en la ***pestaña Tabla*** de *gvSIG Desktop* el comando ***Iniciar edición***.

![Iniciar_edicion](lista_de_valores_basada_en_tabla_files/15_iniciar_edicion.png)

El proceso de añadir elementos a la tabla se realiza mediante ejecución del comando ***Añadir fila*** adyacente al anterior, situado en  la ***pestaña Tabla*** de *gvSIG Desktop*.

![Añadir_fila](lista_de_valores_basada_en_tabla_files/16_añadir_fila.png)

Tras esto en la tabla materiales aparece una fila en blanco donde se introducen los valores del nombre y el valor del material en cuestión para el caso del ejemplo.

Los materiales que presentan las placas de las señales verticales de la tabla vertical_signal son los siguientes;

* name: *Acero*, value: *STEEL*
* name: *Aluminio*,  value: *ALUMINUM*

De modo que tras introducirlos la tabla materiales presenta la siguiente forma.

![Materiales](lista_de_valores_basada_en_tabla_files/17_materiales.png)

Solo queda ahora finalizar edición ejecutando el comando ***Detener edición*** situado en la ***pestaña Tabla*** de *gvSIG Desktop* y guardar los cambios de la tabla.

![Detener_edicion](lista_de_valores_basada_en_tabla_files/18_detener_edicion.png)

Una vez creada la tabla en cuestión solo queda establecer la relación entre la tablas que la utilicen lay esta. Para ello hay que realizar el procedimiento especificado en el documento [Como establecer una relacion maestro detalle entre dos tablas.](https://github.com/gvSIGAssociation/gvsig-desktop-docs-es/blob/master/docs/herramientas/gestor_de_columnas/maestro_detalle/maestro_detalle.md)

A modo de ejemplo y siguiendo con el uso de la tabla de materiales vamos a establecer la relación entre la *tabla vertical_signal* y la *tabla o diccionario materiales*. Esta relación es uno a uno ya que una señal solo puede ser de un material. A continuación se muestran las dos tablas obtenidas con el *Gestor de proyectos*.

![Tablas](lista_de_valores_basada_en_tabla_files/19_tablas.png)

Para configurar la relación hay que obtener el gestor de la tabla vertical_signal  por lo que hay seleccionar la tabla en cuestión y ejecutar el comando ***Gestor de columnas*** situado en la pestaña ***Tabla** de *gvSIG Desktop* siempre y cuando la tabla este abierta. 

![Gestor_columnas](lista_de_valores_basada_en_tabla_files/20_gestor_columnas.png)

Como resultado se obtiene el siguiente gestor, *gestor de columnas* de la *tabla vertical_signal*.

![Gestor_columnas_win](lista_de_valores_basada_en_tabla_files/21_gestor_columnas_win.png)

Esta herramienta permite al usuario definir la estructura de datos de la tabla, así como su representación o visualización. La realización de los cambios se lleva a cabo por columnas y permite modificar estas, crear otras nuevas e incluso eliminarlas si es necesario.

Como se busca definir una relación entre las dos tablas hay que buscar el campo que la establece, en este caso *verticalsignalmateriales*. Para establecer la relación hay que seleccionar en el *gestor de columnas* de la *tabla vertical_signal* el campo que establece la relación, campo *verticalsignalmateriales*.

![GC_material_1](lista_de_valores_basada_en_tabla_files/22_GC_material_1.png)

Una vez seleccionado se inicia su edición pulsando el botón ***Modificar*** situado en la zona derecha de la ventana.

![GC_material_2](lista_de_valores_basada_en_tabla_files/23_GC_material_2.png)

Tras lo anterior se habilitan una serie de pestañas que permiten modificar todo lo referentes a los datos y su representación del citado campo. Para establecer la relación hay que modificar el contenido de dos pestañas, la ***pestaña Campos básicos*** y la ***pestaña Clave ajena***.

![GC_material_3](lista_de_valores_basada_en_tabla_files/24_GC_material_3.png)

La configuración comienza especificando en la ***pestaña Campos básicos***.
En este caso concreto de establecer relación entre tablas uno a uno del ejemplo, se pasa de no tener relación alguna a *Colaboración (1:1)* ya que como se detalla en el ejemplo una señal solo puede estar compuesta de un material

 Tras lo anterior se inicia la configuración de la **pestaña Clave ajena**, seleccionando en primer lugar si el campo es *clave ajena*, el cual lo es en el caso del ejemplo, tras esto hay definir si dicho campo es *clave ajena de una lista cerrada o no*. En el caso de ejemplo, la *tabla materiales* es una tabla cerrada por lo que hay que especificarlo.

 > La única diferencia entre marcar si es una lista cerrada o no es la representación de los valores de esta en el formulario de la tabla de la clave ajena, en este caso en el *formulario de vertical_signal*.

Una vez seleccionados o no los elementos anteriores hay que definir la tabla de la cual  el campo es clave ajena, así como el campo que queremos que muestre en el formulario y una formula para la representación o visualización de los datos.

Según el orden de los parámetros definidos en el párrafo anterior la *tabla* sería *materiales*, el campo sería *value* y la *formula especificada* es *name*.

La configuración de las pestañas se puede ver en la siguiente imagen:

![GC_material_4](lista_de_valores_basada_en_tabla_files/25_GC_material_4.png)

Tras lo anterior solo queda terminar la modificación del campo pulsando el botón *Aceptar* del margen derecho y terminar el proceso en el *Gestor de columnas* pulsando el botón *Aceptar* situado en la esquina inferior derecha de dicha ventana.

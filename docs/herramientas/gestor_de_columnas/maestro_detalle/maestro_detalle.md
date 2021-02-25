{% comment %} encoding: utf-8 {% endcomment %}

{% comment %} Como establecer una relacion maestro detalle entre dos tablas {% endcomment %}

Este es el primero de una serie de documentos que permiten definir todo lo referente a las tablas de una base de datos en cuanto a relaciones entre ellas y visualización de su contenido en su correspondientes formularios.

Concretamente en este documento se especifica el proceso de definir relaciones maestro detalle entre dos tablas mediante campos comunes. Estas relaciones pueden ser de uno a uno o de uno a muchos. Para realizar la explicación se utilizaran las tablas de placas y postes ya que una señal solo puede tener un poste, relación uno a uno, y un poste puede tener varias señales o placas, uno a muchos.

RELACIONES UNO A UNO 

Para establecer la relación entre tablas por un campo común, siendo esta una relación de uno a uno, en primer lugar hay que abrir las tabla y el gestor de columnas asociado a estas. Para abrir las tablas hay que realizarlo desde el Gestor de proyectos situado en la pestaña Mostrar de gvSIG Desktop. El proceso de abrirlas es el genérico a abrir cualquier archivo, primero se selecciona Tabla como tipo de datos a  abrir, se selecciona la opción de Nuevo, lo que habilita un gestor de archivos donde se selecciona el fichero en cuestión. Tras la selección de este la tabla se muestra en una ventana del software. La siguiente ilustración muestra las tablas con las que se va a realizar el proceso. 

![Tablas](1_tablas.png)

La tabla bracket o postes tiene un único registro, mientra que la tabla vertical_signal presenta dos registros de dos señales, las cuales se sabe que están en el poste de la tabla anterior. Como este apartado trata las relaciones uno a uno es necesario abrir el gestor de columnas de la tabla que presenta dicha relación, vertical_signal ya que una señal esta asociada solo a un poste.

Para obtener el gestor de esta hay seleccionar la tabla en cuestión y ejecutar el comando Gestor de columnas situado en la pestaña Tabla de gvSIG Desktop siempre y cuando la tabla este abierta. 

![Gestor_columnas](2_gestor_columnas.png)

Como resultado se obtiene el siguiente gestor, gestor de columnas de la tabla vertical_signal.

![Gestor_columnas_vertical_signal](3_gestor_columnas_vertical_signal.png)

Esta herramienta permite al usuario definir la estructura de datos de la tabla, así como su representación o visualización. La realización de los cambios se lleva a cabo por columnas y permite modificar estas, crear otras nuevas e incluso eliminarlas si es necesario.

Como se busca definir una relación entre las dos tablas hay que buscar el campo que la establece, en este caso bracket. Para establecer la relación hay que seleccionar en el gestor de columnas de la tabla vertical_signal el campo que establece la relación, campo bracket.

![GC_vertical_signal_bracket_1](4_GC_vertical_signal_bracket_1.png)

Una vez seleccionado se inicia su edición pulsando el botón Modificar situado en la zona derecha de la ventana.

![GC_vertical_signal_bracket_2](5_GC_vertical_signal_bracket_2.png)
Tras lo anterior se habilitan una serie de pestañas que permiten modificar todo lo referentes a los datos y su representación del citado campo. Para establecer la relación hay que modificar el contenido de dos pestañas, la pestaña Campos básicos y la pestaña Clave ajena.

![GC_vertical_signal_bracket_3](6_GC_vertical_signal_bracket_3.png)

La configuración comienza especificando en la pestaña Campos básicos el tipo de relación que presenta el campo en cuestión. Los tipos de relación presentes en el ultimo desplegable son:
 * Ninguna.
 * Identidad (1:1). Se utiliza para relacionar tablas que hacen referencia a un mismo objeto. Este, sea por el motivo que sea tiene distribuida la información en diferentes tablas.
 * Colaboración (1:1). Se utiliza para relacionar tablas por un campo o columna común. Las tablas representa información de entes diferentes que tiene relación entre si. 
 * Composición (1:n). Se utiliza para establecer relación entre un objeto o elemento de una tabla y varios objetos o elementos de otra, con la salvedad de que el grupo de elementos depende del objeto único. Un ejemplo fácil seria un ticket de la compra, el listado de artículos no tiene sentido si no esta asociado a un ticket.
 * Agregado (1:n).  Se utiliza para establecer relación entre un objeto o elemento de una tabla y varios objetos o elementos de otra. Se diferencia del anterior en que el grupo de elementos puede subsistir sin necesidad del elemento único. 

En este caso concreto de establecer relación entre tablas uno a uno del ejemplo, se pasa de no tener relación alguna a Colaboración (1:1) ya que como se detalla en el ejemplo una señal solo esta en un poste. 

 Tras o anterior se inicia la configuración de la pestaña Clave ajena, seleccionando en primer lugar si el campo es clave ajena, el cual lo es en el caso del ejemplo, tras esto hay definir si dicho campo es clave ajena de una lista cerrada o no. En el caso de ejemplo, la tabla bracket o postes es una tabla en continuo crecimiento por lo que no esta cerrada.

La única diferencia entre marcar si es una lista cerrada o no es la representación de los valores de esta en el formulario de la table de la clave ajena, en este caso en el formulario de vertical_signal.

Una vez seleccionados o no los elementos anteriores hay que definir la tabla de la cual  el campo es clave ajena, así como el campo que queremos que muestre en el formulario y una formula para la representación o visualización de los datos.

Según el orden de los parámetros definidos en el párrafo anterior la tabla sería bracket, el campo sería id y la formula especificada es ‘Poste ‘ || id.

La configuración de las pestañas se puede ver en la siguiente imagen:

![GC_vertical_signal_bracket_4](7_GC_vertical_signal_bracket_4.png)

Tras lo anterior solo queda terminar la modificación del campo pulsando el botón Aceptar del margen derecho y terminar el proceso en el Gestor de columnas pulsando el botón Aceptar situado en la esquina inferior derecha de dicha ventana.

Para ver si los cambios se han realizado con éxito de manera sencilla se puede consultar el formulario de la tabla modificada. Para obtener el formulario de la tabla hay que ejecutar el comando Show form situado en la pestaña Tabla de gvSIG Desktop siempre y cuando la tabla este abierta. 
 
![Show_form](8_show_form.png)

La siguiente ilustración muestra el formulario de la tabla vertical_signal antes de la relación (derecha) y tras la relación (izquierda).

![Form_dif](9_form_dif.png)

Se puede aprecias que el campo bracket del formulario ha sufrido cambios. En el formulario inicial era un campo sin más y en el formulario resultado de las modificaciones del gestor de columnas presenta una serie de componentes que indican que esta ligado a otra tabla. 

![Comp_relacion](10_comp_relacion.png) 

Esos componentes son cuatro de izquierda a derecha:
* Caja de texto con el elemento de la otra tabla seleccionado. En el caso del ejemplo este cumple la expresión indicada anteriormente,  ‘Poste ‘ || id.
* Icono de selección de elemento. Este está deshabilitado si la tabla no se encuentra en edición y permite seleccionar elementos de la tabla ligada.
* Icono borrar elemento relacionado.  Este está deshabilitado si la tabla no se encuentra en edición.
* Icono ver elemento relacionado. Nos permite visualizar el elemento relacionado de la tabla ligada en el formulario de esta.

![Comp_relacion_ver](11_comp_relacion_ver.png)

Realizado todo lo anterior se completa el proceso de ligar una tabla con otra mediante una relación uno a uno mediante un campo común. 

RELACIONES UNO A VARIOS 

Tras completar el apartado anterior y siguiendo el ejemplo de los postes y las señales se deduce que es necesario establecer relaciones entre un elemento y varios de otra tabla, es decir las señales asignadas a un poste. De esta forma tendríamos completamente definida la relación entre las dos tablas en un sentido y otro.

Existen dos casos bien diferenciados a la hora de definir relaciones entre tablas. El primero de estos dos casos se basa en la existencia de campo comunes que las relacionan. Un ejemplo de este es el realizado en el apartado anterior. El segundo caso se da cuando una de las tabla no presenta un campo como tal que indique los elementos de la otra tabla, pero esa otra tabla si lo presenta. Un ejemplo de esto se da en la tabla bracket, la cual no presenta un campo con las señales que dispone, pero la tabla vertical_signal si dispone un campo bracket. Para establecer la relación de señales que presenta un poste por lo tanto se tendrán que crear campos nuevos en la tabla bracket.

El proceso de relacionar las tablas es básicamente el mismo a excepción de la creación de nuevos campos o columnas y se basa en realizar modificaciones sobre el Gestor de columnas de la tabla bracket, postes.

Una vez en el Gestor de columnas de la tabla bracket se inicia el proceso con la creación de un nuevo campo. Para realizar esto hay que pulsar el botón Nuevo situado en el margen derecho de la ventana.

![Nuevo_campo_default](12_nuevo_campo_default.png)
Como resultado de la ejecución y tal y como se muestra en la imagen anterior se crea un campo por defecto llamado Campo1, de tipo String, tamaño 50, tipo de relación igual a ninguno…

Tras la creación de este, se ha puesto la capa en edición de manera automática y se permite cambiar los parámetros que lo definen. De modo que, siguiendo el ejemplo, el nuevo campo tiene que llamarse Señales, ser de tipo lista, presentar un tipo de relación de agregado (1:n) y además ser un campo calculado con la expresión SELECT * FROM vertical_signal WHERE vertical_signal.bracket=id;

Todos los valores anteriores pueden detallarse en la pestaña Campos básicos. Concretamente el nombre Señales se puede definir en la barra de texto Nombre de campo, el tipo de campo se detalla en el desplegable Tipo de Campo o el icono adyacente a este que ofrece una mayor colección de tipo de datos. El tipo de relación se detalla en el ultimo desplegable de la pestaña llamado Tipo de relación. Por último el que sea un campo calculado se especifica seleccionando la opción Campo virtual situada sobre el desplegable anterior y la formula se introduce en el cuadro adyacente a ese check. La formula puede introducirse de manera manual o mediante el evaluador de expresiones.

Como resultado de la creación y modificación del nuevo campo señales, la ventana del Gestor de columnas presenta este aspecto.

![Nuevo_campo_señales](13_nuevo_campo_señales.png)

Tras modificar lo anterior aceptamos guardar los cambios sobre el campo señales lo cual hace que este presente los parámetros correctos en la lista de campos del Gestor de columnas.

![Campo_señales](14_campo_señales.png)

Una vez eso solo queda terminar los procesos en el Gestor de columnas pulsando el botón Aceptar situado en la esquina inferior derecha de dicha ventana.

Para ver si la relación se ha llevado a cabo hay que visualizar la tabla bracket o el formulario asociado a ella. En los dos elementos debe aparecer un nuevo campo llamado Señales relleno con una lista de valores que identifican las señales que presenta dicho poste.

![Form_table_bracket_mal](15_form_table_bracket_mal.png)

De este modo la relación se ha realizado con éxito pero la visualización del grupo de elementos  relacionados no es la deseada. Para mejorar dicha visualización hay que acudir de nuevo al Gestor de columnas de la tabla de postes, bracket, seleccionar la columna Señales e iniciar la edición pulsando Modificar.

En esta ocasión hay que configurar dos pestañas, la pestaña Visualización y la pestaña Etiquetas.

En la pestaña Visualización se especifica la creación de un grupo al cual llamamos Señales.

![GC_bracket_visualizacion](16_GC_bracket_visualizacion.png)

La creación de un grupo hace que el contenido de esa columna pase a ser una pestaña nueva en el formulario, es decir se encuentre aislada del resto de la información.

Con respecto a la configuración de la pestaña Etiquetas se establece la forma con la que se van a representar los elementos de la columna Señales. Para realizar la configuración hay que añadir al cuadro de dicha pestaña la siguiente serie de parámetros mediante el botón Añadir y Actualizar. Esos parámetros son:
 * DAL.RelatedFeatures.Table. Especifica la tabla de donde va obtener los valores a representar para cada elemento de la columna señales.
 * DAL.RelatedFeatures.Unique.Field.Name. Detalla el identificador único de la tabla anterior.
 * DAL.RelatedFeatures.Columns. Columnas de la tabla que guarda información de los elementos de la lista que se van a mostrar para los diferentes elementos de esta que se dan tras la relación. Especificar que el nombre de las columnas tiene que ir separado por dos puntos (‘:’).
 * dynform.resizeweight. Permite ajustar el tamaño de la zona donde se muestran el grupo d e elementos.

En el caso concreto del ejemplo que se esta realizando los valores de los parámetros anteriores son;

 * DAL.RelatedFeatures.Table → vertical_signal
 * DAL.RelatedFeatures.Unique.Field.Name. → id
* DAL.RelatedFeatures.Columns. → id:model:revisiondate
* dynform.resizeweight. → 10

![GC_bracket_etiquetas](17_GC_etiquetas.png)

Una vez terminado lo anterior se termina la edición de la columna pulsando el botón Aceptar del margen derecho y terminar el proceso en el Gestor de columnas pulsando el botón Aceptar situado en la esquina inferior derecha de dicha ventana.

Como resultado de lo anterior podemos ver que el formulario de la tabla de postes, bracket ha cambiado con respecto al anterior.  Tras las anteriores modificaciones realizadas en el Gestor de columnas este ahora presenta en su margen superior una pestaña llamada Señales, la cual almacena  las placas de señales que tiene el poste en cuestión mostrando el identificador, modelo y fecha de revisión de cada señal.

![Form_table_bracket_bien](18_form_table_bracket_bien.png)

Para ver la información de cada señal en su formulario correspondiente solo hay que seleccionarla y pulsar el icono que hay bajo la lista.

![Form_tbracket_vertical_signal_bien ](19_form_bracket_vertical_signal_bien.png)

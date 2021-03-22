{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Consideraciones {% endcomment %} 

> * Que son recursos asociados a una entidad (leyenda, etiquetado, formularios...)
Los recursos son todos aquellos archivos destinados a mejorar la representación gráfica de las
diferentes capas almacenadas en le repositorio. De lo anterior, se deduce que no son solo de un tipo,
sino que presentan diferentes extensiones en función del componente que almacenen. Un ejemplo de
recurso podría ser el archivo que almacena una leyenda, *leyenda.gvsleg*.

A parte de las leyendas, un recurso también podría ser un archivo con la definición del etiquetado 
de la capa, archivos con formularios...

La implementación definida en VCSGis para su utilización favorece que todos los usuarios trabajen
bajo las mismas características de representación favoreciendo aun más la homogeneidad de la 
información aportada por el control de versiones.


> * La configuración de los recursos asociados a una capa es una labor propia del administrador del 
sistema. Esta configuración se aconseja realizarla antes de comenzar a utilizar el sistema de manera
normal por parte de los usuarios. Con lo anterior se garantiza que todos los usuarios ya no solo 
dispongan de una misma información actualizada en todo momento, sino también del modo de representar
esta.

> * Tabla de recursos. Que es. Como asignarla a una capa.
La tabla de recursos es un archivo de tipo tabla constituida por dos campos, *nombre* y *value*.
El campo *nombre* de tipo ```String```, identifica de manera única el recurso y la capa/tabla a la 
cual esta asociada, mientras que el campo *value* de tipo ```byteArray``` almacena el recuso en sí,
es decir el archivo que lo almacena. Para realizar la asignación de esta, previa a su creación y 
actualización con los diferentes recursos, hay que realizar modificaciones en la entidades del 
repositorio de la tabla **PUBLIC.VCSGISREPO_ENTITIES** asignándole a cada una de ellas su recurso, si
sta dispone de el. 

Para facilitar la comprensión del proceso de aignación de recursos a una determinada capa a
continuación se detalla un ejemplo. Este se basa asignar una leyenda de colores a una capa presente
en un repositorio.

> * Ejemplo:
>   * Descripcion del escenario (un repo, un wc, un capa subida).
La capa utilizada para la realización del ejemplo llamada *EDIFICIOS* es un archivo ```shape```
que almacena la geometría de los edificios de la ciudad de Alicante. Esta capa presenta las 
siguientes características;
 * Repositorio: *aytoALC*
 * Copia de trabajo: *usuario1*
 * Categoría: *BASE*
La siguiente ilustración muestra la capa cargada en *gvSIG Desktop*.

![1_EDIFICIOS_128](ejemplo_asignacion_recursos_files/1_EDIFICIOS_128.png)

Tal y como se puede ver, la simbología presenta una leyenda por defecto que no se corresponde 
con la utilizada para esta capa. Para cambiarla y registrarla en el repositorio de modo que siempre
que se utilice dicha capa se presente con la leyenda correcta hay que registrar dicha leyenda 
como recurso.

>   * Asignar a la entidad una tabla de recursos (admin).
En primer lugar hay que crear la tabla de recursos. Dicho proceso  se realiza ejecutando la opción 
**Crear tabla de recursos** situada en el menú **Herramientas**, submenú **VCSGis**, submenú 
**Administración**.

![2_crearTablaRecursos_128](ejemplo_asignacion_recursos_files/2_crearTablaRecursos_128.png)

Realizar lo anterior muestra el siguiente cuadro de diálogo.

![3_crearTablaRecursosWin_128](ejemplo_asignacion_recursos_files/3_crearTablaRecursosWin_128.png)

En la ventana hay que seleccionar en el primer desplegable llamado **Copia de trabajo** la copia 
de trabajo donde esta la capa, *usuario1*.

En el segundo componente hay que detallar el nombre de la tabla de recursos. Se nombra la nueva 
tabla de recursos como *BASE_RECURSOS* ya que se pretende que todos los recursos de la categoría
*BASE* se encuentren en dicha tabla.

 > Hay que especificar que se pueden crear tantas tablas de recursos como se deseen. De modo que
 se puede crear una única tabla de recursos que almacene todos ellos o varias de estas que 
 almacenen los recursos de determinadas categorías de datos por ejemplo.

El proceso de creación finaliza pulsando el botón *Aceptar* en la esquina inferior derecha de 
la ventana.

Una vez creada la tabla hay que subir esta al repositorio. Para hacer lo anterior hay que realizar
un *commit* tras ejecutar la opción *Mostrar cambios** situada en el menú *Herramientas*, submenú 
*VCSGis*.

Tras la correcta definición de la tabla recursos hay que asignar a la capa *EDIFICIOS* del 
repositorio dicha tabla, para ello hay que abrir la tabla *PUBLIC.VCSGISREPO_ENTITIES* situada 
en el repositorio *aytoALC*. Para abrir la tabla hay que realizarlo desde el *Gestor de proyectos*
situado en el menú *Mostrar* de *gvSIG Desktop*. El proceso de abrir una tabla es el genérico 
a abrir cualquier archivo, primero se selecciona *Tabla* como tipo de datos a abrir, se selecciona 
la opción de *Nuevo*, lo que habilita una ventana donde se tiene que seleccionar la pestaña 
*Base de datos*. Esa pestaña muestra en su zona superior un desplegable donde hay que especificar 
la base de datos donde se encuentra la tabla, *aytoALC*. Una vez seleccionada la base de datos, en
la lista de tablas de esta hay que marcar la tabla en cuestión y pulsa el botón *Aceptar*.

![4_abrirPUBLICVCSGISREPO_ENTITIES_128](ejemplo_asignacion_recursos_files/4_abrirPUBLICVCSGISREPO_ENTITIES_128.png)

La siguiente imagen muestra la tabla *PUBLIC.VCSGISREPO_ENTITIES* donde solo hay dos 
entidades, la capa/tabla *EDIFICIOS* y la tabla *BASE_RESOURCES*.

El proceso de asignación de los recursos se realiza modificando la entidad donde se desea asignar,
en este caso la capa *EDIFICIOS*. Para ello es necesario obtener el formulario asociado la capa
*PUBLIC.VCSGISREPO_ENTITIES*. Para obtener el formulario de la tabla seleccionaremos la opción
*Show form* situada en el menú *Tabla* de *gvSIG Desktop* siempre y cuando la tabla este 
abierta y seleccionada.

![5_showForm_128](ejemplo_asignacion_recursos_files/5_showForm_128.png)

El formulario de la tabla es el siguiente.

![6_formPUBLICVCSGISREPO_ENTITIES_128](ejemplo_asignacion_recursos_files/6_formPUBLICVCSGISREPO_ENTITIES_128.png)

Una vez en el formulario se identifica el elemento que hace referencia a la tabla/capa *EDIFICIOS*
y se inicia la edición de la tabla para la modificación de este. Este proceso se puede realizar desde
el mismo desplegable que se mencionó anteriormente para obtener el formulario, o desde el mismo 
formulario utilizando el botón *Comenzar edición*.

![7_editarFormPUBLICVCSGISREPO_ENTITIES_128](ejemplo_asignacion_recursos_files/7_editarFormPUBLICVCSGISREPO_ENTITIES_128.png)

De los diferentes campos del formulario hay que identificar el refrente a los recursos, llamado,
*Resources*. En este hay que especificar el nombre de nuestra tabla de recursos, *BASE_RESOURCES*, 
ya que la tabla/capa edificios pertenece a la categoría *BASE*.

![8_resourcesFormPUBLICVCSGISREPO_ENTITIES_128](ejemplo_asignacion_recursos_files/8_resourcesFormPUBLICVCSGISREPO_ENTITIES_128.png)

Solo queda guardar los cambios en la entidad.

![9_guardarCambiosFormPUBLICVCSGISREPO_ENTITIES_128](ejemplo_asignacion_recursos_files/9_guardarCambiosFormPUBLICVCSGISREPO_ENTITIES_128.png)

Y terminar la edición de la tabla.

![10_tEditarFormPUBLICVCSGISREPO_ENTITIES_128](ejemplo_asignacion_recursos_files/10_tEditarFormPUBLICVCSGISREPO_ENTITIES_128.png)

Tras lo anterior la asignación de los recursos mediante la tabla de recursos a la capa *EDIFICIOS* .
ha concluido. Pero solo ha terminado la asignación de la tabla de recursos, la cual se encuentra 
sin ningún recurso almacenado en su interior.

El siguiente paso por la tanto es almacenar un recurso en la tabla ya ligada. Para ello es necesario
disponer de él o crearlo desde cero. En el caso del ejemplo se procede a crear de cero la leyenda
para la capa *EDIFICIOS*.

Para crear una leyenda hay que ir al árbol de capas situado en el *Toc* de *gvSIG Desktop* y tras
selección de la capa en cuestión pulsar botón derecho del mouse y seleccionar la opción *Propiedades*.

![11_propiedadesEDIFICIOS_128](ejemplo_asignacion_recursos_files/11_propiedadesEDIFICIOS_128.png)

La opción anterior despliega la siguiente ventana.

![12_propiedadesEDIFICIOSWin_128](ejemplo_asignacion_recursos_files/12_propiedadesEDIFICIOSWin_128.png)

Se selecciona la pestaña *Simbología* pues en esta se especifica todo lo referente a la 
representación gráfica de la capa. EL panel de de la pestaña anterior es el siguiente.

![13_simbologiaPropiedadesEDIFICIOS_128](ejemplo_asignacion_recursos_files/13_simbologiaPropiedadesEDIFICIOS_128.png)

Una vez allí y continuando con el caso del ejemplo, se selecciona la opción *Símbolo único* de
dentro de *Objetos* del cuadro de opciones de simbología situado en la parte izquierda del panel.

Dicha selección habilita el siguiente panel en la ventana.

![14_SUSimbologiaEDIFICIOS_128](ejemplo_asignacion_recursos_files/14_SUSimbologiaEDIFICIOS_128.png)

En el panel se inicia el proceso de definición de nuestra leyenda pulsando el botón
*Selección símbolo* el cual despliega el cuadro de diálogo *Selector de simbología*.

![15_SSSimbologiaEDIFICIOS_128](ejemplo_asignacion_recursos_files/15_SSSimbologiaEDIFICIOS_128.png)

En esta nueva ventana hay que definir las características gráficas de los elementos de la capa,
en este caso polígonos. Por lo tanto hay que definir como se van a representar sus bordes e interior.
Los parámetros para los bordes e interior de los polígonos de la capa edificios se detallanan
a continuación.

|**Componente**|**Color(RGB)**|**Opacidad**|**Ancho (píxel)**
|--:           |--:           |:--         |:--      
|Borde         |248  190  132 |100%        |1        
|Interior      |231  120  58  |100%        |         

Una vez especificados se aceptan los cambios pulsando el botón *Aceptar* y se cierra el cuadro 
de diálogo anterior.

Tras lo anterior ya de nuevo en el panel de la pestaña *Simbología* de la ventana *Propiedades*
de la capa *EDIFICIOS* se puede ver que el símbolo único ha cambiado según la definición 
especificada anteriormente. 

![16_NSUSimbologiaEDIFICIOS_128](ejemplo_asignacion_recursos_files/16_NSUSimbologiaEDIFICIOS_128.png)

Solo queda ahora almacenar esa simbología pulsando el botón *Más opciones* situado en la 
zona superior derecha de la ventana y seleccionar a continuación la opción *Guardar leyenda*.

![17_MOSimbologiaEDIFICIOS_128](ejemplo_asignacion_recursos_files/17_MOSimbologiaEDIFICIOS_128.png)

La opción anterior habilita un cuadro de diálogo que nos permite indicar la ruta donde almacenar la
leyenda y el nombre del fichero que almacenará esta. En el caso del ejemplo se se almacena en 
una carpeta destinada a almacenar leyendas y el nombre del archivo es el mismo que la capa con la 
extension ```.gvsleg```, es decir *EDIFICIOS.gvsleg*. Hay que destacar que el archivo con el 
recurso siempre tiene que llamarse de la misma manera que la capa de la que es recurso.

Una vez guardada la leyenda, pulsamos los botones *Aplicar*  y *Aceptar* para terminar el proceso de
definicion de la simbología de la capa.

Con el recurso ya creado hay que introducir este en la tabla de recursos, *BASE_RESOURCES*. Para 
realizar esto hay que repetir el proceso de edición de una tabla especificado para la edición de la 
tabla PUNLIC.VCSGISREPO_ENTITIES.

En primer lugar hay que abrir la tabla *BASE_RESOURCES*.Para abrir la tabla hay que realizarlo 
desde el *Gestor de proyectos* situado en el menú *Mostrar* de *gvSIG Desktop*. El proceso de 
abrir una tabla es el genérico a abrir cualquier archivo, primero se selecciona *Tabla* como 
tipo de datos a abrir, se selecciona la opción de *Nuevo*, lo que habilita una ventana donde se 
tiene que seleccionar la pestaña *Base de datos*. Esa pestaña muestra en su zona superior un 
desplegable donde hay que especificar la base de datos donde se encuentra la tabla, *aytoALC*. 
Una vez seleccionada la base de datos, en la lista de tablas de esta hay que marcar la tabla 
en cuestión y pulsa el botón *Aceptar*.

![18_abrirBASE_RESOURCES_128](ejemplo_asignacion_recursos_files/18_abrirBASE_RESOURCES_128.png)

Como resultado se obtiene la tabla vacía. Para rellenarla hay que obtener su formulario,
seleccionando la opción *Show form* situada en el menú *Tabla* de *gvSIG Desktop* siempre 
y cuando la tabla este abierta y seleccionada.

El formulario de la tabla *BASE_RESOURCES* es el siguiente.

![19_formBASE_RESOURCES_128](ejemplo_asignacion_recursos_files/19_formBASE_RESOURCES_128.png)

Para introducir un valor en la tabla hay que poner esta en edición ya sea desde
el mismo desplegable que se mencionó anteriormente para obtener el formulario, o desde el mismo 
formulario utilizando el botón *Comenzar edición*.

![20_editarFormBASE_RESOURCES_128](ejemplo_asignacion_recursos_files/20_editarFormBASE_RESOURCES_128.png)

Una vez en edición hay que crear un nuevo elemento mediante el botón *Nuevo* situado en la zona 
inferior del formulario e indicado en la imagen siguiente.

![21_nuevoElementoFormBASE_RESOURCES_128](ejemplo_asignacion_recursos_files/21_nuevoElementoFormBASE_RESOURCES_128.png)

Especificamos en el campo *nombre* el nombre completo del archivo más la extensión del 
recurso que se desea almacenar y en el campo *value* gracias al botón izquierdo se puede subir a 
la tabla dicho fichero.

En el caso del ejemplo la configuración del formulario es la siguiente.

![22_nuevoElemento2FormBASE_RESOURCES_128](ejemplo_asignacion_recursos_files/22_nuevoElemento2FormBASE_RESOURCES_128.png)

Una vez creado el nuevo elemento de la tabla solo queda guardar.

![23_guardarFormBASE_RESOURCES_128](ejemplo_asignacion_recursos_files/23_guardarFormBASE_RESOURCES_128.png)

Y posteriormente finalizar la edición de la tabla.

![24_tEditarFormBASE_RESOURCES_128](ejemplo_asignacion_recursos_files/24_tEditarFormBASE_RESOURCES_128.png)

Para finalizar el proceso de asignación de un recurso de la tabla de recursos a una capa solo hay 
que hacer checkout de esta tabla en cuestión, tal y como se indica en el apartado [*Añadir una capa
del repositorio*](https://gvsigassociation.github.io/gvsig-desktop-docs/es/userdoc/vcsgis/utilizacion_basica/anadir_una_capa_del_repositorio_t.html).

Tras todo lo realizado anteriormente cualquier usuario que realice una descarga del repositorio de la 
capa EDIFICIOS presetará la misma leyenda asociada.


de opciones
>   * Asignacion de una leyenda por defecto a la capa.
>   * Creacion de la leyenda y guardar en disco.
>   * Creacion de la tabla de recursos y cargar la leyenda asociandola a la capa.
>   * Meter la tabla de recursos en el vcs
>   * Hacer checkout de la capa y ver que aplica a la entidad.


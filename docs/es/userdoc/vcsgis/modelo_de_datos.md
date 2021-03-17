{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Modelos de datos{% endcomment %} 

(**en contruccion**)
> * Describir que entendemos aqui como modelo de datos.
> * Su configuracion.
> * Checkout

**Introducción**.

Trabajar con problemas complejos muchas veces precisa realizar un análisis adecuado, y definir un modelo de
datos para representarlos de manera correcta. Normalmente el modelo de datos se materializa en un conjunto 
de tablas, registros, relaciones y restricciones de una base de datos relacional. 

Con *gvSIG Desktop* se puede acceder a esas tablas, realizar consultas, visualizar sus datos y si tienen información 
geográfica representarla en un mapa. De modo que, es posible ver cada una de las tablas que conforman el modelo 
de forma independiente o ver ese conjunto de tablas como un modelo de datos coherente, como un todo. Si se adopta
la última opción, hay que añadir a *gvSIG Desktop* información para que el sofware sea consciente de las 
relaciones que hay entre tablas, las restricciones establecidas para algunos de sus atributos, así como cual es
la forma de acceder a cada una de las tablas del modelo de datos. Normalmente se emplean dos herramientas de
*gvSIG Desktop* para realizar lo anterior, el *gestor de columnas* y los *repositorios de datos* o *espacios 
de trabajo de base de datos*. 

A través del *gestor de columnas* se declaran que relaciones existen entre las tablas. Por ejemplo, si se tiene 
una tabla de *facturas* y otra de *líneas de factura*, se define una relación entre ambas, indicando como obtener
las líneas de una factura, o como obtener la factura asociada a una línea de factura. *GvSIG Desktop*  permite 
declarar este tipo de relaciones entre las distintas tablas o entidades del modelo de datos, y luego cuando se
precisa presentar esta información a traves de formularios, adapta la presentación para que se pueda navegar 
entre las relaciones declaradas. Además, es posible usar estas relaciones para poder realizar búsquedas entre 
las distintas tablas del modelo de forma sencilla y más o menos transparente para el usuario.

Pero para poder "navegar" entre las distintas tablas de un modelo de datos, no solo es necesario declarar las 
relaciones que existen entre ellas; también se debe declarar como se puede acceder a cada una de las tablas 
que componen el modelo. Para esto hay que definir un *repositorio de datos*, en el que se indica donde esta 
almacenada cada tabla del modelo y como acceder a ella.

Centrando la atención en *VCSGis*, se ha integrado una herramienta que ofrece la posibilidad de cargar desde 
el repositorio del control de versionesque tanto la información relacionada con las restricciones y relaciones
tablas así como en donde se encuentran cada una de las tablas del modelo. De esta manera se puede almacenar 
la definición del modelo de datos para tablas ya integradas en el repositorio, pudiendo conectarse a ese modelo 
de datos, descargarlo y registrarlo de forma cómoda para el usuario.

Para ilustrar como configurar la parte de configuración de modelos de datos en el contexto de VCSGis
vamos a trabajar un modelo sencillo, con solo unas pocas tablas.

Las tablas seleccionadas para realizar el ejemplo son *countrie*, *continent*, *region* y *economy*. Estas tablas
representan paises, continentes, subregión y el tipo de región segun su economía respectivamente. Las relaciones
establecidas entre capas se detrallan en la siguiente tabla:

|**Tablas**     |**countrie**                       |**continent**                     |**region**                         |**economy**
|:--            |:--                                |:--                               |:--                                |:--                               
|**countrie**   |**-**                              |Colaboración (1:1) por *CONTINENT*|Colaboración (1:1) por *REGION_WB* |Colaboración (1:1) por *ECONOMY*
|**continent**  |Agregado (1:n) por *CONTINENT*     |**-**                             |**-**                              |**-**                              
|**region**     |Agregado (1:n) por *REGION_WB*     |**-**                             |**-**                              |**-**                              
|**economy**    |Agregado (1:n) por *ECONOMY*       |**-**                             |**-**                              |**-**                              

 > **Colaboración (1:1).** Se utiliza para relacionar tablas por un campo o columna 
 común. Las tablas representa información de entes diferentes que tiene relación entre si. 

 > **Agregado (1:n).** Se utiliza para establecer relación entre un objeto 
 o elemento de una tabla y varios objetos o elementos de otra. Se diferencia 
 del anterior en que el grupo de elementos puede subsistir sin necesidad del 
 elemento único. 

**Configuracion del modelo de datos en VCSGis**

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

**Conectarnos a un modelo de datos**

Una vez definido y cargado en el repositorio un modelo de datos, se sigue el flujo de trabajo 
habitual con *VCSGis*. Crear una copia de trabajo y dercargar en ellas las tablas con las 
que se busca trabajar. Ahora bien, se dispondrá de una herramienta que permite "conectar" 
a un modelo de datos. Esta herramienta presenta para una copia local determinada cuales son los 
modelos de datos que hay definidos en ella pudiendo seleccionar uno. Tras la selección se muestran las 
tablas que componen dicho modelo de datos, y si tras conectarse a el, se descargará las tablas 
del modelo y las registrará para que *gvSIG Desktop* pueda acceder a ellas aunque no esten cargadas 
como tablas o capas del proyecto actual.

>
> Aqui ejemplo
> 
> Continuar con el ejemplo de paises y continentes
> 

**Consideraciones espaciales sobre los modelos de datos**

El sistema de "repositorio de datos" que tiene *gvSIG Desktop* para declarar donde esta cada tabla,
así como la forma en que se definen las relaciones entre estas, usa un modelo "plano" de 
espacio de nombres. Es decir, no tiene esquemas o subespacios de nombres. Todas las tablas que
se cargan en *gvSIG Desktop* comparten el mismo espacio de nombres. Esto implica que si se realiza una conexión 
simultanea a dos modelos de datos que contengan tablas con el mismo nombre estos colisionaran, 
pisandose unas tablas a otras.

Para evitar problemas de este tipo, sobre todo con modelos de datos que conviven en el mismo repositorio 
de *VCSGis*, es recomendable que los nombres de tablas de un modelo lleven un prefijo que identifique
a ese modelo. De esta forma se pueden cargar en el control de versiones varios modelos sin 
que colisionen entre ellos.


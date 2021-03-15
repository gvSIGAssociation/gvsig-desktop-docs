{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Modelos de datos{% endcomment %} 

(**en contruccion**)
> * Describir que entendemos aqui como modelo de datos.
> * Su configuracion.
> * Checkout

**Introducción**.

Cuando estamos trabajando con problemas complejos muchas veces precisaremos ralizar un analisis 
adecuado, y definir un modelo de datos para representar nuestro problema. Normalmente el 
modelo de datos lo materializaremos en un conjunto de tablas, registros, relaciones y restricciones 
de una base de datos relacional. gvSIG desktop permite acceder a esas tablas; podremos consultarlas, 
ver sus datos y si tienen informacion geografica representarla en un mapa. Ahora bien, podemos 
restringirnos a ver cada una de las tablas que forman el modelo de forma independiente o ver el 
conjunto de tablas como un modelo de datos coherente, como un todo. Si nos decidimos por esta ultima
opcion, deberemos añadir a gvSIG desktop informacion para que sea consciente de las relaciones que hay
entre las tablas o las restricciones establecidas para algunos de sus atributos, asi como cual es la 
forma de acceder a cada uno de las tablas del modelo de datos. Normalmente emplearemos dos herramientas 
de gvSIG desktop para ello, el "gestor de columnas" y los "repositorio de datos" o "espacios de trabajo 
de base de datos". 

A traves del "gestor de columnas" declararemos que relaciones existen entre las tablas, por ejemplo, 
si tenemos una tabla de "facturas" y otra de "lineas de factura", definiremos una relacion entre 
ambas, indicando como obtener las lineas de una factura, o como obtener la factura asociada a una 
linea de factura. Entre ambas tablas existira una relacion de agregacion. gvSIG permite declarar 
este tipo de relaciones entre las distintas tablas o entidades del moddelo de datos, y luego cuando 
se precisa presentar esta informacion a traves de formularios adapta la presentacion para que se 
pueda navegar entre las relaciones decleradas. Ademas es posible usar estas relaciones para poder 
realizar busquedas entre las distintas tablas del modelo de forma sencilla y mas o menos transparente
para el usuario.

Pero para poder "navegar" entre las distintas tablas de un modelo de datos, no solo es necesario 
declarar las relaciones que existen entre ellas; tambien deberemos declarar como se puede acceder 
a cada una de las tablas que componen el modelo. Para esto deberemos definir un "repositorio de datos", 
en el que se indica donde esta almacenada cada tabla del modelo y como acceder a ella.

Como una herramienta dentro de VCSGis, se ha integrado la posibilidad de que tanto la informacion 
relacionada con la las restricciones y relaciones tablas como en donde esta cada una de las 
tablas del modelo se puedan cargar desde el repositrio del control de versiones. Asi podemos
almacenar la definicion del modelo de datos en tablas que viven en el repositrio y podemos conectarnos 
a ese modelo de datos, descargandose y registrandose este de forma comoda para el usuario.

Para ilustrar como configurar la parte de configuracion de modelos de datos en el contexto de VCSGis
vamos a trabajar un modelo sencillo, con solo unas pocas tablas, estados, continentes y XXXX.

>
> Aqui describir las relaciones entre las tablas
>


**Configuracion del modelo de datos en VCSGis**

Configurar un modelo de datos en VCSGis requiere cierto analisis y planificacion. No esta pensado 
para ir creandolo sobre la marcha. Antes de añadir las tablas que forman el modelo deberemos tener
bien claras y declaradas las relaciones, entre ellas asi como las restricciones que queremos aplicar
a los atributos de estas. Adicionalmente tambien declararemos como se deben presentar los datos de
las distintas tablas al usuario, normalmente en forma de "formularios". Para realizar toda esta 
tarea nos apollaremos en las herramientas de gvSIG desktop de "crear nueva tabla o capa" y el 
"gestor de columnas". Una vez declarada la informacion que define el modelo de datos, podremos añadir
las tablas que lo componen al repositorio de VCSGis.

Ahora queda solo indicarle a VCSGis que tablas de las que hay en el repositorio forman parte de un
modelo de datos. Para ello precisaremos disponer de acceso de escritura a la base de datos en la
que reside el repositorio en el que estan las tablas que forman el modelo. Cargaremos en el proyecto
de gvSIG desktop la tabla VCSGISREPO_ENTITIES y, bien directamente sobre la tabla o en el formulario 
asociado a ella, indicaremos para cada "entidad" a que modelo de datos pertenece.

>
> Aqui ejemplo
> 
> Preparar ejemplo con tablas de continentes y paises (y alguna lista de valores). 
> Tener las dos tablas en CVS junto a la documentacion para poder descargarlas y probarlo.
>

**Conectarnos a un modelo de datos**

Una vez tenemos definido y cargado en el repositorio un modelo de datos, trabajaremos como es 
habitual con VCSGis. Crearemos una copia de trabajo y descargaremos a el las tablas con las 
que vayamos a trabajar. Ahora bien, disponderemos de una herramienta que nos permite "conectarnos" 
a un modelo de datos. Esta herramienta nos presentara para una copia local dada cuales son los 
modelos de datos que hay definidos en ella. Podremos seleccionar uno, y nos mostrara las 
tablas que componen ese modelo de datos, y si nos conectamos a el, se descargara las tablas 
del modelo y las registrara para que gvSIG sepa como acceder a ellas aunque no esten cargadas 
como tablas o capas de nuestro proyecto.

>
> Aqui ejemplo
> 
> Continuar con el ejemplo de paises y continentes
> 

**Consideraciones espaciales sobre los modelos de datos**

El sistema de "repositorio de datos" que tiene gvSIG desktop para declarar donde esta cada tabla,
asi como la forma en que se definen las relaciones entra estas, usa un modelo "plano" de 
espacio de nombres, es decir, no tiene esquemas o subespacios de nombres. Todas las tablas que
se cargan en gvSIG destop comparten el mismo espacio de nombres. Esto es, si nos conectamos 
simultaneamente a dos modelos de datos que contengan tablas con el mismo nombre estos colisionaran, 
pisandose unas tablas a otras.

Para evitar problemas de este tipo, sobre todo con modelos de datos que conviven en el mismo repositorio 
de VCSGis, es recomendable que los nombres de tablas de un modelo lleven un prefijo que identifique
a ese modelo. De esta forma podremos cargar en el control de versiones varios modelos sin 
que colisionen entre ellos.


{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Consideraciones {% endcomment %} 

(**en contruccion**)
> * Describir que entendemos aqui como modelo de datos.
> * Su configuracion.
> * Checkout


Cuando estamos trabajando con problemas complejos muchas veces precisaremos ralizar un analisis adecuado, y definir un modelo de datos para representar nuestro problema. Normalmente el modelo de datos lo materializaremos en un conjunto de tablas, registros, relaciones y restricciones de una base de datos relacional. gvSIG desktop permite acceder a esas tablas; podremos consultarlas, ver sus datos y si tienen informacion geografica representarla en un mapa. Ahora bien, podemos restringirnos a ver cada una de las tablas que forman el modelo de forma independiente o ver el conjunto de tablas como un modelo de datos coherente, como un todo. Si nos decidimos por esta ultima opcion, deberemos añadir a gvSIG desktop informacion para que sea consciente de las relaciones que hay entre las tablas o las restricciones establecidas para algunos de sus atributos, asi como cual es la forma de acceder a cada uno de las tablas del modelo de datos. Normalmente emplearemos dos herramientas de gvSIG desktop para ello, el "gestor de columnas" y los "repositorio de datos" o "espacios de trabajo de base de datos". 

A traves del "gestor de columnas" declararemos que relaciones existen entre las tablas, por ejemplo, si tenemos una tabla de "facturas" y otra de "lineas de factura", definiremos una relacion entre ambas, indicando como obtener las lineas de una factura, o como obtener la factura asociada a una linea de factura. Entre ambas tablas existira una relacion de agregacion. gvSIG permite declarar este tipo de relaciones entre las distintas tablas o entidades del moddelo de datos, y luego cuando se precisa presentar esta informacion a traves de formularios adapta la presentacion para que se pueda navegar entre las relaciones decleradas. Ademas es posible usar estas relaciones para poder realizar busquedas entre las distintas tablas del modelo de forma sencilla y mas o menos transparente para el usuario.

Pero para poder "navegar" entre las distintas tablas de un modelo de datos, no solo es necesario declarar las relaciones que existen entre ellas; tambien deberemos declarar como se puede acceder a cada una de las tablas que componen el modelo.
Para esto deberemos definir un "repositorio de datos", en el que se indica donde esta almacenada cada tabla del modelo y como acceder a ella.

Como una herramienta dentro de VCSGis, se ha integrado la posibilidad de que tanto la informacion relacionada con la las restricciones y relaciones tablas como en donde esta cada una de las tablas del modelo se puedan cargar desde el repositrio del control de versiones. Asi podemos almacenar la definicion del modelo de datos en tablas que viven en el repositrio y podemos conectarnos a ese modelo de datos, descargandose y registrandose este de forma comoda para el usuario.



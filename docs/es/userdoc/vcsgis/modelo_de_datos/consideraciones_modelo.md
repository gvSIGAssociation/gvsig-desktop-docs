{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Consideraciones modelo {% endcomment %} 

(**en contruccion**)

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

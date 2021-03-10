{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Consideraciones {% endcomment %} 

(**en contruccion**)
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

>   * Asignar a la entidad una tabla de recursos (admin).
>   * Asignacion de una leyenda por defecto a la capa.
>   * Creacion de la leyenda y guardar en disco.
>   * Creacion de la tabla de recursos y cargar la leyenda asociandola a la capa.
>   * Meter la tabla de recursos en el vcs
>   * Hacer checkout de la capa y ver que aplica a la entidad.


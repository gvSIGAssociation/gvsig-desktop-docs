{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Introduccion {% endcomment %} 

En *gvSIG desktop* podemos asociar *recursos* a una capa o tabla. Estos recursos, cuando 
estamos trabajando con tablas de tipo fichero, como puede ser un shape, se almacenan junto a
este. Asi por ejemplo, podemos asociar a un shape, un fichero ".cpg", con la informacion sobre
la codificacion a usar para los textos, un fichero ".gvsleg", para que tenga una leyenda 
por defecto cuando lo carguemos, un fichero  ".gvslab o ".sld" para que tenga asociado un etiquetado
por defecto, ".frm" en el que especifiquemos que aspecto debe tener el formulario asociado a
la tabla, incluso podriamos asociar informes personalidados, ".report". Todos estos tipos de 
ficheros con informacion complementaria a los datos de la tabla se consideran recursos asociados a ella.
Y estos recursos citados son solo una muestra de los que podriamos asociar a una tabla.

Ahora bien, cuando estamos trabajando con VCSGis, las tablas se encuentran almacenadas en un 
repositorio remoto, y se descargan a una base de datos local para trabajar con ellas, entonces...
¿ podemos asociar recursos a estas tablas que estan en un base de datos bajo un 
sistema de control de versiones ?

VCSGis provee mecanismos para poder asociar esos recursos, y almacenarlos en el propio control
de versiones de forma que estos se descarguen automaticamente a la copia local cuando se 
descargan las tablas. Para hacer esto, es preciso la intervencion del administrador del 
repositorio de versiones, y una vez configurado como gestionar los recursos de cada tabla, los usuarios
ya podran acceder a ellos de forma trasparente. Con esto se garantiza que todos los usuarios ya no solo 
dispongan de los datos de una misma tabla actualizada, sino también del modo de representar esta asi como
de los ficheros de recursos que esten asociados a ella.

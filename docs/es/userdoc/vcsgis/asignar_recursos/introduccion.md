{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Introducción {% endcomment %} 

En *gvSIG desktop* podemos asociar *recursos* a una capa o tabla. Estos recursos, cuando 
estamos trabajando con tablas de tipo fichero, como puede ser un shape, se almacenan junto a
este. Así por ejemplo, podemos asociar a un shape, un fichero ".cpg", con la información sobre
la codificación a usar para los textos, un fichero ".gvsleg", para que tenga una leyenda 
por defecto cuando lo carguemos, un fichero  ".gvslab" o ".sld" para que tenga asociado un etiquetado
por defecto, ".frm" en el que especifiquemos que aspecto debe tener el formulario asociado a
la tabla, incluso podríamos asociar informes personalizados, ".report". Todos estos tipos de 
ficheros con información complementaria a los datos de la tabla se consideran recursos asociados a ella.
Siendo los recursos citados solo una muestra de los que podríamos asociar a una tabla.

Ahora bien, cuando estamos trabajando con VCSGis, las tablas se encuentran almacenadas en un 
repositorio remoto, y se descargan a una base de datos local para trabajar con ellas, entonces...
¿ podemos asociar recursos a estas tablas que están en un base de datos bajo un 
sistema de control de versiones ?

VCSGis provee mecanismos para poder asociar esos recursos, y almacenarlos en el propio control
de versiones de forma que estos se descarguen automáticamente a la copia local cuando se 
descargan las tablas. Para hacer esto, es preciso la intervención del administrador del 
repositorio de versiones, y una vez configurado como gestionar los recursos de cada tabla, los usuarios
ya podrán acceder a ellos de forma trasparente. Con esto se garantiza que todos los usuarios ya no solo 
dispongan de los datos de una misma tabla, sino también del modo de representar esta, así como
de los ficheros de recursos que estén asociados a ella.

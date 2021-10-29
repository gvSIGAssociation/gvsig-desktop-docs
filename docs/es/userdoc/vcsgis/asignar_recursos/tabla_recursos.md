{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Tabla de recursos {% endcomment %} 

En VCSGis, La tabla de recursos es una tabla formada por dos campos, *nombre* y *value*.
El campo *nombre* de tipo ```String```, identifica de manera única el recurso y la capa/tabla a la 
cual esta asociada, mientras que el campo *value* de tipo ```byteArray``` almacena el recuso en sí,
es decir el archivo. Para realizar la asignación de este recurso, previa a su creación y 
actualización con los diferentes recursos, hay que realizar modificaciones en las entidades del 
repositorio de la tabla **VCSGISREPO_ENTITIES** asignándole a cada una de las tablas o entidades 
del repositorio en qué tabla están almacenados los recursos de ella.

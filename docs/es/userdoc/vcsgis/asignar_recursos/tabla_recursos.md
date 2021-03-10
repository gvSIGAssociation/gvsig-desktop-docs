{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Tabla de recursos {% endcomment %} 

La tabla de recursos es un archivo de tipo tabla constituida por dos campos, *nombre* y *value*.
El campo *nombre* de tipo ```String```, identifica de manera única el recurso y la capa/tabla a la 
cual esta asociada, mientras que el campo *value* de tipo ```byteArray``` almacena el recuso en sí,
es decir el archivo que lo almacena. Para realizar la asignación de esta, previa a su creación y 
actualización con los diferentes recursos, hay que realizar modificaciones en la entidades del 
repositorio de la tabla **PUBLIC.VCSGISREPO_ENTITIES** asignándole a cada una de ellas su recurso, si
sta dispone de el. 
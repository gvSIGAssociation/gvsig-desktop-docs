{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Introduccion {% endcomment %} 

Como se dijo en el apartado anterior *VCSGis* es un sistema centralizado para compartir información, estando en su núcleo un **repositorio**, es decir un almacén central de datos, que salva la información en forma de tablas. Este almacén no es más que un sistema de base de datos que tiene tanto la información que modifican los usuarios del software, en el caso de *VCSGis* tablas o capas, como las tablas que almacenan los cambios producidos en los anteriores.

Cada tabla del usuario mantendrá su propio control de versiones de forma independiente a las demás tablas del repositorio, llevando un control de los registros que se van insertando, modificando o borrando en ella. La unidad mínima de información que sigue o controla *VCSGis* es el registro de una tabla, sin hacer seguimiento de los cambios en los campos de cada registro.

Cuando un cliente accede a los datos del repositorio en *VCSGis*, normalmente ve la última versión de este, es decir la información actual con las capas y tablas. Sin embargo el cliente también tiene la posibilidad de ver los estados previos del repositorio. Por ejemplo, un cliente podría preguntarse *¿Qué contenía esta tabla este miércoles?* o *¿Quién fue la última persona en editar esta capa y qué cambios realizó?* Estas son el tipo de posibilidades que diferencian a los sistemas de control de versiones: sistemas diseñados para guardar y registrar las modificaciones de los datos a lo largo del tiempo.

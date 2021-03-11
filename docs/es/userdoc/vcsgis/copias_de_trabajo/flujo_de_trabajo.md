{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Flujo de trabajo (Modelo  Copiar-Modificar-Fusionar) {% endcomment %} 


Este apartado define la estructura o forma de trabajar teórica con un sistema de control de versiones que presenta el modelo Copiar-Modificar-Fusionar como podría ser  *VCSGis*. Especificar  que estos mismos procesos serán explicados desde un punto de vista práctico para *VCSGis* en el apartado siguiente.

**Paso 1**: Creación de repositorio. Se lleva a cabo por el administrador y con el se da inicio al proceso.

**Paso 2:** Creación de copia de trabajo. Proceso realizado por los diferentes usuarios o clientes del repositorio y como se dijo en el apartado anterior consiste en la captura del repositorio en un instante determinado. Esa captura completamente funcional permite cualquier acción de edición o modificación y los cambios realizados en esta serán propuestos por el usuario para formar parte del repositorio.

**Paso 3:** Realización de cambios en la informacion de su copia de trabajo y verificación que funcionan correctamente

**Paso 4:** Publicación de cambios. El sistema de control de versiones *VCSGis* en este caso provee al usuario de comandos para publicar sus cambios en el repositorio por tanto estar estos disponibles para todos los usuarios registrado es en ese repositorio. En el caso de que los demás usuarios hayan publicado antes sus propios cambios, el software le provee de comandos para fusionar esos  cambios dentro de su copia de trabajo tras leer el repositorio. La fusión puede presentar dos caso bien diferenciados:

 * Los cambios del usuario afectan a elementos no modificados anteriormente por los demás usuarios y por tanto se mezclan y fusionan las tablas.
 * El usuario ha realizado cambios sobre elementos modificados anteriormente por otros usuarios y ya registrados en el repositorio, en ese caso se entra en conflicto y el usuario decide que cambios son los que se quedan finalmente en el repositorio los propios o los ya presentes.

Al  acto de publicar los datos en el servidor se le denomina hacer **confirmar**, *commit*, y al proceso de actualizar la copia de trabajo con la información del repositorio se le denomina **actualizar**, *update*.


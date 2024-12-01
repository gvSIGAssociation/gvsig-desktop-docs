{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Introduccion {% endcomment %} 

La herramienta de control de versiones *VCSGis* de *gvSIG Desktop* incluye un mecanismo de gestión 
de usuarios básico que le permite discriminar a que recursos tiene acceso un determinado usuario. Este
mecanismo se basa en dos sistemas, uno de autenticación y otro de autorización.

**Autenticación**  consiste  en  un  sistema  para  certificar  que  el  usuario  es  quien  dice  ser;
lo  más común es utilizar una combinación de identificador de usuario único y contraseña, aunque existen otros.
*VCSGis* utiliza este sistema de *usuario+contraseña*.

**Autorización** consiste en dar acceso a una serie de operaciones o recursos a un usuario. Por ejemplo,
si un usuario puedo hacer una operación de *commit* o *checkout*, o no la puede hacer, o si puedo acceder
a una determinada tabla, solo para hacer *checkout* o también para *commit*.

En un repositorio de *VCSGis* podremos activar el mecanismo de *autenticación*, o el mecanismo de 
*autenticación más autorización*. Si activamos la *autenticación*, garantizaremos que solo los usuarios
que podemos certificar quienes son, pueden acceder al sistema. Ahora bien, solo con este mecanismo,
una vez accedan al repositorio, no tendremos control de que operaciones pueden hacer o a que recursos
puede acceder. Si activamos también la *autorización*, podremos especificar tanto las operaciones que puede 
realizar un usuario, como a que recursos puede acceder.

Por defecto, cuando se crea un *repositorio* de *VCSGis*, este no tiene activados ninguno de estos
mecanismos, por lo que tendremos que activarlos manualmente.

Además, tendremos que tener en cuenta, que no existen herramientas específicas para realizar las tareas
de administración de *VCSGis* relacionadas con la gestión de usuario. Para ello el **administrador**
deberá acceder a las tablas de configuración del repositorio y realizar la configuración necesaria 
manipulando estas directamente.

En los siguientes apartados iremos viendo como se pueden llevar a cabo estas tareas de administración.

El mecanismo de control de gestión de usuario de VCSGis podemos verlo a tres niveles:
 * Requiriendo solo autenticación de los usuarios.
 * Requiriendo autenticación y con una autorización básica o por operación.
 * Requiriendo autenticación y con una autorización avanzada o por entidad.
 

 


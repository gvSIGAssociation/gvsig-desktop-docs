{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Introduccion {% endcomment %} 

La herramienta de control de versiones *VCSGis* de *gvSIG Desktop* incluye un mecanismo de gestion 
de usuarios basico que le permite discriminar a que recursos tiene acceso un determinado usuario. Este
mecanismos se basa en dos sistemas, uno de autenticacion y otro de autorizacion.

**Autenticación**  consiste  en  un  sistema  para  certificar  que  el  usuario  es  quien  dice  ser;
lo  más común es utilizar una combinación de identificador de usuario único y contraseña, aunque existen otros.
*VCSGis* utiliza este sistema de *usuario+contraseña*.

**Autorización** consiste en dar acceso a una serie de operaciones o recursos a un usuario. Por ejemplo,
si un usuario puedo hacer una operacion de *commit* o *checkout*, o no la puede hacer, o si puedo acceder
a una determinada tabla, solo para hacer *checkout* o tambien para *commit*.

En un repositorio de *VCSGis* podremos activar el mecanismo de *autenticacion*, o el mecanismo de 
*autenticacion mas autorizacion*. Si activamos la *autenticacion*, garantizaremos que solo los usuario
que podemos certificar quienes son, pueden acceder al sistema. Ahora bien, solo con este mecanismo,
una vez accedan al repositorio, no tendremos control de que operaciones pueden hacer o a que recursos
puede acceder. Si activamos tambien la *autorizacion*, podremos especificar tanto las operaciones que puede 
realizar un usuario, como a que recursos puede acceder.

Por defecto, cuando se crea un *repositorio* de *VCSGis*, este no tiene activados ninguno de estos
mecanismos. y tendremos que activarlos manualmente.

Ademas, tendremos que tener en cuenta, que no existen herramientas especificas para realizar las tareas
de administracion de *VCSGis* relacionadas con la gestion de usuario. Para ello el **administrador**
debera acceder a las tablas de configuracion del repositorio y realizar la configuracion necesaria 
manipulando estas directamente.

En los siguientes apartados iremos viendo como se pueden llevar a cabo estas tareas de administracion.

El mecanismo de control de gestion de usuario de VCSGis podemos verlo a tres niveles:
 * Requiriendo solo autenticacion de los usuario.
 * Requiriendo autenticacion y con una autorización básica o por operación
 * Requiriendo autenticacion y con una autorización avanzada o por entidad
 

 


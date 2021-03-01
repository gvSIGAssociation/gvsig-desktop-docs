{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Iniciar servidor VCSGis {% endcomment %} 


Como se dijo en el apartado anterior, la herramienta de control de versiones VCSGis dispone de la posibilidad de suministrar un repositorio local a otras máquinas mediante la inicialización de este en un servidor propio en gvSIG desktop. En otras palabras VCSGis permite que un único equipo almacene el repositorio y este suministre la información a los demás equipos mediante una conexión (URL) al repositorio remoto. Esta opción se puede configurar ejecutando el comando *Servidor VCSGis* situado dentro de *Herramientas*, desplegable *VCSGis*, despleglable *Administración*.

![servidorVCSGis1](img/100_servidor_VCSGis.png)

Tras la ejecución del comando anterior se obtiene el siguiente interfaz.

![servidorVCSGis2](img/101_servidor_VCSGis_win.png)

En esta ventana hay que especificar la base de datos o repositorio que va a ser suministrado mediante conexión remota así como el puerto por el cual se va a enviar la información. Una vez especificado lo anterior solo queda iniciar el proceso pulsando el botón *Reiniciar* situado en la zona inferior de la ventana. Puede también pararse el suministro de dicha información con el botón *Parar* adyacente al anterior. Tras iniciar el proceso la ventana en la zona central muestra las peticiones realizadas al servidor.

![servidorVCSGis3](img/102_servidor_VCSGis_peticiones.png)

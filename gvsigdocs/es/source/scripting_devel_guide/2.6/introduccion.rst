Introducción
===============

Qué es el Módulo de Scripting
-----------------------------

El Módulo de Scripting es un módulo de programación integrado completamente en gvSIG desktop 2. 
Este módulo se integró desde las versiones 2.x de gvSIG desktop.

Qué necesitas
-------------

Para seguir esta guía tan solo necesitas tener instalado la versión de gvSIG desktop 2.6. El Scripting Framework o 
Módulo de Scripting vienen instalados por defecto en todas las instalaciones de gvSIG desktop, tanto instalables como portables.

La última versión disponible de gvSIG desktop 2 que podrás encontrar en:
http://www.gvsig.com/es/productos/gvsig-desktop/descargas

También será necesario tener instalado el paquete de **Scripting Composer Tools**. Este paquete es un 
conjunto de herramientas desarrollado para facilitar la tarea del desarrollador (más información en el 
siguiente apartado donde se explican todas sus características). Incluye herramientas de autocompletado, 
code navigator, la herramienta de interfaces visuales Abeille, entre otros. Se podrán instalar 
directamente desde el **Administrador de Complementos**.

Ir a :menuselection:`Herramientas --> Administrador de Complementos` y seleccionaremos ``Instalación estándar``.

.. figure::  images/inst_1.png
   :align:   center

Hacer una busqueda de las **Composer Tools**:

.. figure::  images/inst_2.png
   :align:   center

Cuando la instalación a finalizado, abriendo el :menuselection:`Herramientas --> Scripting --> Editor de Scripts`, comprobar que aparece la carpeta ``ScriptingComposerTools`` y que se ha instalado correctamente.

.. figure::  images/inst_3.png
   :align:   center

Es necesario reiniciar gvSIG desktop para su uso. Si se vueelve a abrir el Editor de Scripts, se verá que aparecen una serie de botones extra en la barra de Herramientas:

.. figure::  images/inst_4.png
   :align:   center

Qué nos permite
----------------

Este módulo de programación nos dará la oportunidad de desarrollar nuestras propias herramientas y extensiones para gvSIG desktop.

Los scripts se podrán modificar, adaptar, intercambiar y desarrollar de una manera sencilla, y lo más importante, muy rápida.

Una de las ventajas es que dada la facilidad del lenguaje Python, no será necesario tener conocimientos 
extensos de programación ni de cómo funciona al completo la arquitectura de gvSIG desktop para poder 
desarrollar la herramienta que se puedan necesitar.

Las posibilidades son infinitas, permitirá:
- Automatizar tareas
- Añadir funcionalidades
- Crear nuevos geoprocesos
- Personalizar gvSIG desktop
- Creación de extensiones (Plugins)
- Uso de la API de gvSIG: tratamiento de espaciales, conexiones de datos, generación de mapas, etc.

Qué lenguaje utilizamos
-----------------------

El lenguaje principal en el que se ha centrado el desarrollo es python en su implementación de jython `<http://www.jython.org/>`_ .

**Jython es una implementación de Python realizada en Java.**

Esta implementación nos permite trabajar con la API de gvSIG desktop (aplicación realizada en Java) usando scripts 
utilizando la sintaxis de Python, facilitando mucho el desarrollo y ejecución de estos, solo necesitando tener 
instalado gvSIG desktop para poder programar.

Esto nos da unas ventajas enormes, por un lado, Python es un lenguaje muy sencillo de aprender, por otro lado, 
no se necesita de una compilación previa con un IDE externo, sino que la compilación del código necesario se realiza 
sobre la marcha, cada vez que ejecutamos nuestro script. Esto nos permite realizar modificaciones en nuestros script 
e irlo probando mientras tenemos gvSIG desktop abierto.

Además, tiene compatibilidad con muchas de las librerías de Python existentes, y todas (o mayoría) de Java.


Cómo acceder al Módulo de Scripting
-----------------------------------

Una vez instalado gvSIG desktop 2 ya lo podemos abrir. Para acceder a este módulo de programación lo haremos a través 
del menú :menuselection:`Herramientas --> Scripting`. Aquí nos encontraremos con 3 opciones:

Scripting Launcher / Lanzador de scripts
++++++++++++++++++++++++++++++++++++

.. figure::  images/scripting_launcher.png
   :align:   center

Se trata de un lanzador de scripts, una lista con accesos directos a los scripts que tenemos.
Según vayamos creando y almacenando nuestros scripts, estos pasaran a formar parte de esta 
lista que podremos tener abierta y accesible para ejecutar un script que necesitemos en cualquier 
momento con un doble click. Es muy cómodo si preparamos scripts para ejecutarlos mientras estemos 
trabajando, una forma rápida de tenerlos a mano.


Scripting Composer / Editor de scriprts
++++++++++++++++++++++++++++++++++++

.. figure::  images/scripting_composer.png
   :align:   center

Es la ventana principal de este módulo. Aquí podremos crear, ordenar y almacenar todos nuestros scripts.

Los botones principales: Nuevo, Abrir, Guardar, Guardar y Ejecutar, Cerrar.. Una vez creemos un fichero nuevo, podremos escribir nuestro código.

La ejecución del script aparecerá reflejada en la consola que se sitúa en la parte inferior,

Jython Console / Consola de Jython
++++++++++++++++++++++++++++++++

.. figure::  images/scripting_console.png
   :align:   center

Es una consola que nos permitirá ejecutar código directamente, ejecutándose línea a línea. Nos permite consultar variables y ver cómo se van modificando.

Otra función interesante es que nos ofrecerá una ayuda de los comandos que están disponibles según el código que estemos 
escribiendo, o qué tipo de métodos tienen disponibles las diferentes clases de gvSIG desktop.

Librerías de gvSIG desktop para Scripting
------------------------------------------------------------------

Hemos creado una librería escrita en Jython denominada ``gvsig``. Su función es inyectar métodos extra en estas clases de 
Java ya existentes en la API de gvSIG desktop y ampliar mediante nuevas funciones la potencia y facilidad de uso de este módulo.

Su objetivo es el disminuir el número de líneas requeridas para realizar ciertas operaciones y hacer accesible la API de gvSIG desktop 
de una manera más sencilla desde Jython.

Las librerías Java de las que se compone gvSIG desktop están totalmente accesibles desde nuestros scripts en Jython, siendo 
posible sin ninguna restricción en el acceso a ellas y en la creación de extensiones de la misma forma que si las hiciéramos directamente en Java.

Organización de la librería gvsig
---------------------------------

El Módulo de Scripting viene con diversas librerías:

- ``gvsig``: pertenecen las funciones principales de gvSIG desktop, principalmente para el acceso y manejo de datos.
  Contiene funciones útiles y los métodos inyectados en las clases de gvSIG. También contiene el resto de módulos que explicamos.
- ``gvsig.commonsdialog``: encargada de la generación de ventanas, desde a mensajes de alerta a rutas de ficheros.
- ``gvsig.geom``: contiene todas las funciones relacionadas con las geometrías

Además, hemos incluido otras clases importantes que nos ayudarán mucho la generación de scripts:

- ``gvsig.libs.formpanel.FormPanel``: Esta clase nos ayudará en la generación de script con interfaces visuales
- ``gvsig.libs.gvpy``: Librería para la ejecución de geoprocesos desde Scripting
- ``gvsig.libs.toolbox.ToolboxProcess``: Clase para la creación de geoprocesos que serán añadidos a la Toolbox y podrán ser utilizados desde el Modelizador.
- ``gvsig.libs.load_project.load_project()``: Función para abrir un proyecto en gvSIG desktop desde un fichero.
- etc

Es recomendable importar tan solo las librerías necesarias para la ejecución del script.

Si nuestro script contiene otras librerías propias que también hemos programado, al realizar su importación podemos forzar 
la recarga de estas librerías (sino los cambios no se verán reflejados) utilizando la función `reload()`. La forma correcta de hacerlo sería::

    import lib
    reload(lib)

Creación de un script
-------------------------------------

.. |new| image:: images/icon-new.png

Para crear un script nuevo, trabajaremos en el **Editor de scrpts** presiona el botón 
de Nuevo |new| situado arriba a la izquierda, o en :menuselection:`Archivo --> Nuevo` se nos abrirá una pantalla sobre el tipo de script a crear.

.. figure::  images/nuevo_script.png
   :align:   center

En esta ventana debemos escribir el nombre y descripción de lo que vayamos a crear. En el tipo de archivo podremos elegir qué crear. Las opciones son:

- Script: Programa con código lineal que podremos ejecutar.
- Dialog: Programa con código y una interfaz visual. (No recomendado, para scripts con interfaz visual usaremos también el tipo script)
- Project: Aún no habilitado, para futuras versiones.
- Folder: Crea una carpeta en nuestra lista de "Scripts de usuario".

Podemos elegir el lenguaje de programación que prefiramos. Los lenguajes soportados son:

- ECMAScript
- Python: es el lenguaje en que tenemos centrado el desarrollo
- Groovy

Aunque estan cargados los motores de ejecucion para ECMAScript y Grovvy, estos no son usados habitualmente
por el equipo de desarrollo de gvSIG desktop ni tienen soporte en las herramientas del editor, por lo que se recomienda
el uso de Python.

.. figure::  images/nuevo_script_lenguajes.png
   :align:   center

En ``Save on`` se elije en qué carpeta guardamos el nuevo script. Las dos últimas cajas de texto son sobre información del Autor y Versión.

Hacemos click en "Accept". Esto creará el nuevo script en blanco, que aparecerá abierto para su edición. Veremos que aparece nuevo en nuestro listado de scripts de usuario y se abre una pestaña con el nombre del script. En esta pestaña un asterisco aparecerá indicando si el script contiene cambios que no han sido guardados. Debajo aparece el código por defecto, una plantilla con la estructura básica, y debajo del todo se puede ver la salida por consola.

Los scripts creados se almacenan en la carpeta  ``preferences/gvSIG/plugins/org.gvsig.scripting.app.mainplugin/2.6.1/scripts/`` dentro de la instalacion de la 
portable o en la carpeta ``gvSIG/plugins/org.gvsig.scripting.app.mainplugin/2.6.1/scripts/`` dentro del *home* del usuario si se usa un instalable en lugar
de la portable.

Ahora podemos escribir nuestro primer script. El ejemplo que viene por defecto es totalmente válido:

.. code-block:: python
    :linenos:
    :emphasize-lines: 5

    # encoding: utf-8

    import gvsig

    def main(*args):

        #Remove this lines and add here your code

        print "hola mundo"
        pass

En primer lugar, realiza una importación de la librería que vamos a utilizar, la librería de scripting ``gvsig``, y 
luego define dentro de la función principal main(), el comando print que hará salir el valor por consola.
En este caso, una cadena de texto.

.. figure::  images/scripting_composer_2.png
   :align:   center

En Scripting en gvSIG desktop, la función que se va a ejecutar por defecto **será siempre la función main()**. 
La ejecución de los scripts comenzará ejecutando esta función.

.. note::

   Todos nuestros scripts deben de contener la función main() para su correcta ejecución. No será obligatorio si van a ser usados como librerías.

.. |saveandexecute| image:: images/icon-saveandexecute.png
.. |save| image:: images/icon-save.png
.. |execute| image:: images/icon-execute.png

Para ejecutar un script guardando |save| y ejecutando |execute| o directamente presionaremos el botón |saveandexecute| y veremos su ejecución por consola.

Podemos comprobar que la salida por consola es de "hola mundo", siendo este el objetivo que buscábamos. Con esto hemos ejecutado nuestro primer script con éxito.

Esta estructura es la estructura básica de un script en gvSIG 2.6.

Si abrimos ahora el *Lanzador de scripts*, en el menú de Scripting, veremos que ya aparece nuestro script en el nuevo listado.

.. note::

    Lo recomendable es generar los scripts dentro de su propia carpeta. Esto nos permitirá usarlos como módulos 
    dándonos varias opciones: usar ficheros autorun.py (autoejecutable al inicio de gvSIG desktop), fichero __init__.py (nos permitirá 
    trabajar como si fuera un módulo permitiéndonos importar librerías que estén en la misma carpeta) y la creación de paquetes de Scripts

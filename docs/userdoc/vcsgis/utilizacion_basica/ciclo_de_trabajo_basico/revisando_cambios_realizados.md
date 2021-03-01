{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Revisando y enviando los cambios realizados {% endcomment %} 

Para explicar mejor este comportamiento se va a usar el siguiente ejemplo:

Un usuario (Pedro) modifica una serie de elementos de una capa de su copia de trabajo (CopiaTrabajo2) llamada PINTURA_VIAL, tras terminar edición (eliminar elementos) ejecuta el comando *Mostrar cambios*. Como resultado al seleccionar la opción Local de la ventana Mostrar cambios, se muestran una serie de registros correspondientes a los citados cambios y solo tendría que pulsar el botón confirmación (Commit) para actualizar esos cambios de su copia de trabajo en el repositorio. Proceso que termina realizando.

![ejemplo1](img/33_ejemplo_mod_CopiaTrabajo2.png)

Paralelo al trabajo del usuario Pedro, otro usuario (Sara) trabaja en su copia de trabajo (CopiaTrabajo1) en la misma capa que Pedro y justamente en los mismos elementos que este modificando su posición. Tras terminar la edición procede a ejecutar el comando *Mostrar cambios* para subir sus cambios al repositorio, pero Pedro ya ha actualizado el repositorio con sus cambios previamente. De modo que el resultado que arroja la ventana de *Mostrar cambios* es el siguiente;

![conflicto1](img/34_ejemplo_mod_CopiaTrabajo1.png)

En primer lugar Sara tiene que actualizar la copia de trabajo con respecto al repositorio tal y como se indica en el apartado anterior y tras eso hacer un *Commit*, pero existe un problema sus cambios entran en conflicto con los de Pedro, de ahí el color rojo de estos. Si no entrara en conflicto tras la actualización de la copia de trabajo podría realizar el *Commit* sin problema.

Para solucionar el problema Sara tiene que hacer clic sobre la pestaña *Repositorio*, descargar los cambios del repositorio.

![conflicto2](img/35_ejemplo_download_conflicto.png)

La ventana *Mostrar cambios* contiene ahora los cambios del repositorio, es decir los de Pedro y por tanto Sara tiene que decidir que cambios de este aceptar como buenos y cuales no, marcando con el check, mediante la opción mezclar, componente 11. Es importante destacar que también puede descartar los cambios de Pedro totalmente si realiza un *Merge* sin marcar ninguno de los cambios de la lista de cambios del repositorio o los suyos si marca todo los cambios del repositorio y realiza un *Merge* o si realiza simplemente un *Update*.

![conflicto3](img/36_ejemplo_posibilidades_conflicto.png)


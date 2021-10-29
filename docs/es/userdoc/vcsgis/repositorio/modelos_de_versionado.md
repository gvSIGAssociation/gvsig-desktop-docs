{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Modelos de versionado {% endcomment %} 

Tras la definición de los sistemas de control de versiones y más concretamente *VCSGis*, así como el núcleo de estos o repositorio, puede intuirse la existencia de un punto crítico en este tipo de software. Este punto no es otro que el intercambio  de información actualizada entre usuarios, evitando que los cambios de estos no se pisen unos a otros, ya que parece sencillo pensar que los usuarios de forma accidental pueden sobrescribir cambios de los demás al almacenar la información de los suyos en el repositorio.

Para entender mejor lo anterior consideramos el siguiente escenario. Suponga que tiene dos compañeros de trabajo, Pedro y Sara. Cada uno decide editar la misma tabla del repositorio a la vez. Si Pedro guarda sus cambios en el repositorio primero, es posible que, unos momentos después, Sara pueda accidentalmente sobreescribirlos con su propia versión. Aunque la versión de la tabla de Pedro no se haya perdido para siempre porque el sistema recuerda cada cambio, cualquier cambio que Pedro haya hecho no estará en la versión nueva de la tabla de Sara, porque ella nunca vio los cambios de Pedro. De lo anterior podemos decir que el trabajo de Pedro está efectivamente perdido, o al menos no están en la última versión de la tabla. 

![esquemaRepositorio](modelos_de_versionado_files/1_flujo_no_vcs.png)

Para solucionar ese problema existen dos modelos;
 * Bloquear-Modificar-Desbloquear
 * Copiar-Modificar-Fusionar


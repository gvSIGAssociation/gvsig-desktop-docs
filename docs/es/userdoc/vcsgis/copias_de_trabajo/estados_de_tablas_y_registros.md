{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Estados de tablas y registros {% endcomment %} 


Los estados que puede presentar la copia de trabajo y las diferentes capas y tablas que los componen son las siguientes;

 * *Sin cambios y actualizado.* La tabla no se ha cambiado en la copia de trabajo y no se han confirmado cambios a esa tabla en el repositorio desde su revisión de trabajo. Una acción *commit* de esa tabla no hará nada, y una actualización de ella tampoco.

 * *Cambiado localmente y actualizado.* La tabla ha sido cambiado en la copia de trabajo y no se ha confirmado ningún cambio a esa tabla en el repositorio desde su revisión base. Hay cambios locales que no se han confirmado en el repositorio, por lo que al hacer commit la tabla se confirmaran sus cambios actualizando el repositorio. Si se procede a hacer una actualización o update de la tabla no se realizará, ya que la copia de trabajo actual posee la versión más moderna de esta presente en el repositorio.

 * *Sin cambios y desactualizado.* La tabla no ha sido cambiado en la copia de trabajo, pero ha sido cambiado en el repositorio. La tabla deberá ser actualizado en algún momento para presentar el mismo contenido que la versión del repositorio. Un comando commit sobre la tabla no hará nada, ya que no hay cambios en local y el comando actualizar o update traerá los últimos cambios del repositorio a su copia de trabajo.

 * *Cambiado localmente y desactualizado.* La tabla se ha cambiado tanto en la copia de trabajo como en el repositorio. No podrá ejecutar un *commit* sobre la tabla, ya que necesita actualizar en primera instancia la copia de trabajo con el repositorio. Para ello necesita realizar una actualización o update de la copia de trabajo que intentará fusionar los cambios del repositorio con los cambios locales. Si *VCSGis* no puede completar la fusión de una forma plausible automáticamente, le dejará al usuario la tarea de resolver los conflictos. Por último, una vez actualizado, se deberá realizar una petición commit para registrar los cambios locales en el repositorio y terminar el proceso.
 


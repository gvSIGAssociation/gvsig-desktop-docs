# Calidad

.. tip::
   Es recomendable que lea el apartado *"Inclusion de imágenes o diagramas"* del documento `Normas y recomendaciones `_

Normalmente cuando estemos capturando imágenes para la aplicación almacenaremos dos o 
tres archivos:

* Una captura de pantalla de buena calidad con una paleta de colores de 24 bits o verdadero color
  en formato PNG. Esta imagen será la imagen principal, de gran tamaño y servirá de 
  respaldo en cualquier momento.
  
* En el caso de que sea necesario, se adjuntara el archivo *ODG* de *OpenOffice Draw* con 
  la composición gráfica realizada con la imagen original de calidad. 
  El documento del Draw debe tener una página de tamaño A4 sobre la que se 
  monta la composición. 
  Para realizar la exportación a PNG se deben seleccionar los elementos de la composición 
  y exportarla. De esta forma se generará un imagen del tamaño necesario para contener el montaje.
  
* Una imagen a partir de la imagen principal o de la imagen del montaje, pero de menor calidad 
  y por lo tanto de menor peso también en formato PNG. En este caso se debe utilizar 
  una paleta de colores lo más baja posible, siempre y cuando no se produzcan pérdidas 
  significativas en la resolución. Estas imágenes son las que se insertarán en la documentación.

El utilizar archivos PNG cuya paleta de colores está optimizada se debe a que la exportación de la
documentación a formatos PDF es capaz de optimizar mucho mejor el almacenamiento de imágenes en 
paleta de colores que en color de 24 bits.

El programa que utilizamos para la captura de imágenes es Gimp_  Con él, una vez capturada 
la imágen se optimiza la paleta de colores, adecuándola al número de colores necesario para 
que la imágen no pierda calidad. El criterio es visual. Como regla puede decirse que un 
botón por ejemplo "Cancelar" se ve bien con una paleta de 8 o 16 colores y una imágen 
de 3D con mucho colorido no suele necesitar más de 64.

El menú de optimización de la paleta de colores está en Imagen -> Modo -> Indexado.

.. figure:: images/en/gimp-menu-image-mode.png
   :align: center

   Menú optimizar paleta de colores

En la ventana podemos seleccionar el número de colores que queremos y el modo de optimización.

.. figure:: images/en/gimp-dialog-indexed-color-conversion.png
   :align: center

   Ventana optimización de la paleta de colores.

Como ya se ha comentado, es recomendable dejar accesibles los 2 archivos (el de la imágen optimizada 
y el que no tiene la paleta optimizada). La razón es que si luego se quiere realizar algún 
tratamiento a la imágen, por ejemplo resaltar un área, recortarla o escalarla, ... la 
imágen con la paleta optimizada no tiene la misma calidad que la imágen que no tiene la paleta optimizada.

Como nota final, tener en cuenta que la imagen debe guardarse sin compresión.


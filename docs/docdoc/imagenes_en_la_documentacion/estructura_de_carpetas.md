# Estructura de carpetas

[iso639]: https://es.wikipedia.org/wiki/ISO_639-1


A la hora de incluir imágenes en la documentación tenderemos a estructurar las carpetas
de una de las dos siguientes formas:

* Agrupando las imágenes en una sola carpeta. Si estamos documentando una funcionalidad
  concreta, crearemos una carpeta para albergar la documentación de esa funcionalidad,
  y dentro de ella crearemos una carpeta **images** en la que dejaremos todas las
  imágenes que precise nuestra documentación (en algunos casos en la documentación
  de desarrollo **data**, ya que es común subir junto con las imágenes los archivos 
  fuentes de los modelos que se documenta) 


* Agrupando las imágenes en una carpeta por documento que creemos. 

  Normalmente las imágenes que se capturan se dejan en una carpeta 
  llamada como el documento que tiene la descripción de la funcionalidad 
  añadiendo el sufijo "img". Dentro de esta carpeta imágenes, se crea 
  una carpeta por cada idioma del que se dispongan imágenes, añadiendo 
  el sufijo indicado para el idioma de que se trate según lo especificado 
  en la [iso639][iso639].

  Ejemplo:

  ~~~
      (D) introduccion a gvSIG
          (F) introduccion a gvSIG
          (D) introduccion a gvSIG.img
              (D) es
                  (F) img1-24-es.png 
                  (F) img1-es.png 
              (D) en
                  (F) img1-24-en.png 
                  (F) img1-en.png 
      
      Nota: 
      (D) Directorio/Carpeta
      (F) Archivo
  ~~~


[Anterior](introduccion.md) | [Siguiente](nombrado.md)

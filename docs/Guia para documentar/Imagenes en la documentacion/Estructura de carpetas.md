# Estructura de carpetas

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
  el sufijo indicado para el idioma de que se trate según lo especificado en la iso639_.

  ::

    Ejemplo:

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

Sea uno u otro el caso tendremos que tener en cuenta las siguientes consideraciones:

* La carpeta donde se dejan caer las imágenes no será de tipo **carpeta
  (i18n)**.
  
* Si las imágenes han de ser dependientes del idioma, se creará una carpeta **en**, 
  **es** en la que se dejaran caer las imágenes correspondientes al idioma.
  
* La carpeta de imágenes se excluirá de la navegación (ver 
  `Cómo excluir un documento de la navegación`_ ).

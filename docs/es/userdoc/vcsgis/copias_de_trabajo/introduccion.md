{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Introducción {% endcomment %} 


A modo de recordatorio decir que el sistema de control de versiones *VCSGis* utiliza el modelo  Copia-Modificación-Fusión como modelo de versionado, por lo que utiliza **copias de trabajo**.

Una copia de trabajo en *VCSGis* está formada por una base de datos en su sistema local, la cual contiene una colección de tablas o capas que pueden ser modificados sin ningún tipo de problema. Su copia de trabajo es su área de trabajo privada y *VCSGis* nunca incorporará los cambios de otra gente, ni hará que sus cambios estén disponibles para los demás, a menos que se lo pida expresamente. Básicamente la copia de trabajo es una captura/fotografía/snapshot del repositorio en un instante concreto.

Una copia de trabajo de *VCSGis* también contiene algunas tablas extra, creados y mantenidos por *VCSGis*, para ayudar a llevar a cabo la gestión de cambios. En estos se almacenan los numero de revisión, un sistema de numeración única que identifica de manera inequívoca los diferentes cambios registrados en el repositorio. Estos códigos de revisión, únicos para cada capa o tabla, ayudan al software a reconocer qué capas o tablas contienen cambios no publicados o qué capas o tablas contienen contenidos desfasados respecto a la información del repositorio. 

{% comment %} encoding: utf-8 {% endcomment %}
{% comment %} Introducción {% endcomment %} 

Este documento presenta una introducción resumida al control de versiones **VCSGis** 
o **Version Control System Gis**. En él se tratan los conceptos generales de un 
sistema de control de versiones genérico y estos mismos en el caso concreto de *VCSGis*. 
Además, el documento pretende que tras su lectura el usuario no solo conozca las partes o  
elementos que componen este tipo de sistemas, sino que pueda utilizarlo o trabajar 
con *VCSGis*. Para llevar a cabo la segunda idea esta documentación presenta  una guía 
de uso más ejemplos básicos.

Antes de empezar a describir las partes que componen un sistema de control de versiones 
hay que definir claramente que son estos, y por tanto que es *VCSGis*. Un sistema de 
control de versiones es un programa o software basado en la centralización de información 
para compartir entre usuarios, que a diferencia de un servidor normal, guarda los cambios 
que hayan sido realizados en sus datos. Cabe destacar de nuevo que no es un servidor 
al uso que no solo almacena información, sino que almacena la información así como 
las modificaciones que los usuarios realizan sobre ella, siendo igual de importante la 
gestión de esos cambios como la propia información.

También hay que destacar que los sistemas de control de versiones no se centran en ningún 
tipo de dato en concreto, pudiendo existir sistemas que controlan archivos fuente, 
imágenes… dependiendo de la necesidad de los usuarios. En el caso de VCSGis, al estar 
orientado a un perfil técnico especializado en información geográfica, este gestiona 
información sobre tablas y capas (tablas con información geométrica). 

Sin más dilación comenzamos a detallar las diferentes partes que componen un
sistema de control de versiones tomando como ejemplo a *Version Control System Gis* (*VCSGis*).



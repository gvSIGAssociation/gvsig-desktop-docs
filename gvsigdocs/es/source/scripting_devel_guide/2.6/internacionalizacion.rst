Internacionalización
====================

Traducciones
------------

gvSIG cuenta con su gestor de traducciones. Para hacer uso de él necesitaremos que nuestro script haga una serie de pasos.

Ficheros de traducción
----------------------
Estas traducciones son una serie de cadenas con su equivalente en diferentes idiomas. Por lo general dentro del plugin se creará una carpeta /i18n/ y en ella se crearán ficheros del estilo:

- text.properties
- text_en.properties

El valor por defecto sin el identificativo del idima corresponderá al Español. Podemos crear diferentes para diferentes idiomas. El contenido de cada uno será similar el siguiente:

text.properties

Contenido::

  _Analysis=Analisis
  _Count_Duplicates_Table=Tabla conteo duplicados
  _Count_features_with_duplicates_field=Contar entidades con campos duplicados

text_en.properties

Contenido::

  _Analysis=Analysis
  _Count_Duplicates_Table=Count duplicates table
  _Count_features_with_duplicates_field=Count features with duplicates

Registro
--------
En el autorun o en la ejecución del script se deberán de agregar las traducciones creadas anteriormente. Se indicará la carpeta donde se encuentran localizadas y se ejecutaran las siguientes líneas de código::

  from org.gvsig.tools import ToolsLocator
  from java.io import File

  def main(*args):
      selfRegister()

  def selfRegister(*args):
      i18nManager = ToolsLocator.getI18nManager()
      i18nManager.addResourceFamily("text",File(gvsig.getResource(__file__,"i18n")))

Este código agregará los ficheros encontrados en la carpeta /i18n/ que comiencen por "text" al gestor de traducciones.

Utilización
-----------

Para hacer uso de las traducciones desde un script se necesitará acceder al manager de traducciones. Una vez hemos accedido al manager, se le podrá preguntar por la traducción de una cadena de caracteres específica. El manager devolverá el texto asociado a esa cadena en el idioma que esté gvSIG utilizando en ese momento::

  from org.gvsig.tools import ToolsLocator

  def main(*args):

    i18nManager = ToolsLocator.getI18nManager()
    print i18nManager.getTranslation("_Count_features_with_duplicates_field")
    print i18nManager.getTranslation("_Analysis")


Otros usos
----------

También podemos utilizar el módulo de traducción para abrir otro tipo de ficheros según el idioma de gvSIG.
En el siguiente ejemplo buscamos un archivo de ayuda para un geoproceso. En este caso, se le pregunta a gvSIG por el idioma y por los idiomas alternativos a este (idiomas parecidos) en el caso de que no existiera el primer fichero de traducción en el idioma determinado.

Existiría un script con una carpeta al lado denominada /help/ con dos ficheros xml.
- countduplicates_es.xml
- countduplicates_en.xml

Ejemplo::

  def getHelpFile(self):
      name = "countduplicates"
      extension = ".xml"
      locale = PluginsLocator.getLocaleManager().getCurrentLocale()
      tag = locale.getLanguage()
      #extension = ".properties"

      helpPath = gvsig.getResource(__file__, "help", name + "_" + tag + extension)
      if os.path.exists(helpPath):
          return File(helpPath)
      #Alternatives
      alternatives = PluginsLocator.getLocaleManager().getLocaleAlternatives(locale)
      for alt in alternatives:
          helpPath = gvsig.getResource(__file__, "help", name + "_" + alt.toLanguageTag() + extension )
          if os.path.exists(helpPath):
              return File(helpPath)
      # More Alternatives
      helpPath = gvsig.getResource(__file__, "help", name + extension)
      if os.path.exists(helpPath):
          return File(helpPath)
      return None

.. _label-handling-errors:


Gestión de errores
=================

A la hora de capturar errores, una de las recomendaciones es utilizar la siguiente estructura try/except:

  # encoding: utf-8

  import gvsig
  from java.lang import Throwable, RuntimeException
  from java.lang import Exception as JException, Error
  import sys

  def main(*args):
      print Exception
      print JException
      print Throwable
      print RuntimeException

      try:
        raise Throwable("hola")
      except :
        ex = sys.exc_info()[1]
        print "Error", ex.__class__.__name__, str(ex)

Esta estructura permite capturar los errores tanto generados en la parte de Python, como en la parte de Java. Además, en la variable "ex" nos aparecerá información suficiente para manejar y sacar información del error.


Logger
======

La forma correcta de volcar información en la consola es utilizar la función __logger__. Esta función se encuentra en la librería __gvsig_ para su uso desde Jython. Esta función tiene dos parámetros, uno el mensaje, y el otro el tipo de mensaje.

  # encoding: utf-8

  import gvsig
  from gvsig import logger
  from gvsig import LOGGER_WARN,LOGGER_INFO,LOGGER_ERROR

  def main(*args):
      logger("Proceso finalizado", LOGGER_INFO)

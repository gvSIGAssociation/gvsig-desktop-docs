
Consultas de entidades (features)
===============================
Las consultas, denominadas querys, se aplicarán a capas que dispongan de entidades (features).

getFeatureSet
------------------------

El método getFeatureSet del store de datos nos permite hacer diferentes consultas que devolverían diferentes featureSet. 
El parámetro ``expresion`` pide un String que haga de filtro, el parámetro ``sortBy`` el campo sobre el que se ordenará 
el featureSet, el parámetro ``asc`` ordenará en orden ascendente o descendente según el campo seleccionado.

Unos ejemplos de consultas y sus resultados::

  # encoding: utf-8
  import gvsig

  def main(*args):
      layer = gvsig.currentLayer()
      store = layer.getFeatureStore()
      feature = store.findFirst("")
      print "First feature:",  feature

      fs = store.getFeatureSet()
      print "Total count:", fs.getCount()
      # getFeatureSet(String filter)
      expression = "ID<4"
      fs = store.getFeatureSet(expression)
      print "Fset expression",  expression, ":",  fs.getCount()
      for i in fs: print "\t",i

      # getFeatureSet(String filter, String sortBy)
      expression = "ID<4"
      fs = store.getFeatureSet(expression, "NAME")
      print "Fset expression",  expression, ":",  fs.getCount()
      for i in fs: print "\t",i

      # getFeatureSet(String filter, String sortBy)
      expression = "ID<4 AND NAME='Feature1'"
      fs = store.getFeatureSet(expression, "NAME")
      print "Fset expression",  expression, ":",  fs.getCount()
      for i in fs: print "\t",i

      # getFeatureSet(String filter, String sortBy, boolean asc)
      fs = store.getFeatureSet("ID<4", "NAME", False)
      print "Fset expression",  expression, ":",  fs.getCount()
      for i in fs: print "\t",i

Salida por consola::

  First feature: 1, Feature1, POINT (1.0 2.0)
  Total count: 7
  Fset expression ID<4 : 3
    1, Feature1, POINT (1.0 2.0)
    2, Feature2, POINT (5.0 3.0)
    3, Feature2, POINT (3.0 3.0)
  Fset expression ID<4 : 3
    1, Feature1, POINT (1.0 2.0)
    2, Feature2, POINT (5.0 3.0)
    3, Feature2, POINT (3.0 3.0)
  Fset expression ID<4 AND NAME='Feature1' : 1
    1, Feature1, POINT (1.0 2.0)
  Fset expression ID<4 AND NAME='Feature1' : 3
    2, Feature2, POINT (5.0 3.0)
    3, Feature2, POINT (3.0 3.0)
    1, Feature1, POINT (1.0 2.0)

Otras opciones más avanzadas usando la API de gvSIG para la generación de consultas::

  import gvsig

  def main(*args):

      layer = gvsig.currentLayer() #layer_append_features.main()
      features = layer.getFeatureStore().getFeatureSet()

      print "\nShow features: "
      for f in features:
        print f
      # Query solo devuelve ciertos atributos
      fquery = layer.getDataStore().createFeatureQuery()
      fquery.addAttributeName("ID")
      fquery.addAttributeName("GEOMETRY")

      #FeatureQuery
      print "\nFQuery"
      #fquery.setLimit(3)
      fset = layer.getDataStore().getFeatureSet(fquery)
      for i in fset:
        print i

      #FeatureQueryOrder
      print "\nFquery order geometry"
      forder = layer.getDataStore().createFeatureQuery().getOrder()
      print "Tipo de query:", forder
      forder.add("GEOMETRY", True)
      fquery.setOrder(forder)

      fsetorder = layer.getDataStore().getFeatureSet(fquery)
      for i in fsetorder: print i

Uso de evaluadores
---------------------------------

Evaluadores espaciales
++++++++++++++++++++++

En el siguiente ejemplo se muestra cómo crear un evaluador espacial de intersección. Devolverá las entidades que estén dentro de un Envelope::

  # encoding: utf-8

  import gvsig
  from gvsig import geom
  from org.gvsig.fmap.mapcontext.layers.vectorial import SpatialEvaluatorsFactory

  def main(*args):
      layer = gvsig.currentLayer() #layer_append_features.main()
      store = layer.getFeatureStore()

      # http://downloads.gvsig.org/download/gvsig-desktop-testing/dists/2.4.0/docs/javadocs/html/org/gvsig/fmap/mapcontext/layers/vectorial/SpatialEvaluatorsFactory.html

      # INTERSECTS EVALUATOR
      # method intersects(Geometry geometry, IProjection projection, FeatureStore store)
      pmax = geom.createPoint2D(2,2)
      pmin = geom.createPoint2D(0,0)
      geometry = geom.createEnvelope(pointMin=pmin,pointMax=pmax)
      projection = layer.getProjection()

      sef = SpatialEvaluatorsFactory.getInstance()
      evaluator = sef.intersects( geometry, projection, store)

      # SET QUERY
      fq = store.createFeatureQuery()
      fq.addFilter(evaluator)
      fq.retrievesAllAttributes() # Fuerza el retorno de todos los atributos a traves de la query

      # FeatureSet  getFeatureSet(FeatureQuery featureQuery)
      fs = store.getFeatureSet(fq)
      print "Inside: ", geometry
      print "Feature set Count:",fs.getCount()
      for f in fs: print "\t", f

Evaluadores de expresión
++++++++++++++++++++++++

Otro tipo de evaluadores son los de expresión. Hacen referencia a consultas en las que intervienen los valores de los campos de cada entidad::

  import gvsig
  from org.gvsig.expressionevaluator import ExpressionEvaluatorLocator

  def main(*args):
      layer = gvsig.currentLayer()
      store = layer.getFeatureStore()

      # http://downloads.gvsig.org/download/gvsig-desktop-testing/dists/2.4.0/docs/javadocs/html/org/gvsig/expressionevaluator/impl/DefaultExpressionEvaluatorManager.html
      # DefaultExpressionEvaluatorManager:
      # createEvaluator(String expression)
      expression = "ID < 4"
      expressionEvaluatorManager = ExpressionEvaluatorLocator.getManager()
      evaluator = expressionEvaluatorManager.createEvaluator(expression)
      fq = store.createFeatureQuery()
      fq.addFilter(evaluator)

      # Feature set
      fs = store.getFeatureSet(fq)
      print "Feature set Count:",fs.getCount()
      for f in fs: print "\t", f

Establecer filtros a las capas
++++++++++++++++++++++++++++++

Una posibilidad de los evaluadores es filtrar las geometrías que se muestran en la Vista de una capa concreta.

Por ejemplo, podemos realizar un filtrado de entidades según una expresión. En este caso, creamos una query, donde 
le aplicamos el evaluador, y luego establecemos esta query como filtro base de la capa::

  # encoding: utf-8

  import gvsig
  from org.gvsig.fmap.dal import DALLocator

  def main(*args):
      
      layer = gvsig.currentLayer()
      store = layer.getFeatureStore()
      ## 101, 109, 344
      filter = DALLocator.getDataManager().createExpresion("ID = 1")
      fq = store.createFeatureQuery()
      fq.retrievesAllAttributes()
      fq.addAttributeName("ID")
      fq.setFilter(filter)

      layer.setBaseQuery(fq)

.. note::
   Cuidado. Esta forma de realizar filtros eliminará otros posibles filtros que tenga establecida la capa y habrá que 
   tomar medidas especificas si queremos retornar a los filtros anteriores.

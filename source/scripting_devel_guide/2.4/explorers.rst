.. _label-explorers:


Explorers
=========

Ejemplo de crear cómo crear una base de datos h2 y cargarla en una Vista.

  # encoding: utf-8

  import gvsig

  from org.gvsig.fmap.dal import DataTypes
  from org.gvsig.app import ApplicationLocator
  from org.gvsig.fmap.dal import DALLocator
  from gvsig import geom


  def main(*args):

      pathShape = gvsig.getTempFile("base", ".h2")
      print pathShape

      manager = DALLocator.getDataManager()
      ### SERVER EXPLORER
      serverParameters = manager.createServerExplorerParameters("H2Spatial")
      serverParameters.setDynValue("database_file",pathShape)
      serverExplorer = manager.openServerExplorer("H2Spatial",serverParameters)
      p = serverExplorer.getAddParameters()
      p.setDynValue("Table","t1")

      ft = manager.createFeatureType()
      ft.add("PK",DataTypes.INT)
      ft.add("ID",DataTypes.STRING)
      ft.add("DIST",DataTypes.DOUBLE)
      ft.add("SEGS",DataTypes.INT)

      ft.add("GEOMPOINT", DataTypes.GEOMETRY) #Geometry.TYPES.POINT)
      ft.get("GEOMPOINT").setGeometryType(geom.POINT, geom.D3)
      ft.get("GEOMPOINT").setSRS(gvsig.currentView().getProjection())

      ft.add("GEOMETRY", DataTypes.GEOMETRY) #Geometry.TYPES.CURVE)
      ft.get("GEOMETRY").setGeometryType(geom.LINE, geom.D3)
      ft.get("GEOMETRY").setSRS(gvsig.currentView().getProjection())
      p.setDefaultFeatureType(ft)
      serverExplorer.add("H2Spatial", p, True)

      ## OPEN STORE
      storeParameters = manager.createStoreParameters("H2Spatial")
      storeParameters.setDynValue("database_file",pathShape)
      storeParameters.setDynValue("Table","t1")
      storeParameters.setDynValue("DefaultGeometryField","GEOMETRY")
      #storeParameters.setDynValue("CRS",gvsig.currentView().getProjection())
      store = manager.openStore("H2Spatial",storeParameters)

      ## Add new layer
      application = ApplicationLocator.getManager()
      mapcontextmanager = application.getMapContextManager()
      layer = mapcontextmanager.createLayer("Layer H2",store)
      gvsig.currentView().addLayer(layer)

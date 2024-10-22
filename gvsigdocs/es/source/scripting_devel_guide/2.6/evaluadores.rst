.. _label-explorers:


Evaluadores
=========

Ejemplo de crear cómo crear evaluadores::

    # encoding: utf-8

    import gvsig
    from gvsig import geom

    def main(*args):
        layer = gvsig.currentLayer()
        store = layer.getFeatureStore()
        feature = store.findFirst("")
        print "Feature:", feature, "\n"
        
        # http://downloads.gvsig.org/download/gvsig-desktop-testing/dists/2.4.0/docs/javadocs/html/org/gvsig/fmap/mapcontext/layers/vectorial/SpatialEvaluatorsFactory.html
        #### QUERY
        fq = store.createFeatureQuery()
        
        #### EVALUATOR INTERSECTS
        # intersects(Geometry geometry, IProjection projection, FeatureStore store)
        geometry = geom.createEnvelope(pointMin=geom.createPoint2D(-74,40),pointMax=geom.createPoint2D(-73.9999,41))
        projection = layer.getProjection()
        
        from org.gvsig.fmap.mapcontext.layers.vectorial import SpatialEvaluatorsFactory
        sef = SpatialEvaluatorsFactory.getInstance()
        evaluator = sef.intersects(geometry, projection, store)

        #### SET QUERY
        fq.setFilter(evaluator)
        fq.retrievesAllAttributes()
        layer.addBaseFilter(evaluator)

        fs = store.getFeatureSet(fq)
        print fs.getCount()
        for f in fs:
            print f.getDefaultGeometry() 

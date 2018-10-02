Lenguaje R
==========

Para información sobre el uso de R, en el apartado de Talleres, hay un ejemplo desarrollado de todo lo necesario paso a paso.

Renjin
------
Ejemplo de script en R (Renjin) mostrando información de una Vista::


    import (org.gvsig.app.project.documents.view.ViewDocument)
    import (org.gvsig.app.ApplicationLocator)

    main <- function() {

        cat( "Acceso a una Vista\n" );
        application <- ApplicationLocator$getManager();

        view <- application$getActiveDocument(ViewDocument);
        print(view$name);

    }

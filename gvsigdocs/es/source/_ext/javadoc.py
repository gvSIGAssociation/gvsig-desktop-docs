# -*- coding: utf-8 -*-
"""
    sphinx.ext.javadoc
    ~~~~~~~~~~~~~~~~~~~

    Extension to save typing and prevent hard-coding of base URLs in the reST
    files.

    This adds a new config value called ``javadoc`` that is created like this::

       javadoc = {'javadoc': ('http://example.com/%s.html', prefix), ...}

    Now you can use e.g. :javadoc:`foo` in your documents.  This will create a
    link to ``http://example.com/foo.html``.  The link caption depends on the
    *prefix* value given:

    - If it is ``None``, the caption will be the full URL.
    - If it is a string (empty or not), the caption will be the prefix prepended
      to the role content.

    You can also give an explicit caption, e.g. :exmpl:`Foo <foo>`.

    :copyright: Copyright 2007-2016 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import os
from docutils import nodes, utils

import sphinx
from sphinx.util.nodes import split_explicit_title

"""
Para añadir una version nueva de javadocs:
- Dejar caer los javadocs en "gvsigdocs/javadocs/<version>/html/...."
- Modificar y ejecutar el script "gvsigdocs/build_javadoc_index"
- Añadir el import en este fichero "from javadoc<version>_index import JAVADOC_CLASSES_<version>"
- Añadir al dict JAVADOC_CLASSES la nueva entrada ""2.4" : JAVADOC_CLASSES_<version>,"
"""
from javadoc2_6_index import JAVADOC_CLASSES_2_6
from javadoc2_4_index import JAVADOC_CLASSES_2_4
from javadoc2_3_index import JAVADOC_CLASSES_2_3

JAVADOC_CLASSES = {
  "2.2" : JAVADOC_CLASSES_2_3, # Los de la 2.3 seran los mas parecidos de los que tenemos
  "2.3" : JAVADOC_CLASSES_2_3,
  "2.4" : JAVADOC_CLASSES_2_4,
  "2.6" : JAVADOC_CLASSES_2_6
}


class JavadocRole(object):
  def __init__(self, config):
    self.config = config
    self.versions = JAVADOC_CLASSES.keys()
    print("JavadocRole# versions %r" % self.versions)
    print("JavadocRole# default_version %r" % self.config["default_version"])
    
  def getVersion(self,document_path):
      if not document_path.startswith('/docs/source'):
          return None
      s1 = os.path.dirname(document_path[13:])# quitamos '/docs/source' y nos quedamos solo con el path
      for n in s1.split("/"):
          if n in self.versions:
            return n
      return self.config["default_version"]
  
  def make_url(self, document_path, javadoc_path, version):
      if not document_path.startswith('/docs/source'):
          return None
      s1 = os.path.dirname(document_path[13:]) # quitamos '/docs/source' y nos quedamos solo con el path
      x = []
      for n in s1.split("/"):
          x.insert(0,"..")
      return  ("/".join(x)) + "/../../../javadocs/"+ version+"/" + javadoc_path
      
  def __call__(self,typ, rawtext, text, lineno, inliner, options={}, content=[], **args):
    text = utils.unescape(text)
    has_explicit_title, title, part = split_explicit_title(text)
    version = self.getVersion(inliner.document.current_source)
    classname = part
    doc_path = inliner.document.current_source
    #print("JavadocRole# version %r, classname %r, path %r" % (version, classname,doc_path))
    javadoc_path = JAVADOC_CLASSES[version].get(classname,"#")
    path = self.make_url(doc_path,javadoc_path, version)
    if path is None:
      path = "#"
    if not has_explicit_title:
        title = path
        #title = part
    pnode = nodes.reference(title, title, internal=False, refuri=path)
    return [pnode], []


def setup_link_roles(app):
    app.add_role("javadoc", JavadocRole(app.config.javadoc))

def setup(app):
    app.add_config_value('javadoc', {}, 'env')
    app.connect('builder-inited', setup_link_roles)
    return {'version': sphinx.__version__, 'parallel_read_safe': True}

print ("javadoc plugin loaded")


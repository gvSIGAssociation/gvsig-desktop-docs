# encoding: utf-8

import gvsig
from gvsig import getResource

import os
import shutil
import stat
from os.path import join


def extract_section(tmpfolder, section, version, lang="es",include_javadocs = True, docrev="1.0"):
  source = getResource(__file__,lang)
  javadoc_src = getResource(__file__,"javadocs")

  targetname = "gvsig-%s-%s-%s-%s" % (version, section, lang, docrev)
  target = join(tmpfolder,targetname)
  
  if os.path.exists(target):
    print "Borrando carpeta %s..." % target
    shutil.rmtree(target)
    
  os.makedirs(join(target,"es", "source",section))

  print "Copiando %s..." % join("source",section,version) 
  shutil.copytree(join(source,"source",section,version), join(target,"es","source",section,version))

  for folder in ("make.bat", "Makefile"):
    print "Copiando %s..." % folder
    src = join(source, folder)
    dst = join(target, "es", folder)
    if os.path.isdir(src):
      shutil.copytree(src, dst)
    else:
      shutil.copyfile(src, dst)
  
  for folder in ("_config", "_ext", "_static", "_templates","conf.py", "gvsigsearch_all.rst", "gvsigsearch_logo.svg", "index.rst", "links.rst"):
    print "Copiando %s..." % folder
    src = join(source, "source",folder)
    dst = join(target, "es", "source",folder)
    if os.path.isdir(src):
      shutil.copytree(src, dst)
    else:
      shutil.copyfile(src, dst)
   
  print "Copiando index.rst..."
  shutil.copyfile(join(source,"source",section,version,"index_standalone.rst"), join(target,"es", "source","index.rst")) 

  if include_javadocs :
    os.makedirs(join(target,"javadocs", version))
    print "Copiando javadocs..."
    shutil.copytree(join(javadoc_src,version,"html"), join(target,"javadocs", version,"html")) 

  print "Generando build.sh..."
  f = open(join(target,"build.sh"), "w")
  f.write("""
set -e
cd "%s"
echo "Generando htmls..."
docker run --rm -v "$PWD:/docs" sphinxdoc/sphinx make clean html
echo "Borrando archivos fuente..."
#rm -r source make.bat Makefile
cd ..
echo "Comprimiendo archivos..."
zip -r9 "../%s.zip" . -x "source/*" make.bat Makefile
echo "Copiarndo archivo comprimido a ScriptingComposerTools/javadocviewer/data..."
cp "%s.zip" "%s"
echo " 
Recuerde actualizar la funcion 'actionPerformed' de ScriptingComposerTools/javadocviewer/actions con algo como:

  navigator.getBookmarksPanel().addDocument(
      'gvSIG %s', 
      'jar:file:' + getResource(__file__, 'data','%s.zip!/es/build/html/index.html'), 
      persistent=False
    ) "
  """ % (
      join(target,"es"),
      targetname,
      target,
      os.path.realpath(getResource(__file__, "../../ScriptingComposerTools/javadocviewer/data")),
      section,
      targetname
    )
  )
  f.close()
  os.chmod(join(target,"build.sh"), 0777) #stat.S_IEXEC or stat.S_IXURS or stat.S_IXGRP)
  print "\nEjecute el build.sh para generar el zip con la documentacion e instalarlo en el composer"


def main(*args):
  extract_section(
    tmpfolder = "/home/jjdelcerro/Descargas/gvsigdoc", 
    section = "scripting_devel_guide", 
    version = "2.6", 
    lang="es",
    include_javadocs = True
  )

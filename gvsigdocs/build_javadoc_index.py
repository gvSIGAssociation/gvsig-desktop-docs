# encoding: utf-8

import gvsig
from gvsig import getResource

from StringIO import StringIO
import os

def build_index(javadoc_version):
    init_path = getResource(__file__,"javadocs/"+javadoc_version+"/html")
    dic = dict()
    doc_path_web = "html"
    
    for (path, ficheros, archvs) in os.walk(init_path):
        for a in archvs:
            if not a.endswith(".html"):
                continue
            #key
            javaclass_key = os.path.splitext(a)[0]
            if javaclass_key in dic.keys():
                continue
            #value
            full_path = os.path.join(path, a)
            rel_path = os.path.relpath(full_path, init_path)
            docs_path = os.path.join(doc_path_web, rel_path)
            dic[javaclass_key] = docs_path
    return dic

def write_index(index, version):
  s = StringIO()
  s.write("# encoding: utf-8\n\n\nJAVADOC_CLASSES_%s = {\n" % (version.replace(".","_")))
  first = True
  for k,v in index.items():
    if first:
      first = False
    else:
      s.write(",\n")
    s.write("  ")
    s.write(repr(k))
    s.write(" : ")
    s.write(repr(v))
  s.write("\n}\n\n\n")
  pathname = getResource(__file__,("es/source/_ext/javadoc%s_index.py" % (version.replace(".","_"))) )
  f = open(pathname,"w")
  f.write(s.getvalue())
  f.close()

def main(*args):
  index = build_index("2.3")
  write_index(index, "2.3")

  index = build_index("2.4")
  write_index(index, "2.4")
  
  index = build_index("2.6")
  write_index(index, "2.6")
  

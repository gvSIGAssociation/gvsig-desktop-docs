<?xml version='1.0' encoding='ISO-8859-1' ?>
<!DOCTYPE helpset
  PUBLIC "-//Sun Microsystems Inc.//DTD JavaHelp HelpSet Version 1.0//EN"
 		  "http://java.sun.com/products/javahelp/helpset_1_0.dtd">

<?TestTarget this is data for the test target ?>

<helpset version="1.0">

  <!-- title -->
  <title>Scripting documentation</title>

  <!-- maps -->
  <maps>
     <homeID>main</homeID>
     <mapref location="api.jhm"/>
  </maps>

  <!-- views -->
  <view>
    <name>TOC</name>
    <label>TOC</label>
    <type>javax.help.TOCView</type>
    <data>toc.xml</data>
  </view>
  <view>
    <name>Search</name>
    <label>Search</label>
    <type>javax.help.SearchView</type>
    <data engine="com.sun.java.help.search.DefaultSearchEngine">JavaHelpSearch</data>
  </view>
  <view>
    <name>Favorites</name>
    <label>Favoritos</label>
    <type>javax.help.FavoritesView</type>
  </view>

  <presentation default="true" displayviewimages="false">
     <name>main window</name>
     <size width="700" height="400" />
     <location x="200" y="200" />
     <title>gvSIG - Ayuda en linea</title>
     <image>toplevelfolder</image>
     <toolbar>
       <helpaction image="action.back">javax.help.BackAction</helpaction>
       <helpaction image="action.forward">javax.help.ForwardAction</helpaction>
     </toolbar>
  </presentation>
</helpset>

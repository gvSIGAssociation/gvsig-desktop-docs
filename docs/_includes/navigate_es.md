<table style="width:100%;">
 <tr>
  {% if include.prev %}
    <td><a href="{{ include.prev }}">Anterior</a></td>
  {% endif %}
  {% if include.index == ".." %}
    <td><a href="{{ include.index }}">Subir un nivel</a></td>
  {% endif %}
  {% if include.index and include.index != ".." %}
    <td><a href="{{ include.index }}">Indice</a></td>
  {% endif %}
  {% if include.next %}
    <td><a href="{{ include.next }}">Siguiente</a></td>
  {% endif %}
  <td style="width:100%;"></td>
  {% if include.source %}
    <td><a href="{{ include.source }}">Fuente</a></td>
  {% endif %}
 </tr>
</table>

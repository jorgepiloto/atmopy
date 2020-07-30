API Reference
=============

This page holds atmopy's API documentation, which might be useful for final
users and developers to build their custom tools or programs based on the atmopy
library.

Main philosophy behind this package is to collect every atmospheric model within
a sub-package and make use of the different name-space created.

.. toctree::
   :maxdepth: 5

   {% for page in pages %}
   {% if page.top_level_object and page.display %}
   {{ page.include_path }}
   {% endif %}
   {% endfor %}

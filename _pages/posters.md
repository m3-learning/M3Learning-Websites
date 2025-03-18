---
layout: page
title: Posters
permalink: /posters/
---

# Research Posters 📜

Here is a collection of research posters presented at various conferences and workshops.

{% for poster in site.data.posters %}
  - **{{ poster.title }}**  
    *Presented at {{ poster.venue }}, {{ poster.year }}*  
    [Download (PDF)]({{ poster.pdf }})  
    {% if poster.image %}
    ![Poster preview]({{ poster.image }}){: .img-responsive}
    {% endif %}
    <br>
{% endfor %}
{% extends 'display_priority.tpl' %}
{%- block header -%}
---
title: "{{ resources['metadata']['name'] }}"
output: html_notebook
---
{% endblock header %}

{%- block in_prompt -%}
{%- endblock in_prompt -%}

{%- block output_prompt -%}
{%- endblock output_prompt %}

{%- block input -%}
{% if not cell.metadata.get('notshow') %}
```{r}
{{ cell.source}}
```
{% endif %}
{%- endblock input -%}

{% block error %}
{% endblock error %}

{% block traceback_line %}
{% endblock traceback_line %}

{% block execute_result %}
{% block data_priority scoped %}
{% endblock %}
{% endblock execute_result %}

{% block stream %}
{% endblock stream %}

{% block data_svg %}
{% endblock data_svg %}

{% block data_png %}
{% endblock data_png %}

{% block data_jpg %}
{% endblock data_jpg %}

{% block data_latex %}
{% endblock data_latex %}

{% block data_html scoped %}
{% endblock data_html %}

{% block data_markdown scoped %}
{% endblock data_markdown %}

{% block data_text scoped %}
{% endblock data_text %}

{% block markdowncell scoped %}
{{ cell.source }}
{% endblock markdowncell %}

{% block unknowncell scoped %}
unknown type  {{ cell.type }}
{% endblock unknowncell %}
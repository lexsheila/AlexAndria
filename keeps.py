{% extends 'base.html' %} 
{% block head_title %}Viewing category {{ category.title }}{% endblock %}
{% block title %}{{ category.title }}{% endblock %}

{% block content %}
    {% if categorys %}
        <ul>
        {% for category in categorys %}
            <li><a href="{{ category.get_absolute_url }}">{{ category.title }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>There are no categories.</p>
    {% endif %}
{% endblock %}
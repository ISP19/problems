# Answer to a custom template filters  

[poll_extras.py](django/polls/templatetags/poll_extras.py)
``` python
from django import template

register = template.Library()


@register.filter
def latest_question(questions):
    """ Return 5 latest questions by using custom template filter"""
    return questions.order_by('-pub_date')[:5]

```
 
[index.html](django/polls/templates/polls/index.html)
``` html
<html>
<body>
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
{% load poll_extras %}

{% if questions %}
    <ul>
    {% for question in questions|latest_question %}
        <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}

</body>
</html>

```
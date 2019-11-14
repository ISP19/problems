# Basic Custom Template Filters

In Django polls tutorial if you want to show latest questions.
You can filtters latest questions by using Django custom template filters.  
```
django
    mysite
    polls
        migrations
        templates
            polls
                index.html
                detail.html
        templatetags
            __init__.py
            poll_extras.py
        admin.py
        apps.py
        models.py
        urls.py
        views.py
    manage.py
```
```models.py```  
``` python3
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # code omitted


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

```

```views.py```
``` python3
from .models import Question
from django.shortcuts import render

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/index.html', context)
```

```index.html```  
``` html
<html>
<body>
{% if questions %}
    <ul>
    {% for question in questions|latest_question %}
        <li>
            <a href="{% url 'polls:detail' question.id %}">
                {{ question.question_text }}
            </a>
        </li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
</body>
</html>
```  

## Question
Create custom template tags or filters that return 5 latest questions in poll_extras.py.  

## Useful references
- [Custom template tags and filters](https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/)
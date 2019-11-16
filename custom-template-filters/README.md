# Basic Custom Template Filters

The Django polls tutorial has several ways to show the latest questions.
One way that the tutorial does not mention is using custom template tags and filters, which is useful magic of Django that you can create your tamplate tags or filters for use in your project.   

## Question
Create custom template tags or filters that return 5 latest questions in poll_extras.py.  

> You can be using the starter template or just read the code below.   
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

[models.py](starter/polls/models.py)
``` python
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

[views.py](starter/polls/views.py)
``` python
from .models import Question
from django.shortcuts import render

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/index.html', context)
```  

[poll_extras.py](starter/polls/templatetags/poll_extras.py)
``` python
from django import template

register = template.Library()


# Write your code below

```  

[index.html](starter/polls/templates/polls/index.html)  
``` html
<html>
<body>
{% if questions %}
    <ul>
    <!-- Write the code that display 5 latest question below -->
    <!-- Using Django custom template tags or filters -->
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
</body>
</html>
```  

## Answer
> Try to do it by your self before check your answer [here](answer/README.md).

## Useful references
- [Custom template tags and filters](https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/)
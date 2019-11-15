## Django models tip
---
In django tutorial part 2 (https://docs.djangoproject.com/en/2.2/intro/tutorial02/#creating-models), in the foreignkey, if we want to get, create or access the choice objects from the question we need the keyword `choice_set`.
For example
```
>>> Question.objects.get(pk=1)
<Question: What's up?>
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3
```
If we do not want to use the keyword `choice_set`,but we whant to use the word `choices` intead, what part should be edited?

models.py

```
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

<details><summary>Answer</summary>

```
class Choice(models.Model):
    question = models.ForeignKey(Question,related_name="choice", on_delete=models.CASCADE)
```

adding the kwarg `related_name` in the ForeignKey parameter
### The benefit of using related_name
---
The related_name allows you to specify a simpler or more legible name to get the reverse relation. 
</details>

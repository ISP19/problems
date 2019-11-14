## Matching Django-related question and answers.
### Question
Match the letters to the correct sentence or question.

```sh
1. This file is for redirecting webpages and rendering webpages from request. (Could be a normal function or a class based)
__
2. User needs to put their desire address of the website using 'path' function in this bracket([]) named:
__
3. To put web html templates, user needs to first create a folder named template, then create folder named "something" inside the template folder to make django reads html file properly.
__
4. This built-in django accepts (at least) these 3 arguments: request, "/*.html/", context. What is the name of it and how to import it from?
__
5. When testing the database, user should use python3 manage.py shell, then type WHAT?
__
6. With your html templates, to use the picture within the folder, you need {% "something here" %} to be able to recall the file within that location.
__
```

### Choices
```sh
A. from "yourappname".models import *
B. urls.py
C. from django.shortcuts import render
D. Name of your app.
E. urlspatterns
F. static
G. from django.http import HttpResponse
H. views.py
I. from django.db import models
J. templates
K. django-templates

```
### Answer
1. H
2. E
3. D
4. C
5. A
6. F

**References**
- [Django Urls](https://docs.djangoproject.com/en/2.2/ref/urls/)
- [Writing Views](https://docs.djangoproject.com/en/2.2/topics/http/views/)
- [Django Render](https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/#render)
- [Templates](https://docs.djangoproject.com/en/2.2/topics/templates/)
- [Polls App: Tutorial 1](https://docs.djangoproject.com/en/1.7/intro/tutorial01/)
- [Templates Static](https://docs.djangoproject.com/en/2.2/howto/static-files/)

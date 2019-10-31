# DRY- principle

```
Don't repeat yourself (DRY, or sometimes do not repeat yourself) is a principle of software development aimed at reducing repetition of software patterns, replacing it with abstractions or using data normalization to avoid redundancy.

```

from [Wiki](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

see the files in `./template` in Django. you might see your files containing same thing in `header` and `footer`

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>AwesomeProjectName</title>
    <!-- custom CSS -->
    <link rel="stylesheet" href="{% static 'awesomeApp/style.css' %}" />
  </head>

  <body>
    =========== PAGE CONTENT ===========
    =======  for X pages you have ======
    <!-- Jquery -->
    <script
      src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
      integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

as you can see, we might have a lot of importing from Bootstrap, Jquery, Popper.js, CSS and this applied to ALL pages.

# Question

1. how can you apply DRY principle to Django templates so that we don't have to repeat typing import for every pages?

# Answer

- use `Django template extending` by creating base.html for content to be built on.


`base.html`

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>AwesomeApp</title>
    <!-- custom CSS -->
    <link rel="stylesheet" href="{% static 'awesomeApp/style.css' %}" />
  </head>

  <body>
    {% block content %}
    {% endblock %}

    <!-- Jquery -->
    <script
      src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
      integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

`awesomePage.html`

```html
{% extends 'AwesomeApp/base.html' %}

{% block content %}
<h1>awesome World!</h1>
{% endblock %}
```

`indexPage.html`

```html
{% extends 'AwesomeApp/base.html' %}

{% block content %}
<h1>index World!</h1>
{% endblock %}
```

`registerPage.html`

```html
{% extends 'AwesomeApp/base.html' %}

{% block content %}
<h1>register World!</h1>
{% endblock %}
```
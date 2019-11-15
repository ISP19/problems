# DRY Principle

> Don't repeat yourself (DRY) is a principle of software development aimed at reducing repetition of software patterns, replacing them with
> abstractions or data normalization to avoid redundancy.


from [Wikipedia](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

If you look at the files in your Django `./templates` directory, 
you may see many files containing the same `header` and `footer`:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <!--  In EVERY PAGE your have this header -->
  <head>
    <meta charset="utf-8" />
    <title>AwesomeProjectName</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" 
     href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css"
    />
    <!-- custom CSS -->
    <link rel="stylesheet" href="{% static 'awesomeApp/style.css' %}" />
  </head>

  <body>
    ======= Your PAGE CONTENT ==========
    =======      Here         ==========

    <!--  In EVERY PAGE your have this footer -->
    <!-- Jquery -->
    <script
      src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
      integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
      crossorigin="anonymous"
    ></script>
    <!-- Bootstrap -->
    <script 
      src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js">
    </script>
    
  </body>
</html>
```

The above page has a lot of imports for CSS, Bootstrap, Jquery, and others that need to be included in **every** page.

That's duplicate code.

# Question

How can you apply the DRY principle to Django templates so that we don't have to repeat the same imports and same styling in every page?

# Answer

- Use ***Django template extension*** by creating a `base.html` base page for other pages to on.
- Each html template "*extends*" the base template and adds custom content in pre-defined "*blocks*".


File `base.html` defines a "base" page with the content and styling you want to repeat:
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

Other pages "extend" the base template and insert custom content in "blocks".

File `awesomePage.html`:

```html
{% extends 'AwesomeApp/base.html' %}

{% block content %}
<h1>Awesome World!</h1>

The body of the page goes here.
{% endblock %}
```

File `indexPage.html`:

```html
{% extends 'AwesomeApp/base.html' %}

{% block content %}
<h6>Index World!</h6>

The body of index page goes here.
{% endblock %}
```

File `registerPage.html`:

```html
{% extends 'AwesomeApp/base.html' %}

{% block content %}
<p>Register World!</p>

Register yourself:
<form method='POST'>
<table>
{{form.as_t}}
</table>
{% endblock %}
```

Benefits:

* The pages are a lot cleaner, shorter, and more focused
* The result will have a uniform appearance since they all you the same styling
* Its easy to change page styling because you only need to change it once, in `base.html`

## References

* [Django Templates](https://docs.djangoproject.com/en/2.2/topics/templates/) in Django official docs.
* [Template Extending](https://tutorial.djangogirls.org/en/template_extending/) in the Django Girls tutorial.
* [Don't Repeat Yourself - Understanding Django Template Inheritance](https://consideratecode.com/2018/04/17/django-template-inheritance/) good article on ConsiderateCode.com. Example copies the Django tutorial but adds more explanation of template extension.

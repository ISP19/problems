# Security in Django

> A Django application without security concern is like a zoned house with unlocked doors.

An interesting topic which has not been elaborately covered in the class is all about security in Django. 

One good site which provides popular security vulnerabilities is [OWASP](https://www.owasp.org/index.php/Main_Page), short for Open Web Application Security Project. **OWASP** is an online website from a non-profit organisation which generally provides freely available documentation—most popular ones are its yearly top 10's—in the field of **web application security**.

## Question

Given a scenario based on the real implementation when a developer wanted to bring in client-side reactive components into his web application using [Vue.js](https://vuejs.org/) for creating a Facebook clone. He decided to directly inject data into an HTML template of the application, seeing that it would result in less round trip time during rendering a web page instead of another Ajax request to fetch the data.

Then he wrote an HTML template which partially contains the `script` tag as follows.

_The first Django (Jinja2) template:_

```jinja
<script type="application/javascript">
  app = new Vue({
    el: '#app',
    data: {
      showModal: false,
      currentPost: {
        body: ''
      },
      posts: [
        {% for user_post in user_posts %}
            {{ user_post.as_json | safe }},
        {% endfor %}
       ],
      }
  })
</script>
```

In addition, he provided another template to enable users of his application to submit their posts in a separate page using a Django form with [`widget-tweaks`](https://pypi.org/project/django-widget-tweaks/) template extension. He preliminarily wrote the template as follows.

_The second template:_

```jinja
<form method="post" class="box" @submit.prevent="createPost()">
  <label for="post-body">What's on your mind?</label>
  {{ form.body|attr:"v-model: currentPost.body"|add_class:'textarea' }}
   {# This will be translated into a textarea input field #}
  <div class="buttons">
    <button type="submit" class="button is-primary is-medium">Post</button>
  </div>
</form>
```

This seems to be a solution to integrate a Django app with a client-side JavaScript framework, yet it poses security vulnerabilities.

To what vulnerabilities can the application be possibly prone according to the given OWASP's top 10 list and how can you mitigate those issues? (*You can either provide a improved template or a brief explanation of your solution.*)

**Hint**: Preliminarily, there are two of them.

## Answer
Think about this question for a moment before getting into an answer.

### **Spoiler alert**
> [Click here](answer/README.md) to get an answer.

## Useful references:

- Django official site
  - Security in Django - [Read me](https://docs.djangoproject.com/en/2.2/topics/security/)
  - Built-in template tags and filters - [Read me](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/)
  - Working with forms - [Read me](https://docs.djangoproject.com/en/2.2/topics/forms/)
  
- (OWASP) Top 10 list of security vulnerabilities in 2017 - [Read me](https://www.owasp.org/index.php/Top_10-2017_Top_10)

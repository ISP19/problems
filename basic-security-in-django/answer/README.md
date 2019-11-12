## Answer to a basic Security in Django question
> Note: There might be more problems in the category.

In the given problem, it seems there are two possible vulnerabilities: CSRF and XSS.

### Cross site request forgery (CSRF)

From the second template of which HTML code is

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

Fortunately, Django **would not let this happen** in the first place as it already covers the protection against the possible attack; nevertheless, it is noticeable that he forgot to include the tag `{% csrf_token %}`. This would possibly result in Django **CSRF token missing** error beforehand.

#### Solution

Simply include `{% csrf_token %}` in the `form` section and let Django take care of the rest.


### Cross site scripting (XSS)

According to the first template of which HTML code is

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

He was using the `safe` filter which was bypassing Django built-in HTML escape functionality, opening up possibilities for malicious user inputs; for instance, a user enters another `script` tag in his post during post creation, and the application will then display some odd behaviour.

Even worse, an attacker can execute a client-side script to steal sensitive user data (such as **cookies**) across sites or even attempt to **hijack** the user's session.

#### Mitigation

- Be extra careful when using `safe` filter, `is_safe`, and `mark_safe` function, **do validate** and sanitise user inputs before saving to a database. 
- Instead, split the notorious in-line `script` tag into a separate JS file, refer to it using `src` attribute, and consume the data from Ajax requests.
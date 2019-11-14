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

Fortunately, Django **would not let this happen** in the first place as it already covers protection against this attack; nevertheless, it is noticeable that he forgot to include the tag `{% csrf_token %}`. This would possibly result in Django **CSRF token missing** error beforehand.

#### Solution

Simply include `{% csrf_token %}` in the `form` section and let Django take care of the rest.



### Cross site scripting (XSS)

To comprehend this topic, let me introduce you what JavaScript injection is.

#### JavaScript injection
JavaScript injection is a technique that a malicious user or an attacker exploits the client-side script behaviour, namely JavaScript. This technique can be performed in various scenarios, ranging from ruining look and feel of a website to impersonating a user of the site, which can eventually result in XSS.

In the impersonation case, the script can look like the following extract.

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
        { body: 'Just a post' },
        { body: '<script>
                function getCookie(name) {
                  const re = new RegExp(name + "=([^;]+)");
                  const value = re.exec(document.cookie);
                  return value != null ? unescape(value[1]) : null;
                }
                const sessionId = getCookie('SESSION_ID');
                stealCookieAndSendItToMyHarmfulSite(sessionId);
                </script>' }
       ],
      }
  })
</script>
```

#### Explanation of the answer

According to the first template of which HTML code is,

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

He was using the `safe` filter which bypasses Django built-in HTML escape functionality, opening up possibilities for malicious user inputs; for instance, a user enters another `script` tag in his post during post creation, and the application will then display some odd behaviour.

Even worse, an attacker can execute a client-side script to steal sensitive user data (such as **cookies**) across sites or even attempt to **hijack** the user's session;
however, this is not __the case__ as __Django__ had released security patches since `version 2`, including this one—session cookies with `httpOnly` header. 

Conversely, it can be the case when you settle on a lower-level web framework that needs extra implementation.




#### Mitigation

- Be extra careful when using `safe` filter, `is_safe`, and `mark_safe` function; **do validate** and sanitise user inputs before saving to a database. 
- Instead, split the notorious in-line `script` tag into a separate JS file, refer to it using `src` attribute, and consume the data from Ajax requests.
- Since Django (currently `2.2`) stores session cookies with `httpOnly` header set by default, this helps prevent a browser JavaScript from interfering with site cookies.
  
  Still, this doesn't prevent targeted attackers from other techniques. (e.g. directly browsing browser developer tools, DOM-based XSS, or exploiting a browser)

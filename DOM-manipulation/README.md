# DOM Manipulation

- The Document Object Model (DOM) is a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects. That way, programming languages can connect to the page.

- A Web page is a document. This document can be either displayed in the browser window or as the HTML source. But it is the same document in both cases. The Document Object Model (DOM) represents that same document so it can be manipulated. The DOM is an object-oriented representation of the web page, which can be modified with a scripting language such as JavaScript.

# Question
- Using DOM to write a javascript method, how will you use it to change the string “ISP” text color randomly between intervals time.(eg. Changing text color between red and green around 1.5s)
## **HTML**
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="css/style.css">
    <title>Jade</title>
</head>

<body class="vsc-initialized">
    <div class="container" id="headText">
        <h1>ISP</h1>
    </div>

    <div class="container secondary"></div>
    <script src="js/answer.js"></script>
</body>

</html>
```
## **CSS**
```css
@import url('https://fonts.googleapis.com/css?family=Fira+Sans+Condensed|Nanum+Pen+Script&display=swap');

* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Fira Sans Condensed', sans-serif;
    width: 100%;
    height: 100vh;
    background-color: black;
}

div {
    text-align: center;

}

h1 {
    font-size: 100px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
```

## **JS**
```
#TODO: Finish up this javascript code section
```

<details>
<summary>ANSWER</summary>

### This is just only my method to do this question
```javascript
var colors = ["red", "green"]
var current = 0
var myText = document.querySelectorAll("#headText h1");

function changeTextcolor() {
    --current
    if (current < 0) current = colors.length - 1
    for (var i = 0; i < myText.length; i++) {
        myText[i].style.color = colors[(current + i) % colors.length]
    }
}
setInterval(changeTextcolor, 1000)
```
</details>
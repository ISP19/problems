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
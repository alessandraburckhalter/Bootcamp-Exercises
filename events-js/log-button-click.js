const button1 = document.getElementById("button");
button1.onclick = function() {
    alert("Button Pressed")
}

button1.addEventListener('blur', function(event) {
    alert("You Left Clicked")
})

window.addEventListener('resize', function(){
    alert("You Change the size of the Window!");
})

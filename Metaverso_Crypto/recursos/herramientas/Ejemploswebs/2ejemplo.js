function greet(name) {
	alert("Hello, " + name + "!");
}

var button = document.getElementById("myButton");
button.addEventListener("click", function() {
	greet("John");
});

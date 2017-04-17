function text()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	var pic = new Image();
	pic.src = "http://sugarglidercare.org/wp-content/uploads/2010/02/sugar-glider-1.jpg"
	
	pic.addEventListener("load", function() { canvas.drawImage(pic, 0, 0, 200, 150);}, false)
}

window.addEventListener("load", text, false);
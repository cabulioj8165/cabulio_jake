function mouse()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	window.addEventListener("mousemove", icon, false);
}

function icon(g) {
	

	
	canvas.clearRect(0, 0, 2000, 900);
	var xPos = g.clientX;
	var yPos = g.clientY;
	var pic = new Image();
	pic.src = "wtb0516r-1.jpg"
	canvas.drawImage(pic, xPos-100, yPos-100, 200, 200)
}

window.addEventListener("load", mouse, false);
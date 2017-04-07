function shapes()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	var g = canvas.createLinearGradient(0, 0, 600, 400);
	g.addColorStop(0, "green");
	g.addColorStop(.5, "orange");
	canvas.strokeStyle = "purple";
	canvas.fillStyle = g;
	canvas.beginPath();
	canvas.moveTo(150, 200);
	canvas.lineTo(175, 250);
	canvas.lineTo(220, 225);
	canvas.lineTo(195, 270);
	canvas.lineTo(240, 280);
	canvas.lineTo(194, 295);
	/*4th*/canvas.lineTo(220, 335);
	/*4th*/canvas.lineTo(175, 310);
	canvas.lineTo(150, 350);
	canvas.lineTo(130, 310);
	canvas.lineTo(90, 335);
	canvas.lineTo(110, 295);
	canvas.lineTo(75, 280);
	canvas.lineTo(115, 270);
	canvas.lineTo(90, 225);
	canvas.lineTo(130, 250);
	canvas.lineTo(150, 200);
	canvas.closePath();
	canvas.fill();
	canvas.stroke();

}

window.addEventListener("load", shapes, false);
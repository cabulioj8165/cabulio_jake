function shapes()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	var g = canvas.createLinearGradient(0, 0, 600, 400);
	g.addColorStop(0, "green");
	g.addColorStop(.6, "orange");
	canvas.strokeStyle = "purple";
	canvas.fillStyle = g;
	canvas.beginPath();
	/*1st*/canvas.moveTo(150, 200);
	/*1st*/canvas.lineTo(170, 250);
	/*2nd*/canvas.lineTo(210, 225);
	/*2nd*/canvas.lineTo(185, 270);
	/*3rd*/canvas.lineTo(225, 280);
	/*3rd*/canvas.lineTo(194, 295);
	/*4th*/canvas.lineTo(215, 335);
	/*4th*/canvas.lineTo(170, 310);
	/*5th*/canvas.lineTo(150, 350);
	/*5th*/canvas.lineTo(130, 310);
	/*6th*/canvas.lineTo(90, 335);
	/*6th*/canvas.lineTo(110, 295);
	/*7th*/canvas.lineTo(75, 280);
	/*7th*/canvas.lineTo(115, 270);
	/*8th*/canvas.lineTo(90, 225);
	/*8th*/canvas.lineTo(130, 250);
	canvas.closePath();
	canvas.fill();
	canvas.stroke();

}

window.addEventListener("load", shapes, false);
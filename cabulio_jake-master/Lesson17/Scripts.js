function drag() {
	basketball = document.getElementById("basketball");
	leftbox = document.getElementById("leftBox");
	
	basketball.addEventListener("dragstart", startDrag, false);
	basketball.addEventListener("dragend", endDrag, false);
	
	leftbox.addEventListener("dragenter", dragEnter, false);
	leftbox.addEventListener("dragleave", dragLeave, false);
	leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
	leftbox.addEventListener("drop", drop, false);
}

function startDrag(e) {
	var pic = '<img id = "basketball" src = "basketball.png">';
	e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e) {
	e.preventDefault();
	leftbox.style.background = "#fff83d";
	leftbox.style.border = "3px solid #f25252";
}

function dragLeave(e) {
	e.preventDefault();
	leftbox.style.background = "white";
	leftbox.style.border = "3px solid #4c3fff";
}

function drop(e) {
	e.preventDefault();
	leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e) {
	pic = e.target
	pic.style.visibility = "hidden";
}

window.addEventListener("load", drag, false);
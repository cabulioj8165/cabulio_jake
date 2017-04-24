function validate() {
	var x = document.forms.input.username.value;
	var atPos = x.indexOf("@");
	var dotPos = x.lastIndexOf(".");
		
	
	if(atPos < 1 || dotPos < atPos+2 || dotPos + 2 > x.length)
		return(false);
			
	else
		return(true);
}

function validatepw() {

	var y = document.forms.input.passwd.value;
	
	if(y.length < 6)
		return(false);
	
	else
		return(true);
}

function confirminfo() {
	var x = validate();
	var y = validatepw();
	
	if (x == false)
		if (y == false)
			alert("You did not provide a valid email address!(Your password does not meet the minimum requirements)");
	else
		if (y = true)
			alert("This is not a valid email!");
	if (x == true)
		if (y == false)
			alert("Password must be at least 6 characters!")
	else
		if (y == true)
			alert("Success!");
	
}
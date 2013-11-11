function readFile(evt) {
	//Returns the contents of the specified file
	var fileHandle = evt.target.files[0]; 

	if (fileHandle) {
	  //proceed with read…
	  var r = new FileReader();
	  var text;
	  r.onload = function(e) {
		  var contents = e.target.result;
		  document.getElementById('fileContents').value = contents;
	  }
	  r.readAsText(fileHandle);
	}
	else {
		alert ("file opening failed!");
		//go with textbox?
}
return "";
}

document.getElementById('inputByFile').addEventListener('change', readFile, false);
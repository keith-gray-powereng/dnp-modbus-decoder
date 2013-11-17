/*Content:  JS file
	Focus:  Take in a file name and path as input and store the file's
			contents to our hidden element, fileContents.
	Source: Most of the code used here was heavily influenced by
			the following site: http://www.htmlgoodies.com/beyond/javascript/read-text-files-using-the-javascript-filereader.html#fbid=9k2XR0DAity
 */
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
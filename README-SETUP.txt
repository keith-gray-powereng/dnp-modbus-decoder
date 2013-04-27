Hello, this is a read me file for using Power Decoder prototype for the computer science course CS:425: Senior Design.
In order to use the prototype you will need the following items:
The client has these already installed on their computers.

//A walkthrough for installing distribute and pip, https://zignar.net/2012/06/17/install-python-on-windows/
install each portion in this order:

Distribute    		 Required to install Pip	https://pypi.python.org/pypi/distribute/0.6.27#installation-instructions

Python 3.2    		 The underlying code													http://www.python.org/download/

Pip 1.3-1.4,    	 You will need to install bitstring using the pip install command		https://raw.github.com/pypa/pip/master/contrib/get-pip.py

Django 1.5,			 The webpage generator													https://www.djangoproject.com/download/											

bitstring 3.1.2		either use "pip install bitstring" or download at:	http://pythonhosted.org/bitstring/index.html?highlight=version#download


Once these are installed, you can launch the batch files to execute the website.

The batch file to launch the website is under dnp-modbus-decoder/source code/PowerDecoder/Django Webpage/RunSite.bat

python and the python scripts folder must be PATH 'd in order to work.

Once the website is executed, click on DNP3, then the decoder button, and then the webpage will execute the
underlying parser python code.  


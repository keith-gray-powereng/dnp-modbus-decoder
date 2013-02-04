Overall Description
===================
POWER Engineers is sponsoring a senior design project at Southern Illinois University Edwardsville Computer Science department.  This is the git repository for the project.

Project Description
===================
Distributed Network Protocol (DNP) is a communication protocol that has found widespread deployment in the electric and water utilities. DNP is supported by many Intelligent Electronic Devices (IEDs), communications processors, Remote Terminal Units (RTUs), and master stations. Modbus is another communications protocol which is commonly found in electrical substations.

Troubleshooting efforts may involve interpreting the raw communications data stream and extracting the DNP or Modbus message.  POWER Engineers would like to automate that process using a software application.

POWER Engineers will provide test cases in electronic format to validate the application's operation.

An optional task for creating a server based application is included.

Task 1 Specifications
=====================
The goal of this project is to produce a software application that can read data, decode all DNP or Modbus messages in the data, and display those messages in a meaninful way.  Task 1 describes the specific requirements associated with this project.

Subtask 1.0 Project Requirements
--------------------------------

Objective(s):
~~~~~~~~~~~~~
To clearly define the requirements for the execution of this project.

Prerequisite(s):
~~~~~~~~~~~~~~~~
None

Responsibility: 
~~~~~~~~~~~~~~~
POWER Engineers

Deliverable(s):
~~~~~~~~~~~~~~~
None

The following items define the requirements for the project:

* Software application built using Python and the Django web framework
* Unit tests should be used and the tests should cover 100% of the code
* HTML, Javascript, and CSS tests should also be included and test run in IE8 & IE9, Chrome, and Firefox
* Mercurial or Git distributed source control software should be used to manage development by different people
* Main Git repository will be hosted on Github.com
* Software to be released as open source under the GPLv3 license
* Capability to paste a copy of the message in hex
* Software should remove all extra data from the message including text such as "TX' and "RX"
* Software should be able to interpret mesages from the following communication processors and RTUs

    * NovaTech Orion5r and OrionLX
    * GE D20/D200
    * Cooper SMP Gateway

* Capability to interpret multiple messages
* Output to be in html format

    * Compatible with IE8 & IE9, Chrome and Firefox

* Messages displayed in a tree view hierarchy with more detailed information presented the lower down the tree the user navigates
* Software to be distributed to Windows users as a .exe file

    * Starts a web server listening on the localhost at the designated port
    * Opens users web browser pointed to the webserver now running on the user's machine
    * User interacts with the application through the web browser

* Documentation must be provided using RestructuredText and the sphinx application. The documentation must cover the following topics:

    * End User Usage
    * APTs

Task 2 Validation
=================
POWER will supply the test cases which the application will be validated against. The tests described in this section are separate from the unit tests described in Task 1.

Subtask 2.1 Bench Testing
-------------------------

Objective(s):
~~~~~~~~~~~~~
To define the testing requirements of the project

Prerequisite(s):
~~~~~~~~~~~~~~~~
None

Responsibility:
~~~~~~~~~~~~~~~
POWER Engineers

Deliverable(s):
~~~~~~~~~~~~~~~
Integration Test Cases

POWER will provide files containing data captured from each of the RTUs listed in Task 1. The files are to be used as input to the application and the output will be validated to ensure the application meets the requirements. The test cases will have a sub-category of "Common".  The "Common" test cases will contain messages that are most often seen in the field.

Assumption(s):
~~~~~~~~~~~~~~
Files to be submitted in ASCII or pcap format
Testing will be performed using Selenium Browser Automation

Task 3 Optional - Remotely Accessible Server
============================================
If time and budget allows, POWER would like the same application described in Task 1 to be available through a web interface accessible via the Internet.

Subtask 3.1 Remotely Accessible Server
--------------------------------------

Objective(s):
~~~~~~~~~~~~~
To define the testing requirements of a version of the application that can be access over the Internet.

Prerequisite(s):
~~~~~~~~~~~~~~~~
Task 1 and Task 2 are complete

Responsibility:
~~~~~~~~~~~~~~~
POWER Engineers

Deliverable(s):
~~~~~~~~~~~~~~~
None

A version of the applciation that is accessible via the Internet could be userful in certain testing situations. The following additional requirements would be applied to the application created in Task 1.

* Server application configured to be deployed using the current best practices for a Django application
* HTML output to be useful on desktop, laptop, tablet, and mobile device screens

Assumption(s):
~~~~~~~~~~~~~~
The same integration testing described in Task 2 will be applied to the server application

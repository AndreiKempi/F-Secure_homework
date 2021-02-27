Title: F-Secure Coding task 
Developer: Andrei Kempi

Task: Implement a program, that monitors web sites and reports their availability.

Main functions:

. Reads a list of web pages (HTTP URLs) and corresponding page content requirements from a configuration file.
. Periodically makes an HTTP request to each page.
. Verifies that the page content received from the server matches the content requirements.
. Measures the time it took for the web server to complete the whole request.
. Writes a log file that shows the progress of the periodic checks

Language: Python 3.8 
IDE: PyCharm 2019.3

Running: To run programm use command 'python SiteMonitor.py' from directory 'scr' 
Logs: Logs will be safed in directory 'logs'

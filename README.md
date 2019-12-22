# meep2

Cookie resource consumption denial of service testing tool.

This tool is adapted off of the proof of concept tool I created for CVE-2019-16889.  It differs from the original poc in that it allows you to define the cookie value.  This allows the tool to be used to test any cookie value regardless of architecture for resource consumption.

Use 'pip3 install -r requirements.txt' to install.

Usage: python meep2.py 'http://victim.com/' cookiename 50 20000
(50 represents the amount of threads and 20000 represents the amount of requests, adjust accordingly)

*Please use responsibly*

Please feel free to comment and or make suggestions to make this better!

Future updates will include, error handling, the ability to use post requests...

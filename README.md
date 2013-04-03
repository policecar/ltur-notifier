ltur-notifier
================

Receive a Pushover notification to your Android or iPhone 
if bahn prices at ltur drop to the maximum you're willing to pay.

Note
-------

This is work in progress which hasn't been tested in any thorough manner.  
Developed using Python 2.7 on Mac OS X 10.6.

Setup
-------

Install the python library mechanize ( cf. http://pypi.python.org/pypi/mechanize ), e.g.

    $ easy_install mechanize

Get your Pushover user token from https://pushover.net/ and enter it into config.py.  
Specify your traveling data in config.py as well. Then set up a cronjob for ltur-notifer.py

    $ crontab -e

e.g. insert the following line to run the script every 5 hours
    
    0 */5 * * * <INSERT_FULL_PATH_TO_PYTHON>/python <INSERT_FULL_PATH_TO_REPOSITORY>/ltur-notifier.py


Author
-------
Priska Herger

License
-------
License: [GNU GPLv3][1]
[1]: http://www.gnu.org/licenses/gpl.html

ltur-notifier
================

Receive a Pushover notification to your Android or iPhone 
if bahn prices at ltur reach the maximum you're willing to pay.

Setup
-------

Get your Pushover user token from https://pushover.net/ and enter it into config.py.  
Specify your traveling data in config.py as well. Then set up a cronjob for ltur-notifer.py, e.g. 
    
    0 */5 * * * <INSERT_FULL_PATH_TO_PYTHON>/python <INSERT_FULL_PATH_TO_REPOSITORY>/ltur-notifier.py

to run the script every 5 hours.

Author
-------
Priska Herger <priska@23bit.net>  

License
-------
License: [GNU GPLv3][1]
[1]: http://www.gnu.org/licenses/gpl.html

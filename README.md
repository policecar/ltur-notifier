ltur-notifier
================

A script that sends a [notification](https://pushover.net/) to your Android or iPhone 
if prices for train tickets at [l'tur](http://www.ltur.com/de/bahn.html?omnin=DB-DE) drop to the maximum you're willing to pay.

Note
-------

Work in progress. Developed using Python 2.7 on Mac OS X 10.6.

Setup
-------

Install [mechanize](http://pypi.python.org/pypi/mechanize), e.g.

    $ easy_install mechanize

Get your Pushover user token from https://pushover.net/ and enter it into config.py.  
Specify your traveling data in config.py. Then set up a [cronjob](http://crontab.org/) for ltur-notifer.py

    $ crontab -e

e.g. insert the following line to run the script every 5 hours
    
    0 */5 * * * <INSERT_FULL_PATH_TO_PYTHON>/python <INSERT_FULL_PATH_TO_REPOSITORY>/ltur-notifier.py

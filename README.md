ltur-notifier
================

A script that sends a [Pushover](https://pushover.net/) notifiation or email to your Android fon or iPhone 
if prices for train tickets at [l'tur](http://www.ltur.com/de/bahn.html?omnin=DB-DE) drop to the maximum you're willing to pay.

Note
-------
Work in progress. Developed using Python 2.7 on Mac OS X 10.6 and Ubuntu 14.04 LTS

This script is not being maintained and tested regularly. If it does not work properly anymore, please open an issue.


Setup
-------

Install dependencies [mechanize](http://pypi.python.org/pypi/mechanize) and [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4/4.3.2):

Using pip and the provided requirements.txt file:

    $ pip install -r requirements.txt

Alternatively, using easy_install:

    $ easy_install mechanize
    $ easy_install BeautifulSoup4

Enter your email specs into the config file or else get a Pushover user token from https://pushover.net/ and use that.
Specify your traveling data in config.py. Then set up a [cronjob](http://crontab.org/) for ltur-notifer.py

    $ crontab -e

e.g. insert the following line to run the script every 5 hours
    
    0 */5 * * * <INSERT_FULL_PATH_TO_PYTHON>/python <INSERT_FULL_PATH_TO_REPOSITORY>/ltur-notifier.py

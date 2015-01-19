# -*- encoding: utf-8 *-*

import datetime

# customize traveling specs
# mind that ltur offers bahn tickets only for the next 7 days starting from tomorrow
from_city = 'Berlin Hbf'
to_city = 'München Hbf'

# default to tomorrow
on_date = ( datetime.date.today() + datetime.timedelta( days=1 )).strftime( '%d.%m.%Y' )
#on_date = '21.01.2013'

at_time = '09:12'
max_price = 40.0

# ltur's Bahn webpage: journey form (dynamically loaded after page load via AJAX)
user_url = 'http://www.ltur.com/de/bahn.html?omnin=DB-DE'
scraper_url = 'http://bahn.ltur.com/ltb/searchform/external'

# set the mode of notification: pushover or email
# MODE = 'pushover'
MODE = 'email'

# keywords for webscraping
TRIGGER = [
    'price_Fernweh_H',      # really cheap prices
    'price_Sparpreis_H'     # medium cheap prices...
]
PRICE_TAG_REGEX = u'([0-9]{1,3}(,|.)?([0-9]{1,2}))?\s*€?'


# Pushover config
APP_TOKEN   = 'EpMD3BrlmxioeKvGujVccccPqHeUxd'
USER_TOKEN  = ''
PUSHOVER_URL = "api.pushover.net"
PUSHOVER_PATH = "/1/messages.json"


# E-mail config
EMAIL = 'you@example.org'
FROM_EMAIL = 'lturdaemon@example.org'
SMTP_SERVER = 'smtp.example.org'
SMTP_USER = 'lturdaemon@example.org'  # optional
SMTP_PASS = 'somesecretpassword'  # optional


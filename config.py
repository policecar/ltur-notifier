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

# ltur's Bahn webpage
url = 'http://www.ltur.com/de/bahn.html?omnin=DB-DE'

# set the mode of notification: pushover or email
# MODE = 'pushover'
MODE = 'email'

# keywords for webscraping
TRIGGER = '\xe2\x82\xac'	# the euro sign
IMPOSTOR = 'Sparangebote'
DELIMITERS = 'label>| \xe2\x82\xac'


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


# -*- encoding: utf-8 *-*

# customize traveling specs
# mind that ltur offers bahn tickets only for the next 7 days starting from tomorrow
from_city = 'Berlin Hbf'
to_city = 'München Hbf'
on_date = '21.01.2013'
at_time = '21:12'
max_price = 90.0

# ltur's Bahn webpage
url = 'http://www.ltur.com/de/bahn.html?omnin=DB-DE'

# keywords for webscraping
TRIGGER = '\xe2\x82\xac'	# the euro sign
IMPOSTOR = 'Sparangebote'
DELIMITERS = 'label>|,00 \xe2\x82\xac'


# Pushover config
APP_TOKEN   = 'EpMD3BrlmxioeKvGujVccccPqHeUxd'
USER_TOKEN  = ''

PUSHOVER_URL = "api.pushover.net"
PUSHOVER_PATH = "/1/messages.json"

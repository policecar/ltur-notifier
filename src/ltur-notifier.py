#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import httplib
import urllib
import sys
import re

from mechanize import Browser
from bs4 import BeautifulSoup

from config import *

# TODO: error handling
# (1) if on_date - today > 7, inform user

def main():
    page = submit_form()
    prices = parse_page(page.read(), TRIGGER)
    if any([p <= max_price for p in prices]):
        if MODE == 'pushover':
            send_pushover(min(prices))
        elif MODE == 'email':
            send_mail(min(prices))


def submit_form():
    br = Browser()  # create browser instance
    response = br.open(scraper_url)  # load page

    # hack
    rp_data = response.get_data()
    rp_data = re.sub(r'<optgroup label=".+">', "", rp_data)  # replace all optgroup elements
    response.set_data(rp_data)
    br.set_response(response)
    # eohack

    br.select_form(name='form_spar_topz')

    # fill in custom values
    br['from'] = from_city
    br['to_spar'] = to_city
    br.form.find_control('fromDate').readonly = False
    br['fromDate'] = on_date
    br['fromTime'] = at_time

    return br.submit()


def parse_page(haystack, needles):
    bs = BeautifulSoup(haystack)
    gems = []
    price_tags = []
    for needle in needles:
        price_tags.extend(bs.find_all('td', attrs={'class': needle}))

    for price_tag in price_tags:
        price_string = price_tag.get_text().strip()
        match = re.match(PRICE_TAG_REGEX, unicode(price_string))
        if match:
            price = match.group(1)
            price = re.sub(',', '.', price)
            gems.append(float(price))
    return gems


def send_pushover(cheapest):
    if not USER_TOKEN:
        print( "You have to configure your Pushover user token in config.py for this to work." )
        sys.exit()
    conn = httplib.HTTPSConnection(PUSHOVER_URL)
    conn.request('POST', PUSHOVER_PATH,
                 urllib.urlencode({
                     'title': '( : ltur für ' + str(cheapest) + ' ',
                     'token': APP_TOKEN,
                     'user': USER_TOKEN,
                     'message': ')',
                 }), {'Content-type': 'application/x-www-form-urlencoded'})

    # for debugging
    res = conn.getresponse()
    conn.close()


def send_mail(cheapest):
    import smtplib
    from email.mime.text import MIMEText

    # Create a text/plain message
    msg = MIMEText("Ltur notification. cheapest offer: %s €\n\n%s" % ( str(cheapest), user_url ))
    msg['Subject'] = 'Ltur notifier: %s ' % str(cheapest)
    msg['From'] = FROM_EMAIL
    msg['To'] = EMAIL

    s = smtplib.SMTP(SMTP_SERVER)
    if SMTP_USER and SMTP_PASS:
        s.login(SMTP_USER, SMTP_PASS)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.quit()


if __name__ == '__main__':
    main()

#! /usr/bin/env python
# -*- encoding: utf-8 -*-

# import BeautifulSoup
import mechanize
import httplib, urllib
import sys, re

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
    br = mechanize.Browser()  # create browser instance
    response = br.open(url)  # load page

    # hack
    rp_data = response.get_data()
    rp_data = re.sub(r'<optgroup label=".+">', "", rp_data)  # replace all optgroup elements
    response.set_data(rp_data)
    br.set_response(response)
    # eohack

    # TODO does not find form because it is dynamically loaded via ajax...
    # as it seems, mechanize cannot handle dynamic content
    # consider using Selenium instead?
    # cf. http://stackoverflow.com/a/8455194

    # hook directly into POST request sent by web form?
    # http://bahn.ltur.com/ltb/search/external
    # POSTing to that results in a redirect back to the original page...
    # seems like encrypted content is sent over in order to authenticate against the service

    br.select_form(name='form_spar')

    # fill in custom values
    br['trip_mode'] = ['trip_simple']  # alt: 'trip_both'
    br['from_spar'] = from_city
    br['to_spar'] = to_city
    br.form.find_control('start_datum').readonly = False
    br['start_datum'] = on_date
    br['start_time'] = at_time

    return br.submit()


def parse_page(haystack, needle):
    heaps = haystack.split('<')
    gems = []
    for heap in heaps:
        if needle in heap and not IMPOSTOR in heap:
            price = re.split(DELIMITERS, heap)[1]
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
    msg = MIMEText("Ltur notification. cheapest offer: %s €\n\n%s" % ( str(cheapest), url ))
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

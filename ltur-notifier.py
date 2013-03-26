#! /usr/bin/env python
# -*- encoding: utf-8 -*-

# import BeautifulSoup
import mechanize
import httplib, urllib
import sys, re

from config import *

#TODO: error handling
# (1) if on_date - today > 7, inform user

def main():
	page = submit_form()
	prices = parse_page( page.read(), TRIGGER )
	if any( [ p <= max_price for p in prices ] ):
		send_pushover( min( prices ))


def submit_form():
	br = mechanize.Browser()				# create browser instance
	response = br.open( url )				# load page
	# hack
	rp_data = response.get_data()
	rp_data = re.sub(r'<optgroup label=".+">', "", rp_data) # replace all optgroup elements
	response.set_data( rp_data )
	br.set_response( response )
	# eohack
	br.select_form( name='form_spar' )
	
	# fill in custom values
	br[ 'trip_mode' ] = [ 'trip_simple' ]	# alt: 'trip_both'	
	br[ 'from_spar' ] = from_city
	br[ 'to_spar' ] = to_city
	br.form.find_control( 'start_datum' ).readonly = False
	br[ 'start_datum' ] = on_date 
	br[ 'start_time' ] = at_time
	
	return br.submit()


def parse_page( haystack, needle ):
	heaps = haystack.split( '<' )
	gems = []
	for heap in heaps:
		if needle in heap and not IMPOSTOR in heap:
			gems.append( float( re.split( DELIMITERS, heap )[1] ))
	return gems


def send_pushover( cheapest ):
    if not USER_TOKEN:
        print "You have to configure your Pushover user token in config.py for this to work."
        sys.exit()
    conn = httplib.HTTPSConnection( PUSHOVER_URL )
    conn.request( 'POST', PUSHOVER_PATH,
        urllib.urlencode({ 
            'title'  : '( : ltur für ' + str( cheapest ) + ' ',
            'token'  : APP_TOKEN,
            'user'   : USER_TOKEN,
            'message': ')',
        }), { 'Content-type': 'application/x-www-form-urlencoded' })

    # for debugging
    res = conn.getresponse()
    conn.close()


if __name__ == '__main__':
	main()

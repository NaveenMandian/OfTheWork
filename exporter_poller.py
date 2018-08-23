import urllib2
from datetime import datetime
from time import sleep
import logging
poll_interval = 1
url ='http://txt2html.sourceforge.net/sample.txt'  #Update with exporter URL (sample URL given)

while True:
    metrics_data = urllib2.urlopen(url).readlines()
    logging.warning('Successfully read url data at '+ url+'time: '+ str(datetime.now()))
    sleep(poll_interval)
#   print metrics_data

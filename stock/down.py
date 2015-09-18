#! /usr/bin/env python
#coding=utf-8

from os.path import basename
from urlparse import urlsplit
import urllib2
import csv

def url2name(url):
  return basename(urlsplit(url)[2])


# read csv http://python.usyiyi.cn/python_278/library/csv.html
def download(url, localFileName = None):
  localName = url2name(url)
  req = urllib2.Request(url)
  r = urllib2.urlopen(req)
  if r.info().has_key('Content-Disposition'):
    # If the response has Content-Disposition, we take file name from it
    localName = r.info()['Content-Disposition'].split('filename=')[1]
    if localName[0] == '"' or localName[0] == "'":
      localName = localName[1:-1]
  elif r.url != url:
    # if we were redirected, the real file name we take from the final URL
    localName = url2name(r.url)
  if localFileName:
    # we can force to save the file as specified name
    localName = localFileName
  f = open(localName, 'wb')
  f.write(r.read())
  f.close()

def readcsv():
    with open('E:\\stock\\600036.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print ', '.join(row)
 
if __name__ == "__main__":
    import sys
    readcsv()
    
    
#    git config --global credential.helper store
    
    sys.exit(1)
    
    shformat = "http://quotes.money.163.com/service/chddata.html?code=0%s&start=19020918&end=22151212&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"  
    szformat = "http://quotes.money.163.com/service/chddata.html?code=1%s&start=19020918&end=22151212&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
    downurl=""
    shcodelist=['600557', '600036', '601169', '600000', '601169', '601166', '600535', '601000', '600549']
    szcodelist=['002241', '002364', '002108', '002262', '000009']
    for code in shcodelist:
        downurl= shformat %code
        download(downurl)
        
    for code in szcodelist:
        downurl= szformat %code
        download(downurl)
        
    print szcodelist
    #download(r'http://quotes.money.163.com/service/chddata.html?code=0600884&start=19920918&end=20150902&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP')

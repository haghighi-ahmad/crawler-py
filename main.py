import urllib
from bs4 import BeautifulSoup
import json
import bs4
import time


# get a Table as input
# return stored snp/infos as a JSON object
def getSnp(tbl):
    """

    :type tbl: bs4.element.Tag
    """
    snp = {}
    for row in tbl.find_all('tr'):

        th = row.th.string

        if hasattr(row.td, 'contents'):
            td = row.td.contents.__str__()
        else:
            td = 'NULL'

        # if td != 'NULL':
        #     td = BeautifulSoup(td,'html.parser').get_text()

        snp[th] = td

    return snp


# list of all snps
lst = []

for ID in range(0, 220):
    page = urllib.urlopen("http://XXXXX?id=%s" % ID)
    doc = BeautifulSoup(page, 'html.parser')
    table = doc.table
    if table:
        # print table
        lst.append(getSnp(table))
    # use sleep to prevent DoS or blocking by IPS
    # time.sleep(1)

# print lst
# print '________________'
# print
# print json.dumps(lst)


# Storing
target = open('result_pretty.json', 'w')
target.truncate()
target.write(json.dumps(lst,indent=4))
target.close()

target = open('result.json', 'w')
target.truncate()
target.write(json.dumps(lst))
target.close()

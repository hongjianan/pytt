# -*- coding: utf-8 -*-

import sys
import urllib
import urllib2
import re

reload(sys)
sys.setdefaultencoding("utf-8")


def run():
    rsp = urllib2.urlopen("http://neihanshequ.com/")
    html = rsp.read()

    pattern = '''<div class="upload-txt  no-mb">(.*?)</div>'''
    pa = re.compile(pattern, re.S)
    ma = pa.findall(html)
    print(len(ma))
    for i in ma:
        pa = re.compile(r"<p>.*</p>")
        ma = pa.search(i)
        text = ma.group().replace(r"<p>", "").replace(r"</p>", "")
        # text = urllib.unquote(text)
        print(text)
        print("========")

if __name__ == "__main__":
    run()

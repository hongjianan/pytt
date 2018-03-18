# coding: utf-8

import sys
from lxml import etree

'''
<city>
    <bookstore>
    
    <book category="COOKING">
      <title lang="en">Everyday Italian</title>
      <author>Giada De Laurentiis</author>
      <year>2005</year>
      <price>30.00</price>
    </book>
    
    <book category="CHILDREN">
      <title lang="en">Harry Potter</title>
      <author>J K. Rowling</author>
      <year>2005</year>
      <price>29.99</price>
    </book>
    
    <book category="WEB">
      <title lang="en">XQuery Kick Start</title>
      <author>James McGovern</author>
      <author>Per Bothner</author>
      <author>Kurt Cagle</author>
      <author>James Linn</author>
      <author>Vaidyanathan Nagarajan</author>
      <year>2003</year>
      <price>49.99</price>
    </book>
    
    <book category="WEB">
      <title lang="en">Learning XML</title>
      <author>Erik T. Ray</author>
      <year>2003</year>
      <price>39.95</price>
    </book>
    
    </bookstore>
</city>
'''

def xml_parse(text):
    xml = etree.XML(text)
    # print(dir(xml))
    print("==========")

    result = xml.xpath('/city/bookstore/book/title/text()')
    # result = xml.xpath('//title[@*]')
    print(type(result), result)


def run():
    # open xml
    f = open("test.xml", "r")
    xml = f.read()
    xml_parse(xml)


if __name__ == "__main__":
    run()

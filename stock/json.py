#! /usr/bin/env python
#coding=utf-8

import simplejson as json


def readjsonstr():
    file = 'D:\\tmp.txt'
    dict = ''
    try:
        fp = open(file, 'r')
        dict = json.load(fp)       
        print dict["Api_ThirdLogin"].keys()
        print dict["Api_ThirdLogin"]["action"]
    finally:
        fp.close()
    

if __name__ == '__main__':
    import sys
    
    readjsonstr()
    sys.exit(2)
    

    json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    print json.dumps("\"foo\bar") 

    print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True) 

    #s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
    s = json.loads("D:\\tmp.txt")
    print s.keys()
    print s.values()
    #print s["name"]
    #print s["type"]["name"]
    #print s["type"]["parameter"][1]

#! /usr/bin/env python
#coding=utf-8

import string
import types

global_count=0
global_price=0.0

import types
def check(object):
    print object,
    if type(object) is types.IntType:
        print "INTEGER",
    if type(object) is types.FloatType:
        print "FLOAT",
    if type(object) is types.StringType:
        print "STRING",
    if type(object) is types.ClassType:
        print "CLASS",
    if type(object) is types.InstanceType:
        print "INSTANCE",
    print


def parseline(line):    
    global global_count
    global global_price
    
    valuelist=[]
    line1=str(line)
    valuelist=line1.split(',')
    print "price %s" %valuelist[3]
    
    print "global_count == %s" %global_count
#    if global_count == 1:
#        print '**********'
#        global_price == string.atof(valuelist[3])
#    else:
#        print '---------------'
#        
    if string.atof(valuelist[3]) < global_price:
        try:
            global_price = string.atof(valuelist[3])
        except:
            global_price = 0.0 
    else:
        print "N"
    global_count += 1   
    
#    print global_price
    print '----------------------------------------'
    

def readfile(filePath, savePath=None):
    try:
        read = open(filePath)
        line=read.readline()
        n = 0
        list=[]
        while line:
            print line
            newline=""
            try:
                n += 1
                newline = parseline(line)
            except:
                n +=1 
#            newline += "\n"
            list.append(newline)
            line=read.readline()
            if n == 3:
                break
    finally:
        read.close 
    
    return 1
    
global_str = 'foo'
def foo():
    global global_str
    local_str = 'bar'
    global_str = 'test'
    return global_str + local_str


if __name__=="__main__":
    readfile("E:\\stock\\600036.csv")
#    print foo()
#    print global_str
    print "last global_count %s" %global_count
    print "the best price: %s" %global_price
#    a="a\tb\tc"
#    a=a.replace('\t', '')
#    print a
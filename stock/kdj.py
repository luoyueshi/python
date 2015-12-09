#! /usr/bin/env python
#coding=utf-8

class stock():
    MinPrice = 0
    MaxPrice = 0
    ClosePrice = 0
    
    def __init__(self,min,max,close):  
        self.MinPrice = min  
        self.MaxPrice = max  
        self.ClosePrice = close 
    
#! /usr/bin/env python
#coding=utf-8
 
import os
import mysql.connector
import urllib
 
config = {
  'user': 'root',
  'password': '4321',
  'host': '127.0.0.1',
  'database': 'stock',
  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)

    
class ReadFile:
    def readLines(self):
        f = open("/opt/stock/600557.csv", "r", 1)
        i=0
        list=[]
        for line in f:
            strs = line.split(",")
            if len(strs) != 15:
                continue
            
            if strs[3] == '0.0':
                continue
                                    
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")  
            a='\xd5\xd0\xc9\xcc\xd2\xf8\xd0\xd0'
#            print a.decode('gbk')               
                                  
            name = strs[2].decode('gbk')

            data=(strs[0],strs[1].replace("\'", ""),name,strs[3],strs[4],strs[5],strs[6],strs[7],strs[8],strs[9],strs[10],strs[11],strs[12],strs[13],strs[14].replace("\n",""),)
            list.append(data)
            
            cursor=cnx.cursor()
            sql = "insert into stock_history(day, code, name, close_price, \
            high_price, low_price, open_price, before_closing_price, s_change, chg, turnover_rate, \
            volume, AMO, market_cap, circulation_market_value)   \
            values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"   
            if i>5000:
                cursor.executemany(sql,list)
                cnx.commit()
                print("插入")
                i=0
                list = []

            i=i+1
            
        if i>0:
            print list
            a = ['11', '123']
            values = [('22333',),(6,)]
            param = (4, 33, 44 )
            print sql
            cursor.executemany(sql,list)
            print list
            cnx.commit()
        cnx.close()
        f.close()
        print("ok")
        
    def listFiles(self):
        d = os.listdir("E:/data/")
        return d
        
             
if __name__ == "__main__":        
    readFile = ReadFile()
    readFile.readLines()

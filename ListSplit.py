# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:04:34 2020

@author: swetha
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 20:59:26 2020

@author: swetha
"""

def listSplit():
    global book
    global author
    global q
    global cost
    book=[]
    author=[]
    q=[]
    cost=[]
    with open("stock.txt","r") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    book.append(a)
                elif(ind==1):
                    author.append(a)
                elif(ind==2):
                    q.append(a)
                elif(ind==3):
                    cost.append(a.strip("$"))
                ind+=1

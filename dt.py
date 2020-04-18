# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:01:22 2020

@author: swetha
"""


def getDate():
    import datetime
    now=datetime.datetime.now
    return str(now().date())

def getTime():
    import datetime
    now=datetime.datetime.now
    return str(now().time())

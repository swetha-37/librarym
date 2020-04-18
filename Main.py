# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 20:59:26 2020

@author: swetha
"""

import Return
import ListSplit
import dt
import Borrow

def start():
    while(True):
        print("------------------------------------------------------")
        print("        Welcome to the library management system      ")
        print("------------------------------------------------------")
        print("Enter 1. To Display the books available")
        print("Enter 2. To Borrow a book")
        print("Enter 3. To Return a book")
        print("Enter 4. To exit")
        try:
            a=int(input("Select a choice : "))
            print()
            if(a==1):
                with open("stock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(a==2):
                ListSplit.listSplit()
                Borrow.borrowBook()
            elif(a==3):
                ListSplit.listSplit()
                Return.returnBook()
            elif(a==4):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please enter input as suggested.")
start()

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:05:56 2020

@author: swetha
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:01:23 2020

@author: swetha
"""

import dt
import ListSplit

def borrowBook():
    s=False
    while(True):
        fName=input("Enter the first name of the borrower: ")
        if fName.isalpha():
            break
        print("please input alphabet from A-Z")
    while(True):
        lName=input("Enter the last name of the borrower: ")
        if lName.isalpha():
            break
        print("please input alphabet from A-Z")
            
    t="Borrow-"+fName+".txt"
    with open(t,"w+") as f:
        f.write("               Library Management System  \n")
        f.write("                   Borrowed By: "+ fName+" "+lName+"\n")
        f.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write("S.N. \t\t Bookname \t      Authorname \n" )
    
    while s==False:
        print("\nPlease select a option below:\n")
        for i in range(len(ListSplit.book)):
            print("Enter", i, "to borrow book", ListSplit.book[i])
    
        try:   
            a=int(input())
            try:
                if(int(ListSplit.q[a])>0):
                    print("Book is available")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ ListSplit.book[a]+"\t\t  "+ListSplit.author[a]+"\n")

                    ListSplit.q[a]=int(ListSplit.q[a])-1
                    with open("Stock.txt","w+") as f:
                        for i in range(3):
                            f.write(ListSplit.book[i]+","+ListSplit.author[i]+","+str(ListSplit.q[i])+","+"$"+ListSplit.cost[i]+"\n")


                    
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Do you want to borrow more books? However you cannot borrow same book twice. Press y for yes and n for no."))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(ListSplit.book)):
                                print("Enter", i, "to borrow book", ListSplit.book[i])
                            a=int(input())
                            if(int(ListSplit.q[a])>0):
                                print("Book is available")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ ListSplit.book[a]+"\t\t  "+ListSplit.author[a]+"\n")

                                ListSplit.q[a]=int(ListSplit.q[a])-1
                                with open("Stock.txt","w+") as f:
                                    for i in range(3):
                                        f.write(ListSplit.book[i]+","+ListSplit.author[i]+","+str(ListSplit.q[i])+","+"$"+ListSplit.cost[i]+"\n")
                                        s=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing books from us. ")
                            print("")
                            loop=False
                            s=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("Book is not available")
                    borrowBook()
                    s=False
            except IndexError:
                print("")
                print("Please choose book acording to their number.")
        except ValueError:
            
            print("Please choose as suggested.")

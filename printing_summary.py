#!/usr/bin/python

import os.path as o
import sys
import re


#--------------------validate the execution syntax-------------------------------

try:
    opt = sys.argv[1]
    if(opt=="-u"):
        myuser = sys.argv[2]
        #print("ENTERED USER: "+myuser)
        myfile = sys.argv[3]

        if("-" in myuser):
            sys.exit("Syntax error! Please check your syntax")

        if(len(sys.argv)>4):
            sys.exit("Syntax error! Please check your syntax")

    else:
        myfile = sys.argv[2]
        if(len(sys.argv)>3):
            sys.exit("Syntax error! Please check your syntax")

except IndexError:
    sys.exit("Syntax error! Please check your syntax")

#--------------------------------------------------------------------


#--------------check if the file exists, is a file and is readable-------------------

if (o.exists(myfile)):
    if(o.isfile(myfile)):
        try:
            f=open(myfile)
            f.close()
        except PermissionError:
            sys.exit("Permission Denied. The File \""+myfile+"\" is not readable")
       # else:
            #print("\""+myfile+"\" exists as a file and is readable\n")
        
    else:
        sys.exit("\""+myfile+"\" is not a file")
          
else:
    sys.exit("\""+myfile+"\" does not exist")

#-------------------------------------------------------------------------------------


#--------------------reading the file--------------------------------------

dict={}

f=open(myfile)

for line in f:
    line=line.strip("\n")
    fields=re.split(",", line)
    #print(fields[2])
    user=fields[2]
    filename=fields[0]
    bytes=int(fields[1])

#creating a dictionary containing a dictionary of lists
#inner disctionary stores the files as key which stores a list of file's bytes as value
#outer dictionary stores users as key which stores user's printed files as value and key of inner dictionary
  
    if user in dict:
        if filename in dict[user]:
            dict[user][filename].append(bytes)

        else:
            dict[user][filename]=[bytes]

    else:
        dict[user]={filename:[bytes]}

f.close()
#print(dict)

#----------------------------------------------------------------------------


#----------------------performing operations based on options-----------------------------

#Printing unique usernames using option -a
if(opt=="-a"):
    #print("execute function username")
    if (len(dict) == 0):
        print("No printing users")
    else:
        print("Printing users:")
        for u in dict:
            print(u)


#Printing total number of files printed using option -f
elif(opt=="-f"):
    #print("execute function total_files")
    if (len(dict) == 0):
        print("Total number of files printed: 0")
    else:
        total_files = 0
        for u in dict:
            #print(u)
            for v in dict[u]:
                #print(len(dict[u][v]))
                total_files += len(dict[u][v])
        print("Total number of files printed: "+str(total_files))


#Printing total number of bytes printed using option -s
elif(opt=="-s"):
    #print("execute function total_bytes")
    if (len(dict) == 0):
        print("Total number of bytes printed: 0")
    else:
        total_bytes = 0
        for u in dict:
            for v in dict[u]:
                for e in range(0,len(dict[u][v])):
                    total_bytes += dict[u][v][e]
        print("Total number of bytes printed: "+str(total_bytes))


#Printing user's printing details using option -u
elif(opt=="-u"):
    #print(myuser)
    user_files = 0
    user_bytes = 0
    max_file = 0
    
    if myuser in dict:
        for u in dict[myuser]:
           user_files += len(dict[myuser][u])
           for e in range(0,len(dict[myuser][u])):
               user_bytes += dict[myuser][u][e]
               if(dict[myuser][u][e]>max_file):
                   max_file = dict[myuser][u][e]
        print("User "+myuser+":")
        print("Total number of files printed: "+str(user_files))
        print("Total number of bytes printed:"+str(user_bytes))
        print("Largest file printed: "+str(max_file))
    
    else:
        print("User "+myuser+" not found")
        

#Printing student details using option -v
elif(opt=="-v"):
    print("##########################################")
    print("Name: Abdul Razik\nSurname: Fakih\nStudent ID: 13494137\nDate of Completion: 28th May 2020")
    print("##########################################")


#correct syntax but wrong option
else:
    sys.exit("Option \""+opt+"\" does not exist")








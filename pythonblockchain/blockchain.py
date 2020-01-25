from hashlib import sha256
from tkinter import *
import time
import sys
import webbrowser
global LastHash;LastHash=""

try:
    open('HASH.dat','x').write('')
except:
    pass

#global difficulty
difficulty=1


#global index
index=[]

class block:
    
    def __init__(self,data):
        self.timestamp=self.timestampee()
        self.LastHash=LastHash
        self.data=data
        a=[]
        a=block.Hashe(data,LastHash,self.timestamp)
        self.Hash=str(a[0])
        self.epoch=str(a[1])
        block.addBlock(self.data,self.Hash,self.LastHash,self.timestamp,self.epoch)

    def reset_hash():
        global LastHash
        LastHash= str(open("HASH.dat",'r').read())
        
        
    def timestampee(self):
        a=int(float(time.time()*1000))
        a=str(a)
        return a

    def printblock(timestamp,LastHash,Hash,data,epoch):
        a=str("Block was added with \n Timestamp=%s \n lastHash= %s \n Hash=%s \n Data= %s \n epoch= %s \n \n \n"%
              (str(timestamp),str(LastHash),str(Hash)[0:15],str(data),str(epoch)))
        open('HASH.dat','w').write(str(Hash[0:15]))
        block.reset_hash()
        return a

    def toHex(x):
        x=x.encode('utf-32')
        x=(sha256(x)).hexdigest()
        return x
        
    def Hashe(data,LastHash,timestamp):
        epoch=0
        #global Hash
        Hash=""
        temp=" "
        a=""
        while(temp[0:difficulty]!=a):
            timestamp=block.timestampee(3)
            temp=(''+str(data)+str(LastHash)+str(timestamp)+'')
            cond2=str(block.toHex(("0"*difficulty)))
            temp=str(block.toHex(temp))
            a= str(block.toHex("0"*difficulty))
            a=a[0:difficulty]
            epoch=epoch+1

        Hash=str(temp)
        return [Hash,epoch]

    def genesis():
        data='1st Block'
        Hash="f1r5t Ha5h"
        LastHash=""
        timestamp="Genesis Time"
        epoch=0
        block.addBlock(data,Hash,LastHash,timestamp,epoch)


    def addBlock(data,Hash,LastHash,timestamp,epoch):
        gene=block.printblock(timestamp,LastHash,Hash,data,epoch)
        index.append(gene)



def write_html(data):
    htmlstart=str(open("toread.html","r").read())
    #now writing in the web
    htmlend=str(open('toend.html','r').read())
    
    total=""
    open('temp_data.html','w').write(htmlstart)
    
    for i in range(0,20):
        if (i%2!=0 or i==0):
            total=str(""+str(index[i]))
            total=total.replace('\n','<br>')
            open('temp_data.html','a').write(total)
            total=""
    

    
    open('temp_data.html','a').write(htmlend)


def runhtml():
    webbrowser.open('temp_data.html')

block.genesis()

for i in range(1,20):
    data=("THIS IS BLOCK NO. "+str(i))
    index.append(str(block(data))+"")


for j in range(0,20):
    if (j%2!=0 or j==0):
        write_html(index[j])


runhtml()

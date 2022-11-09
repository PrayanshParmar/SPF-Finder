import os 
import sys
from src import figlet 
from src import colors as co 

def printintro():
    co.printout(figlet.ascii_work, co.BLUE)
    co.printout("\n[WRN]",co.YELLOW)
    co.printout(" Use with caution.You are responsible for your actions\n")
    co.printout("[WRN]",co.YELLOW)
    co.printout(" Developer assume no liability and are not responsible for any misuse\n\n")
    

def spf_bulk(domain,read=" "): 
 tool= "nslookup -type=txt {} " 
 com= tool.format(domain) 
 run=os.popen(com)
 read=run.read() 
 if '"v=spf1' in read:  
    res0="(SPF record found) {}" 
    res1=res0.format(domain) 
    co.printout(res1,co.GREEN) 
    return res1 
 elif "text" in read: 
    res01="(SPF record not found) {}"
    res1=res01.format(domain)  
    co.printout(res1,co.YELLOW) 
    return res1 
 else:
    res0="An error occured,skipping {} "
    res1=res0.format(domain)
    co.printout(res1,co.RED) 

def spf_single(domain): 
 tool= "nslookup -type=txt {} " 
 com= tool.format(domain) 
 run=os.popen(com)
 read=run.read() 
 if '"v=spf1' in read:  
    co.printout("SPF record found",co.GREEN) 
    
 elif "text" in read: 
    co.printout("SPF record not found",co.YELLOW) 

 else:
    co.printout("An error occured",co.RED)    
    
 
def read_write(path1,path2,length): 
  f=open(path1,"r")
  str1= " " 
  O=open(path2,"w") 
  for i in range(length): 
     str1=f.readline()   
     result=spf_bulk(str1) 
     if result!=None:
       O.write(result) 
     else:
        pass  
  f.close() 
  O.close()  

def read_print(path1,length): 
  f=open(path1,"r")
  str1= " " 
  for i in range(length): 
     str1=f.readline()   
     spf_bulk(str1)  
  f.close() 
      
def len_f(path1): 
   f=open(path1,"r")
   str1=f.readlines() 
   length=len(str1) 
   return length 
   f.close() 
 
 
#__________________________________________Main___________________________________
args=len(sys.argv)
argv=sys.argv

if args==1:
     print()
     print('''-h, --help    for Help section''')
     
elif args==2 and argv[1]=="-h" or argv[1]=="--help":
    print()
    help='''-h, --help         Help section
-v, --version      Show version
-d, --domain       for single domain
-l, --inputfile    Input file of domain name (support only ".txt")
-o, --outputfile   Output file name (support only ".txt")

usage[]: python3 spf.py [options] domain_name '''
    co.printout(help,co.CYAN)

elif args==2 and argv[1]=="-v" or argv[1]=="--version":
    co.printout('Version --> 1.0',co.CYAN)

elif args==3 and argv[1]=="-d" or argv[1]=="--domain":
    domain=argv[2]
    printintro()
    spf_single(domain)

elif args==3 and argv[1]=="-l" or argv[1]=="--inputfile":
    path1=argv[2]
    printintro()
    length=len_f(path1)
    read_print(path1,length)

elif args==5 and argv[1]=="-l" or argv[1]=="--inputfile" and argv[3]=="-o" or argv[3]=="--outputfile":
    path1=argv[2]
    path2=argv[4]
    printintro()
    length=len_f(path1)
    read_write(path1,path2,length)

else:
    co.printout("Invalid operation!!",co.RED)


 

    

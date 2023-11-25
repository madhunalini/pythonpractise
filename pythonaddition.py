import sys
import os 

def addition(a,b):
    c=a+b
    return c  
a=float(sys.argv[1])
operation=sys.argv[2]
b=float(sys.argv[3])

if (operation=="addition"):
    output=a+b
    print(output)

print(os.getenv("password"))
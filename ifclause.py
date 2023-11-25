import sys

instance_type=sys.argv[1]

if(instance_type=="t2.micro"):
    print("ok its 2$/day")
elif(instance_type=="t2.medium"):
    print("ok its 3$/day")
elif(instance_type=="t2.nano"):
    print("ok its 1$/day")
else:
    print("dont create new instances")


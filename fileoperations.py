def file_operations(file_path,key,value):
    with open(file_path,"r") as file:
        lines= file.readlines()

    with open(file_path, "w"):
        for line in lines:
            if key in line:
                file.write(key +"="+ value)
            else:
                file.write(line)

        
file_operations("max_connections.py","max_connections","1000")

             


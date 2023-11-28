
def file_operations(filepath,key, value):
    with open(filepath, "r") as file:
        files= file.readline()

    with open(filepath,"w") as file:
        for line in files:
            if key in line:
                file.write(key + "" + value)
            else:
                file.write(line)

file_operations("server_config.py",max_connections,1000)

             


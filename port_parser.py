#! usr/bin/env/python3
import re

# Need a better regex expression to filter out special characters.  Perhaps a split is the way to do this.
logfile = open("caterpillar_log.txt") #default mode is read only
pattern = r"([^`~!@#$%^&*()_+={}\[\]|\\:;“’<,>.?๐฿A-Za-z](?:[0-9]+(?:-[0-9]+)?)(?:,[0-9]+(?:-[0-9]+)?)*)" #pattern for port number 0-65535
port_list = []

for line in logfile:
    # this could surely be consolidated to a function at the least
    ports = re.findall(pattern,line)
    for port in ports:
        if port.isdigit() == False: #port number is numeric
            pass
        if len(port) > 5: 
            pass   #port number can be no more than 5 digits
        if port[0] == 0 and len(line) > 1:
            pass
        port_list.append(ports)
    
        print(port_list)




    
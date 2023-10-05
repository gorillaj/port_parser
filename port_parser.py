#! usr/bin/env/python3
import re
import numpy as np

# Need a better regex expression to filter out special characters.  
logfile = ("caterpillar_log.txt") #default mode is read only
pattern = r"^ 0|([1-5][0-9]{0,4})|(6[1-4,0][0-9]{0,3})|(65[1-4,0][0-9]{0,2})|(655[1-2,0][0-9])|(6553[1-5,0])$ " #pattern for port number 0-65535
filtered_items = r"[A-Za-z],\./,\-/)" # Need a better regex expression to filter out special characters
dates = r"^\d{2}[/-]\d{2}[/-]\d{4}$" #mm/dd/yyyy
alt_dates = r"^\d{4}-\d{2}-\d{2}$"  #yyyy/dd/mm
timestamps = r"^\d{2}:\d{2}:\d{2}$"
ip_addresses =r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$"
cleaned_strings=[]
all_ports=[]

with open(logfile) as f:
    for line in f:                      #log files should be opened line by line
        lines=line.split() 
        for line in lines:
            if line is not re.findall(dates,line) and line is not re.findall(timestamps,line) and line is not re.findall(ip_addresses,line) and line is not re.findall(alt_dates,line):   #remove dates, timestamps, and ip addresses
                cleaned_strings.append(line)
                for line in cleaned_strings:
                    possible_ports=line.split('"')
                    for item in possible_ports:
                           if len(item) < 6 and item.isdigit() == True:
                            all_ports.append(item)
                            
                            ports=np.array(all_ports)          #output unique values for port no
                            port_no=np.unique(ports)
                            print(port_no)   





    
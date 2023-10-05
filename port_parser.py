#! usr/bin/env/python3

#import sys module would be used for most cases
import re

logfile = ("caterpillar_log.txt") # this would be sys.argv[1] for most use cases #default mode is read only
pattern = r"^ 0|([1-5][0-9]{0,4})|(6[1-4,0][0-9]{0,3})|(65[1-4,0][0-9]{0,2})|(655[1-2,0][0-9])|(6553[1-5,0])$ " #pattern for port number 0-65535
filtered_items = r"[A-Za-z],\./,\-/)" # Need a better regex expression to filter out special characters.
dates = r"^\d{2}[/-]\d{2}[/-]\d{4}$" #mm/dd/yyyy
alt_dates = r"^\d{4}-\d{2}-\d{2}$"  #yyyy/dd/mm
timestamps = r"^\d{2}:\d{2}:\d{2}$"
ip_addresses  =r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$"
cleaned_strings=[]
all_ports =[]
ports = set()

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
                            for port in all_ports:
                                ports.add(port)
                                # ports[port] = ports.get (item, 0) +1                        #output unique values for port no
print(*ports,sep = "\n")        #additional processing would reveal only certain ports but could overlook potential ones
                          
                               





    
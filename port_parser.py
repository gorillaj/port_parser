#! usr/bin/env/python3
import re


logfile = ("caterpillar_log.txt")
pattern = r" ((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4})) "

with open(logfile) as f:
    for line in f:
        line = " ".join(line.split(",:,[,]"))
        port_no = re.findall(pattern,line)
            
        ports=port_no 
        print(ports)
#! usr/bin/env/python3
import re

# Need a better regex expression to filter out special characters.  Perhaps a split is the way to do this.
logfile = ("caterpillar_log.txt") #default mode is read only
pattern = r"^((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4}))$" #pattern for port number 0-65535
with open(logfile) as f:
    for line in f:                      #log files should be opened line by line
        num_pattern=re.findall('(\d{1,5})', line) #find number strings len<5 
        for item in num_pattern:
            numbers=re.search(pattern,item)  
            print(numbers.group())
        





    
#! usr/bin/env/python3
import re

# Need a better regex expression to filter out special characters.  Perhaps a split is the way to do this.
logfile = ("caterpillar_log.txt") #default mode is read only
pattern = r"([^`~!@#$%^&*()_+={}\[\]|\\:;“’<,>.?๐฿A-Za-z](?:[0-9]+(?:-[0-9]+)?)(?:,[0-9]+(?:-[0-9]+)?)*)" #pattern for port number 0-65535
with open(logfile) as f:
    for line in f:
        num_pattern=re.findall( '(\d+)', line )
        for item in num_pattern:
            numbers=re.findall(pattern,item)
            print(numbers)
        





    
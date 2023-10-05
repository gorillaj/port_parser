# port_parser
script for parsing log file to return potential port numbers.  While for the sample text, it is obvious this script returns more than the existant ports, and tuning this further just using regex (ie only known ports, only 4- 5- char strings), could limit 
utility when parsing larger files by overlooking potential port numbers.  In the event of events like cyberattack, following up on a ll potentially valuable ports seems preferable to possibly overlooking one.

Sys module can be enabled by removing hashtag and replacing logfile argument with sys.arg[1] for general untility based on end-user system configuration

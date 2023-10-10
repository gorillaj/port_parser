# port_parser
script for parsing log file to return potential port numbers.  While for the sample text, it is obvious this script returns more than the existant ports, tuning this further using only regex (ie only known ports, only 4- 5- char strings), could limit utility when parsing larger files by overlooking potential port numbers (and ports like 80 should always be considered).   In the event of cyberattack, following up on all potential ports seems preferable to possibly overlooking one.

Sys module can be enabled by removing hashtag and replacing logfile argument with sys.arg[1] for general utility based on end-user system configuration

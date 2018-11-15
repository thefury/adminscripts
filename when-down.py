#!/usr/bin/env python

import sys
import os
import time
import getopt
import subprocess 

DEFAULT_INTERVAL=60
DEFAULT_TIMEOUT=3600

def print_usage():
    print "usage: retry.py [options] -- command"

def print_help():
    print '''
    usage: 
    retry.py [options] -- command
    
    description: 
    retry commands until they succeed or timeout
    
    options:
    -h: display this message
    -a, --address: the IP address to tes
    -i, --interval: the interval between attempts in seconds (default 60s)
    -t, --timeout: the timeout in seconds (default 3600s)
    '''


def parse_args(argv):
    interval = DEFAULT_INTERVAL
    timeout = DEFAULT_TIMEOUT
    address = ""

    try:
        opts, args = getopt.getopt(argv, "hi:t:a:", ["interval=","timeout=","address="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ['-a', '--address']:
            address = arg
        elif opt in ['-i', '--interval']:
            interval = arg
        elif opt in ['-t', '--timeout']:
            timeout = arg

    return int(interval), int(timeout), address, args

def is_up(address):
    if os.system("ping -c 1 " + address) is 0:
        return True
    else:
        return False

def main():
    interval, timeout, address, command = parse_args(sys.argv[1:])

    while timeout > 0: 
        if (not is_up(address)):
            returncode = subprocess.call(command)
        
            if returncode == 0:
                break

        time.sleep(interval)
        timeout -= interval

if __name__ == "__main__":
    main()


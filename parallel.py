#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from subprocess import Popen
import subprocess

processes = []
INSTANCES = 1

def cmd(command):
    try:
        print('command: ', command)
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Wait for completion and to capture the error message,
        stdout, stderr = p.communicate(timeout=15)
        if(p.returncode != 0):
            print('ERROR', stderr)
    except OSError as e:
        print("OSError > ",e.errno)
        print("OSError > ",e.strerror)
        print("OSError > ",e.filename)


def main():
    if len(sys.argv) > 1 :
        print('we have arguments')
        print(sys.argv)
    else:
        print('no arguments')
        
    print('in progress...')

if __name__ == '__main__':
    main()
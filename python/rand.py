#!/usr/bin/env python
"""rand a dataset"""

import sys
import random
def Usage():
    print 'rand.py inputfile outputfile'

if len(sys.argv) != 3:
    Usage()
    sys.exit()
input_file = sys.argv[1]
output_file = sys.argv[2]
file_handler = open(input_file,'r')
content = file_handler.readlines()
#print content[-1]
if content[-1][-1] != '\n':
    #print content[-1][-1]
    content[-1]+='\n'
file_handler.close()

random.shuffle(content)

file_handler = open(output_file, 'w')
file_handler.writelines(content)
file_handler.close()

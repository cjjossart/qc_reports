import re
import os
import sys
import argparse
import pandas as pd

# take input
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('infile', type=argparse.FileType('r'), nargs='*')

args = parser.parse_args()


print(args.infile)
for f in args.infile:
# Need to point to each specific file for each pooint of data
# Probably have if statements of where statments for each text file
    for line in f:
        print(line)


path = os.abspath(sys.argv[1])
print(path)
    # process file...
#print(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])
#print(sys.argv[4])

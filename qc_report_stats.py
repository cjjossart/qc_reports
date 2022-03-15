from importlib.resources import path
import re
import os
import sys
import argparse
import pandas as pd

# take input
parser = argparse.ArgumentParser(description=__doc__)

#parser.add_argument('infile', type=argparse.FileType('r'), nargs='*')

parser.add_argument('--stats', type=argparse.FileType('r'))
parser.add_argument('--base_content_before_trim', type=argparse.FileType('r'))
parser.add_argument('--base_content_after_trim', type=argparse.FileType('r'))
parser.add_argument('--qual_scores_before_trim', type=argparse.FileType('r'))
parser.add_argument('--qual_scores_after_trim', type=argparse.FileType('r'))
# parser.add_argument('--path', type=argparse.FileType('r'))
args = parser.parse_args()

#print(args.stats)
list = []
#count = 0
for lines in args.stats:
# Need to point to each specific file for each pooint of data
# Probably have if statements of where statments for each text file
    #count += 1
    #print(count, lines)
    list.append(lines)
    # reads_before_trim = lines[1].split(" ")[2]
    # print(reads_before_trim)
print(list)
reads_before_trim = list[1].split(" ")[2]
print("reads_before_trim: ", reads_before_trim )

read_length_before_trim = list[3].split(" ")[2]
print("read_length_before_trim: ", read_length_before_trim)

reads_after_trim = list[6].split(" ")[2]
print("reads_after_trim: ", reads_after_trim)

paired_reads_after_trim = list[9].split(" ")[5]
print("paired_reads_after_trim: ", paired_reads_after_trim)

unpaired_reads_after_trim = list[11].split(" ")[5]
print("unpaired_reads_after_trim: ", unpaired_reads_after_trim)

coverage_numer = float(read_length_before_trim) * float(reads_before_trim)
print("coverage_numer: ", coverage_numer)

    #for line in f:
    #    print(line)

# base_content_before_trim
df = pd.read_csv(args.base_content_before_trim,
                 delim_whitespace=True, header=None, index_col=None)
#print(df)
df_subset = df[df[0] == "GC"]
df_subset[3] = df[1] * df[2]

#print(df_subset)
sum_reads = sum(df_subset[2])
sum_reads_GC_content = sum(df_subset[3])
GC_content = (sum_reads_GC_content) / (sum_reads)
print("GC content", GC_content)

# base_content_after_trim
df = pd.read_csv(args.base_content_after_trim,
                 delim_whitespace=True, header=None, index_col=None)
#print(df)
df_subset = df[df[0] == "GC"]
df_subset[3] = df[1] * df[2]

#print(df_subset)
sum_reads = sum(df_subset[2])
sum_reads_GC_content = sum(df_subset[3])
GC_content = (sum_reads_GC_content) / (sum_reads)
print("GC content", GC_content)

# qual_scores_before_trim
f = pd.read_csv(args.qual_scores_before_trim,
                delim_whitespace=True, index_col=None)

f['x'] = f['Score']*f['readsNum']

sum_reads_num = sum(f['readsNum'])
print("sum of reads: ", sum_reads_num)

phred_avg = sum(f['x'])/sum_reads_num
#print("phred quality score: ", f)
print("phred average: ", phred_avg)

# qual_scores_after_trim
f = pd.read_csv(args.qual_scores_after_trim,
                delim_whitespace=True, index_col=None)

f['x'] = f['Score']*f['readsNum']

sum_reads_num = sum(f['readsNum'])
print("AFTER sum of reads: ", sum_reads_num)

phred_avg = sum(f['x'])/sum_reads_num
#print("phred quality score: ", f)
print("AFTER phred average: ", phred_avg)
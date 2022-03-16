from genericpath import sameopenfile
from importlib.resources import path
import re
import os
import sys
import argparse
import pandas as pd

# take input
# Separate function to parse args
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--sample')
parser.add_argument('--stats', type=argparse.FileType('r'))
parser.add_argument('--base_content_before_trim', type=argparse.FileType('r'))
parser.add_argument('--base_content_after_trim', type=argparse.FileType('r'))
parser.add_argument('--qual_scores_before_trim', type=argparse.FileType('r'))
parser.add_argument('--qual_scores_after_trim', type=argparse.FileType('r'))
parser.add_argument('--reference', type=argparse.FileType('r'))

args = parser.parse_args()

# Separate function to produce list or dataframe for metrics, need to read in reference
# Stats file
sample_name = args.sample

# Print
header = None
length = 0
for line in args.reference:
    # Trim newline
    line = line.rstrip()
    if line.startswith('>'):
        # If we captured one before, print it now
        if header is not None:
            print(header, length)
            length = 0
        header = line[1:]
    else:
        length += len(line)
# Don't forget the last one
if length:
    print("Reference Length :", length)


list = []
for lines in args.stats:
    list.append(lines)
reads_before_trim = list[1].split(" ")[2]
print("reads_before_trim: ", reads_before_trim.strip('\n') )
read_length_before_trim = list[3].split(" ")[2]
print("read_length_before_trim: ", read_length_before_trim)
reads_after_trim = list[6].split(" ")[2]
print("reads_after_trim: ", reads_after_trim)
read_length_after_trim = list[8].split(" ")[3]
print("read_length_after_trim: ", read_length_after_trim)
paired_reads_after_trim = list[9].split(" ")[5]
print("paired_reads_after_trim: ", paired_reads_after_trim)
unpaired_reads_after_trim = list[11].split(" ")[5]
print("unpaired_reads_after_trim: ", unpaired_reads_after_trim)
coverage_numer = float(read_length_before_trim) * float(reads_before_trim)
print("coverage_numer: ", coverage_numer)
coverage = coverage_numer / length
print("Coverage :", coverage)

# base_content_before_trim
df = pd.read_csv(args.base_content_before_trim,
                 delim_whitespace=True, header=None, index_col=None)

df_subset = df[df[0] == "GC"]
df_subset[3] = df[1] * df[2]

#print(df_subset)
sum_reads = sum(df_subset[2])
sum_reads_GC_content = sum(df_subset[3])
GC_content_before = (sum_reads_GC_content) / (sum_reads)
print("GC content_before", GC_content_before)

# base_content_after_trim
df = pd.read_csv(args.base_content_after_trim,
                 delim_whitespace=True, header=None, index_col=None)
#print(df)
df_subset = df[df[0] == "GC"]
df_subset[3] = df[1] * df[2]

#print(df_subset)
sum_reads = sum(df_subset[2])
sum_reads_GC_content = sum(df_subset[3])
GC_content_after = (sum_reads_GC_content) / (sum_reads)
print("GC content after", GC_content_after)

# qual_scores_before_trim
f = pd.read_csv(args.qual_scores_before_trim,
                delim_whitespace=True, index_col=None)

f['x'] = f['Score']*f['readsNum']

sum_reads_num = sum(f['readsNum'])
print("sum of reads: ", sum_reads_num)

phred_avg_before = sum(f['x'])/sum_reads_num
#print("phred quality score: ", f)
print("phred average before: ", phred_avg_before)

# qual_scores_after_trim
f = pd.read_csv(args.qual_scores_after_trim,
                delim_whitespace=True, index_col=None)

f['x'] = f['Score']*f['readsNum']

sum_reads_num = sum(f['readsNum'])
print("AFTER sum of reads: ", sum_reads_num)

phred_avg_after = sum(f['x'])/sum_reads_num
#print("phred quality score: ", f)
print("phred average after: ", phred_avg_after)

# Function to combine dataframes together
df = pd.dataframe = {'Sample Name': sample_name, 'Reads Before Trimming': reads_before_trim , 'GC Before Trimming': GC_content_before, 'Average Phred Before Trimming': phred_avg_before, 'Reads After Trimming': reads_after_trim, 'Paired Reads After Trimming': paired_reads_after_trim, 'Unpaired Reads After Trimming': unpaired_reads_after_trim, 'GC After Trimming': GC_content_after,'Average Phred After Trimming': phred_avg_after,'Coverage After Trimming': coverage}

print(df)
#t\\t# \\t# \\t# \\t

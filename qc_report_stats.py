#! /usr/bin/env python3

open(*stats.txt)
# read input
# Look into collection of read in them
# Open *stats.txt file 
    # initialize variables
    # reads before trimming and add to array
    # reads after trimming and add to array 
    # Paired reads after trimming
    # unpaired reads after trimming
    # output the numerator (reads count * reads avg length)  for the coverage calculation to be divided by reference length in the module
    # 
# Close *stats.txt file

# Open *base_content.txt
    # parse only GC lines and calculate average GC content
    # Collect the percentages of GC content
    # Collect the frequencey of reads with specific GC content
        # Multply the percenatage columns by the frequency columns
        # Sum the frequencies
        # Sum the (percentages*frequncies)
        # divide the (sum(percentages)*sum(frequncies)) by total frequencies
# Close *base_content.txt

# Open qa*base_content.txt
    # parse only GC lines and calculate average GC content
    # Collect the percentages of GC content
    # Collect the frequencey of reads with specific GC content
        # Multply the percenatage columns by the frequency columns
        # Sum the frequencies
        # Sum the (percentages*frequncies)
        # divide the (sum(percentages)*sum(frequncies)) by total frequencies
# Close qa*base_content.txt

# Open *for_qual_histograms.txt
    # Collect the PHRED scores
    # Collect the frequencey of reads with specific PHRED content
        # Multply the PHRED columns by the frequency columns
        # Sum the frequencies
        # Sum the (PHRED*frequncies)
        # divide the (sum(PHRED)*sum(frequncies)) by total frequencies
# Close *for_qual_histograms.txt

# Open qa*for_qual_histograms.txt
    # Collect the PHRED scores
    # Collect the frequencey of reads with specific PHRED content
        # Multply the PHRED columns by the frequency columns
        # Sum the frequencies
        # Sum the (PHRED*frequncies)
        # divide the (sum(PHRED)*sum(frequncies)) by total frequencies
# Close qa*for_qual_histograms.txt

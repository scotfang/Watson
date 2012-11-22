#!/usr/bin/env python

import random
import linecache
import sys
import os
from gen_csv_header import gen_attribute_header

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def split_data(data_f, chunk_size, line_count):
    #Shuffle the lines of a data_f and split it into n_chunks 
    #line_count - the total number of lines in the file (do "wc -l data_f"

    chunk_size = int(chunk_size)
    line_count = int(line_count)

    lines = range(1, line_count+1)      
    random.shuffle(lines)

    path, basename = os.path.split(data_f)

    header = gen_attribute_header()
    for idx, chunk in enumerate(chunks(lines, chunk_size)):    
        dump_f = "c%d_l%d_%s" % (idx+1, len(chunk), basename)
        dump_f = os.path.join(path, dump_f)
        with open(dump_f, "wb") as f:
            print "Dumping to", f.name
            f.write(header)
            for li, line in enumerate(chunk):
                f.write(linecache.getline(data_f, line))
                if li and li%1000 == 0:
                    print "Dumped %d lines" % li

if __name__ == "__main__":
    split_data(sys.argv[1], sys.argv[2], sys.argv[3])

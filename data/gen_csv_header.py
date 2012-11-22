#!/usr/bin/env python

def gen_attribute_header():
    #generate Watson CSV attribute header
    h = "ID,"
    for i in range(1, 342):
        h += "f%d," % i 
    h += "TRUTH\n" 
    return h
if __name__ == "__main__":
    print gen_attribute_header()

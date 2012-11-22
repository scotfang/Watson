#!/bin/bash -ex

#splits watson data into 8 chunks
#./split_data.py data.csv 164301 1314407

#converts .csv chunks to arff
CHUNKS=`find -name "c*.csv"` 

for c in $CHUNKS
do
    ARFF=`echo $c | sed "s/csv$/arff/"`
    java -Xmx6000M weka.core.converters.CSVLoader -N 343 $c > $ARFF
done


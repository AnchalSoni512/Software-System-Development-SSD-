#!/bin/bash

read input
output=`echo $input | tr -d "(" | tr -d ")"`
#output=`echo $input | tr -s "()"""`
#output=`echo $output | sed -e 's/^[[:space:]]*//'`


#echo "(" $output ")"
echo "($output)"

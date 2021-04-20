#!/bin/bash

#function pow()
#{
# power=`echo "$power ^ $var" | bc`
# echo $power
#}
#for var in "$@"
#do
#pow $power $var #calling power function for every input
#echo
#echo $power
#echo
#done

power=1
for var in "$@"
do
power=`echo "$var"*"$power" | bc`
done
power=`echo "$power"/"$1" | bc`
echo "$1"^"$power" | bc


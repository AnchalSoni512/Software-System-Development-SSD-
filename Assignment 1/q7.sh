#!/bin/bash

#echo number of pids?
read -p ": " varname

ps -au | awk '{print $2}'| grep -v "PID" > pid.txt 

count=$( wc -l < pid.txt )
#echo $count

if [ $varname -lt $count ]
then
head -$varname pid.txt
else

varname=$count
echo "input exceeded the total process ids, total pid count: "
echo $varname
fi




#!/bin/bash
#echo "Enter your string: "
compgen -c > command.txt 
read input
var1=$(echo $input | grep -o . | sort | tr -d "\n")

find=0
#cat command.txt | while read line || [[ -n $line ]];
for item in $(cat command.txt);
do
	
	if [ ${#var1} -ne ${#item} ]
	then continue
	
	else
	   var2=$(echo $item | grep -o . | sort | tr -d "\n")
	   if [ "$var1" == "$var2" ]
		then
 	 	    echo Yes
 	 	    find=1
 	 	    echo $item
 	            break
	
	   fi
        fi
done
cmp=0
if [ $find -eq $cmp ]
then 
    echo no
fi


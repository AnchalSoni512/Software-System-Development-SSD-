#!/bin/bash

read operator
read numOfOp

i=0
arr=()

while [ $i -lt $numOfOp ]
do
    read x
    arr[$i]=$x
    i=$(($i+1))
done

result=0
    
if [[ $operator = "/" ]]
    then   
        j=0
        result=${arr[$j]}
        j=`expr $j + 1`
        while [ $j -lt $numOfOp ]
        do
            result=`echo "$result/${arr[$j]}" | bc -l`
            j=$(($j+1))
        done

elif [[ $operator = "*" ]]
then
        j=0
        result=1
        while [ $j -lt $numOfOp ]
        do 
            result=$(($result*${arr[$j]}))
            j=$(($j+1))
        done

elif [[ $operator = "+" ]]
then   
        j=0
        result=0
        while [ $j -lt $numOfOp ]
        do
            result=$(($result+${arr[$j]}))
            j=$(($j+1))
        done

elif [[ $operator = "-" ]]
    then   
        j=0
        result=${arr[$j]}
        j=`expr $j + 1`
        while [ $j -lt $numOfOp ]
        do
            result=$(($result-${arr[$j]}))
            j=$(($j+1))
        done

fi
#printing result here with precision
printf '%.4f\n' $result


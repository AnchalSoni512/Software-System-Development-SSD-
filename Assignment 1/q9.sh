#!/bin/bash
read input
count=$(echo $input | tr -d ' ' | wc -c)
res=$(echo $input | tr -d ' ' | rev)
k=0
sum=0
for ((c=0; c<$count-1; c++))
do
    if ! [[ ${res:$c:1} =~ [0-9] ]]
    then 
        echo "wrong input";
        exit 1
    fi

    if [ `expr $c % 2` != 0 ]
    then    
        k=`expr ${res:$c:1} \* 2`
        if [ $k -gt 9 ]
        then 
            k=`expr $k - 9`
        fi
    else
        k=${res:$c:1}
    fi

    sum=`expr $sum + $k`
done
if [ `expr $sum % 10` == 0 ]
then 
    echo "Valid"
else
    echo "Invalid"
fi

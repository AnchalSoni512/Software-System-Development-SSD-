#!/bin/bash

#echo "enter a string to check if it is pallindrome"
read test;
test1=${test,,}
palin=$(echo $test1 | rev)
if [ $test1 = $palin ]
then
   echo "Yes"
else
   echo "No"
fi

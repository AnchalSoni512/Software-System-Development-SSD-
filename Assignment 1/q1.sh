#!/bin/bash

 mkdir Assignment1
 cd Assignment1
 
#b. create 5 empty files in a single command
 touch lab{1..5}.txt

#c. rename the above files 
find *.txt | awk -F . '{system("mv "$0" "$1".c")}'
 
#d. List the content of your current directory in long list format sorted in increasing order of file size.
 ls -laSh -r
 
#e. Display all files and folders inside Homedirectory (~)up to two levels of depth such that full path is displayed for each file/folder
find /home  -maxdepth 2 -name '*' 
 
#f. Display all ‘.txt’ files inside directory ‘Assignment1’ such that full path is displayed foreach file/folder.
ls -d $PWD/*.txt

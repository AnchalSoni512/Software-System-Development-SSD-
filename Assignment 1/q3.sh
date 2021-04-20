#!/bin/bash

cat ~/.bash_history | tail | awk '{CMD[$1]++;}END { for (a in CMD) print CMD[a] " " a ;}' | grep -v "./" | column -c3 -s " " -t | sort -nr |  head -n10

#cat ~/.bash_history | tail -n 10 | awk 'BEGIN {FS="[ \t]+|\\|"} {print $1 "" $2}' | sort | uniq -c | sort -nr | awk '{print $2 " " $1}'

#!/bin/bash
crontab $1 > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo YES
else
    echo NO
fi


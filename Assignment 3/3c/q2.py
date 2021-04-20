import re
import sys

file1 = open('date_calculator.txt', 'r') 
Lines = file1.readlines()

month =	{ "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,"Nov": 11, "Dec": 12 }
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ] 

# def inputvalidate():
n = len(sys.argv)
if(n == 1):
    flag=0 #flag == 0 means default mode dd/mm/yy, flag == 1 means mm/dd/yyyy
elif(n==2):
    if(sys.argv[1][0] == 'm'):
        flag = 1
    elif(sys.argv[1][0] == 'd'):
        flag = 0
    else:
        print("Enter a valid date format!")
        exit(0)
else:
    print("Invalid command line argument!")
    exit(0)

def printing(days1, days2):
    outF = open("output.txt", "a")
    outF.write("Date difference: ")
    outF.write(str(abs(days2-days1)))
    outF.write(" day(s)\n")
    outF.close()
    file1.close()

def countLeapYears(y,m): 
    if (m <= 2): 
        y-= 1
    return int(y // 4 - y // 100 + y // 400 ) 

def four(li):
    # li = arr[0]
    dt1=int(li[1][:-2])
    mo1=month[li[2][0:3]]
    year1=int(li[3][0:4])
    
    days1 = dt1 + (year1) * 365 
    for i in range(0, mo1 - 1) : 
        days1 += monthDays[i]
    days1 += countLeapYears(year1, mo1)
    return days1

def two(li):
    dt = re.findall(r"[\w']+", li)
    if(flag == 0):
        dt2 = int(dt[0])
        mo2 = int(dt[1])
    else:
        mo2 = int(dt[0])
        dt2 = int(dt[1])
    year2 = int(dt[2])

    days2 = dt2 + (year2) * 365 
    for i in range(0, mo2 - 1) :
        days2 += monthDays[i]
    days2 += countLeapYears(year2, mo2)
    return days2

def start():
    arr=[]
    for line in Lines: 
        arr.append(line.split(' '))
    if(len(arr[0]) == 4):
        days1=four(arr[0])
    else:
        days1=two(arr[0][1])

    if(len(arr[1]) == 4):
        days2=four(arr[1])
    else:
        days2=two(arr[1][1])

    printing(days1,days2)
    
# inputvalidate()
count = 0
start()
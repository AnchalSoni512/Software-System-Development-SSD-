import re

file1 = open('date_calculator.txt', 'r') 
Lines = file1.readlines()
# print(type(Lines)) #list type

month =	{ "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,"Nov": 11, "Dec": 12 }
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ] 

def countLeapYears(y,m): 
    if (m <= 2): 
        y-= 1
    return int(y // 4 - y // 100 + y // 400 ) 

count = 0
arr=[]
# Strips the newline character 
for line in Lines: 
    arr.append(line.split(' '))
# print(len(arr[0]))
# print(len(arr[1]))
if(len(arr[0]) == 4 and len(arr[1]) == 4): #first two format
    
    li = arr[0]
    dt1=int(li[1][:-2])
    mo1=month[li[2][0:3]]
    year1=int(li[3][0:4])

    li = arr[1]
    dt2=int(li[1][:-2])
    mo2=month[li[2][0:3]]
    year2=int(li[3][0:4])
   
    days1 = dt1 + (year1) * 365 
    for i in range(0, mo1 - 1) : 
        days1 += monthDays[i]
    days1 += countLeapYears(year1, mo1)

    days2 = dt2 + (year2) * 365 
    for i in range(0, mo2 - 1) : 
        days2 += monthDays[i]
    days2 += countLeapYears(year2, mo2)

elif(len(arr[0]) == 4 and len(arr[1]) == 2):
    li = arr[0]
    dt1=int(li[1][:-2])
    mo1=month[li[2][0:3]]
    year1=int(li[3][0:4])

    li = arr[1][1]
    dt = re.findall(r"[\w']+", li)
    dt2 = int(dt[0])
    mo2 = int(dt[1])
    year2 = int(dt[2])

    days1 = dt1 + (year1) * 365 
    for i in range(0, mo1 - 1) : 
        days1 += monthDays[i]
    days1 += countLeapYears(year1, mo1)

    days2 = dt2 + (year2) * 365 
    for i in range(0, mo2 - 1) : 
        days2 += monthDays[i]
    days2 += countLeapYears(year2, mo2)

elif(len(arr[0]) == 2 and len(arr[1]) == 4):
    li = arr[0][1]
    dt = re.findall(r"[\w']+", li)
    dt1 = int(dt[0])
    mo1 = int(dt[1])
    year1 = int(dt[2])

    li = arr[1]
    dt2=int(li[1][:-2])
    mo2=month[li[2][0:3]]
    year2=int(li[3][0:4])

    days1 = dt1 + (year1) * 365 
    for i in range(0, mo1 - 1) : 
        days1 += monthDays[i]
    days1 += countLeapYears(year1, mo1)

    days2 = dt2 + (year2) * 365 
    for i in range(0, mo2 - 1) : 
        days2 += monthDays[i]
    days2 += countLeapYears(year2, mo2)


else: #last two format
    
    li = arr[0][1]
    dt = re.findall(r"[\w']+", li)
    dt1 = int(dt[0])
    mo1 = int(dt[1])
    year1 = int(dt[2])

    li = arr[1][1]
    dt = re.findall(r"[\w']+", li)
    dt2 = int(dt[0])
    mo2 = int(dt[1])
    year2 = int(dt[2])

    days1 = dt1 + (year1) * 365 
    for i in range(0, mo1 - 1) : 
        days1 += monthDays[i]
    days1 += countLeapYears(year1, mo1)

    days2 = dt2 + (year2) * 365 
    for i in range(0, mo2 - 1) : 
        days2 += monthDays[i]
    days2 += countLeapYears(year2, mo2)

outF = open("output.txt", "a")
outF.write("Date difference: ")
outF.write(str(abs(days2-days1)))
outF.write(" day(s)\n")
outF.close()

file1.close()
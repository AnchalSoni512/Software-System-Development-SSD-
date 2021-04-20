import ast

file = open("Employee1.txt", "r")
contents = file.read()
dic = ast.literal_eval(contents)
file.close()

for i in dic : 
    empname1=i #name of the employee1 stored here type = string
datedic1 = dic[empname1] #type = dict

for i in datedic1 : 
    date1=i #type = str

file = open("Employee2.txt", "r")
contents = file.read()
dic = ast.literal_eval(contents)
file.close()

for i in dic : 
    empname2=i #name of the employee2 stored here type = string

datedic2 = dic[empname2]  #type = dict

for i in datedic2 : 
    date2=i #type = str

t1=[]
t2=[]
sym1 = "AM"
sym2 = "PM"
o = int(1)
z = int(0)

if (date1 != date2):
    print("dates are different, no common slots available")
    exit()

t1 = datedic1[date1] #list
t2 = datedic2[date2] #list
# t1 and t2 keeping list of times
test=[]
for i in range(0,len(t1)):
   test=test+t1[i].split(" - ")
t1 = test

test=[]
for i in range(0,len(t2)):
   test=test+t2[i].split(" - ")
t2 = test

free1=[]
free2=[]
freeslot1=[]
freeslot2=[]

# print(t1)
# print(t2)

if(t1[0] != "9:00AM" and t1[0] != "09:00AM"):
    free1.append("9:00AM - "+ t1[0])
    for i in range(1,len(t1)-1,2):
        if(t1[i] != t1[i+1]):
            free1.append(t1[i] + " - " + t1[i+1])
        # i=i+1
    if(t1[len(t1)-1] != "5:00PM"):
        free1.append(t1[len(t1)-1] + " - 5:00PM")
    # print(t1[len(t1)-1])
else:
    for i in range(1,len(t1)-1,2):
        if(t1[i] != t1[i+1]):
            free1.append(t1[i] + " - " + t1[i+1])
        # i=i+1
    if(t1[len(t1)-1] != "5:00PM" and t2[len(t2)-1] != "05:00PM"):
        free1.append(t1[len(t1)-1] + " - 5:00PM")


if(t2[0] != "9:00AM" and t2[0] != "09:00AM"):
    free2.append("9:00AM - "+ t2[0])
    for i in range(1,len(t2)-1,2):
        if(t2[i] != t2[i+1]):
            free2.append(t2[i] + " - " + t2[i+1])
        # i=i+1
    if(t2[len(t2)-1] != "5:00PM" and t2[len(t2)-1] != "05:00PM"):
        free2.append(t2[len(t2)-1]+" - 5:00PM")
else:
    for i in range(1,len(t2)-1,2):
        if(t2[i] != t2[i+1]):
            free2.append(t2[i] + " - " + t2[i+1])
        # i=i+1
    if(t2[len(t2)-1] != "5:00PM"):
        free2.append(t2[len(t2)-1]+" - 5:00PM")

# print(t1)
# print(t2)
# print(free1)
# print(free2)
# print(str(free1))
# print(str(free2))

freeslot1=free1
freeslot2=free2

test=[]
for i in range(0,len(free1)):
   test=test+free1[i].split(" - ")
free1 = test

test=[]
for i in range(0,len(free2)):
   test=test+free2[i].split(" - ")
free2 = test

ul1=[]
for i in free1:
    # print(type(i))
    i=i.replace(":",'')
    i=i.replace("30","50")
    i=i.split(" ")
    ul1=ul1+i

fl1=[]
for i in ul1:  
    if(i[len(i)-2:] != "PM"):
        i=i[:-2]            
        i=int(i)
        fl1.append(i)
    else:
        i=i[:-2]
        i=int(i)
        if(i<1200):
            i=i+1200
        fl1.append(i)
# print(ul1)
# print(fl1)

ul2=[]
for i in free2:
    i=i.replace(":",'')
    i=i.replace("30","50")
    i=i.split(" ")
    ul2=ul2+i

fl2=[]
for i in ul2:   

    if(i[len(i)-2:] != "PM"):
        i=i[:-2]            
        i=int(i)
        fl2.append(i)
    else:
        i=i[:-2]
        i=int(i)
        if(i<1200):
            i=i+1200
        fl2.append(i)

# print(ul2)
# print(fl2)

slot=float(input())
slot=int(slot*2)

numlist1=[]
for i in fl1:
    i=i-900
    i=int(i/50)
    numlist1.append(i)
chklist1=[]
for i in range(0,16):
    chklist1.append(0)

numlist2=[]
for i in fl2:
    i=i-900
    i=int(i/50)+z
    numlist2.append(i)
chklist2=[]
for i in range(0,16):
    chklist2.append(0) 

i=0
while i<len(numlist1)-1:
    for j in range(numlist1[i],numlist1[i+1]):
        chklist1[j] = 1
    i=i+2

i=0
while i<len(numlist2)-1:
    for j in range(numlist2[i],numlist2[i+1]):
        chklist2[j] = 1
    i=i+2

count=0
for i in range(0,16):
    if(chklist1[i]==1 and chklist2[i]==1):
        count=count+1
        if(count == slot):
            break
    else:
        count=0

timeslot=['9:00AM','9:30AM','10:00AM','10:30AM','11:00AM','11:30AM','12:00PM','12:30PM','1:00PM','1:30PM','2:00PM','2:30PM','3:00PM','3:30PM','4:00PM','4:30PM','5:00PM']


if(count==slot):
    end = i+1
    start = end-slot
    duration = timeslot[start] + " - " + timeslot[end]
    durationlist=[duration]
    dic = {date1:durationlist}
else:
    dic="No Common Slot Available"

slot=slot/2

f1=open("output.txt","a")
f1.write("\nAvailable slot\n")
f1.write(empname1+": "+ str(freeslot1)+"\n")
f1.write(empname2+": "+ str(freeslot2)+"\n\n")
f1.write("Slot Duration: " + str(slot) + " hours\n")
f1.write(str(dic) + "\n")
f1.close()
import ast
import os 
emparr = os.listdir('Employee') #list containing names of .txt files
# print(emparr)
empnamelist=[] #list contains names of all employees fron different .txt files
datelist=[]    #list contains dates of all employees
chklist=[]  #list containing records of free slots of all employees
freetimeslot =[] #list containing free slots for printing purpose
timeslot=['9:00AM','9:30AM','10:00AM','10:30AM','11:00AM','11:30AM','12:00PM','12:30PM','1:00PM','1:30PM','2:00PM','2:30PM','3:00PM','3:30PM','4:00PM','4:30PM','5:00PM']


def openfile(filename):
# for filename in emparr:
    file = open("Employee/"+ filename,'r')
    contents = file.read()
    dic = ast.literal_eval(contents)
    file.close()
    for i in dic:
        empname=i
        empnamelist.append(empname)
    datedic = dic[empname]
    for i in datedic : 
        date=i
        datelist.append(date)
    t = dic[empname][date]
    # print(empname)
    # print(date)
    # print(t)
    return t
    
def tokenseperator(liist):
    test=[]
    for i in range(0,len(liist)):
        test=test+liist[i].split(" - ")
    liist = test
    return liist

def fun2(freeslot,liist):
    for i in range(1,len(liist)-1,2):
        if(liist[i] != liist[i+1]):
            freeslot.append(liist[i] + " - " + liist[i+1])
    if(liist[len(liist)-1] != "5:00PM"):
        freeslot.append(liist[len(liist)-1] + " - 5:00PM")
            
def getfreeslot(liist): #returns freeslots seperated by - 
    freeslot=[]
    if(liist[0] != "9:00AM" and liist[0] != "09:00AM"):
        freeslot.append("9:00AM - "+ liist[0])
    fun2(freeslot,liist)        
               
    freetimeslot.append(freeslot)
    z=tokenseperator(freeslot)       
    # return freeslot
    return z

def fun1(convertlist1,convertlist2):
    for i in convertlist1:  
        if(i[len(i)-2:] != "PM"):
            i=i[:-2]            
            i=int(i)
            convertlist2.append(i)
        else:
            i=i[:-2]
            i=int(i)
            if(i<1200):
                i=i+1200
            convertlist2.append(i)

def fun3(numlist,convertlist2):
    for i in convertlist2:
        i=int(i)-int(900)
        i=int(i/50)
        numlist.append(i)

    # return convertlist2
    i=0
    while i<len(numlist)-1:
        for j in range(numlist[i],numlist[i+1]):
            chklist[j] = chklist[j]+1
        i=i+2
    return chklist

def convert(liist):
    convertlist1=[]
    for i in liist:
        # print(type(i))
        i=i.replace(":",'')
        i=i.replace("30","50")
        i=i.split(" ")
        convertlist1=convertlist1+i
    # print(convert2(convertlist1))
    convertlist2=[]
    fun1(convertlist1,convertlist2)
    
    # print(convertlist2)
    numlist=[]
    return fun3(numlist,convertlist2)

def start():
    for i in range(0,16):
        chklist.append(0) #first checklist will contain all 0
    slot=float(input())
    slot=int(slot*2)
    for item in emparr:
        # print(item)
        t=openfile(item)
        # print(datelist)
        if(len(set(datelist)) != 1):
            print("dates mismatch! common slot cant be found")
            exit(0)
        t=tokenseperator(t)
        y=getfreeslot(t)
        x=convert(y)
    # print("chk list for free slots ",x) 

    count=0
    for i in range(0,16):
        if(x[i]==len(empnamelist)):
            count=count+1
            if(count == slot):
                end = i
                break
        else:
            count=0

    if(count==slot):
        end = i+1
        start = end-slot
        duration = timeslot[start] + " - " + timeslot[end]
        durationlist=[duration]
        dic = {datelist[0]:durationlist}
    else:
        dic="No Common Slot Available"

    slot=slot/2

    f1=open("output.txt","a")
    f1.write("\nAvailable slot\n")
    for i in range(len(emparr)):
        f1.write(empnamelist[i]+":"+str(freetimeslot[i])+"\n")
    f1.write("Slot Duration: " + str(slot) + " hours\n")
    f1.write(str(dic) + "\n")
    f1.close()

start()
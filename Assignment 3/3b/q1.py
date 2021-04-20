import json
from functools import reduce

f = open('org.json')
data = json.load(f) 

#recursive function to find parent
def find_p(e1,p1):
    for element in reversed(data):
        li=data[element]
        for item in range(len(li)):
            if(li[item]['name'] == e1):
                if(li[item].get('parent') != None):
                    x=li[item]['parent']
                    p1.append(x)
                else:
                    return
            
    find_p(x,p1)
#function to find the difference between two lists
def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

biglist=[] #list of list of parents of each employee
ip = input()
ip = ip.split()
n = int(ip[0]) #no. of employees
#input error handling done here
if( n != len(ip)-1):
    print("Error in the number of employee mentioned and number of emp id provided!\nValid input format: space seperated numbers where first number is number of employees followed by n emp ids")
    exit(0)
for i in range(1,n):
    if(len(ip[i]) != 3):
        print("invalid emp id entered")
        exit(0)

for i in range(1,n+1):
    p1=[]
    find_p(ip[i],p1)
    biglist.append(p1)

#res to store common leaders of all employees
res = list(reduce(lambda i, j: i & j, (set(x) for x in biglist)))

inc=1 #incrementer to increment for each input
if(len(res) == 0):#len(res) is zero if no common emp is there
    print("leader not found!")
    exit(0)
else:
    li1 = biglist[0] #can chose any list for the purpose ant at this point it is sure that no sublist will be empty
    li3 = Diff(li1,Diff(li1, res))#doing this to maintain the order
    led = li3[0] #gets closest common leader here
    print("common leader: "+led)
    for i in biglist:
        for j in range(len(i)):
            if(i[j] == led):
                print("leader "+led+" is "+str(j+1)+" level(s) above from " + str(ip[inc]))
                inc=inc+1
f.close()
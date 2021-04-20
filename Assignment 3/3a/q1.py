import json

f = open('org.json')
data = json.load(f) 

x = input()
target1= x
y = input()
target2 = y

p1=[]

#recursive function to find parent
def find_p(e1):

    for element in reversed(data):
        #print(data[element])
        li=data[element]
        print(li)
        # print(li[0]['name'])
        for item in range(len(li)):
            if(li[item]['name'] == e1):
                if(li[item].get('parent') != None):
                    x=li[item]['parent']
                    p1.append(x)
                else:
                    return
            
    find_p(x)


find_p(x)
mylist1=p1
p1=[]

find_p(y)
mylist2=p1

print(mylist1)
print(mylist2)

flag =0
for i in range(0,len(mylist1)):
    for j in range(0,len(mylist2)):
        if mylist1[i] == mylist2[j]:
            print(mylist1[i])
            print("leader "+str(mylist1[i])+" is "+str(i+1)+" level(s) above from " + str(target1))
            print("leader "+str(mylist2[j])+" is "+str(j+1)+" level(s) above from " + str(target2))
            flag = 1
            break
    if flag==1:
        break
if flag == 0:
    print("leader not found")

f.close()
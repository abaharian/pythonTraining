def endswithdot(param):
    n = len(param)
    if param[n-1]==".":
        return True
    return False

def removedotcomma(param):
    param = param.replace('.','')
    param = param.replace(',','')

inpstr = input().split()
n = len(inpstr)
arr = [False for i in range(n)]
for i in range(n):
    if inpstr[i] == inpstr[i].capitalize():
        if i != 0 and endswithdot(inpstr[i-1] == False):
            arr[i] = true

for i in range(n):
    if(arr[i] == True):
        print(i+1,":",removedotcomma(inpstr[i]))

def myPrint(flist, mlist):
    for item in flist:
        print("f", item[0], item[1])
    for item in mlist:
        print("m", item[0], item[1])

mlist = []
flist = []
n = int(input())
for i in range(n):
    line = input()
    listj = line.split('.')    
    name = listj[1].capitalize().strip()
    t = (name, listj[2].strip())    
    if(listj[0] == "f" or listj[0] =='F'):
        flist.append(t)
    else:
        mlist.append(t)
flist.sort(key = lambda x: x[0])
mlist.sort(key = lambda x: x[0])
myPrint(flist, mlist)
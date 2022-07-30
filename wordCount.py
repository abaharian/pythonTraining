def endswithdot(param):
    n = len(param)
    if param[n-1]==".":
        return True
    return False

def removedotcomma(param):    
    param = param.replace('.','')
    param = param.replace(',','')
    return param

inpstr = input().split()
n = len(inpstr)
arr = [False for i in range(n)]
for i in range(n):
    if inpstr[i] == inpstr[i].capitalize():
        if i != 0 and endswithdot(inpstr[i-1]) == False:
            arr[i] = True

for i in range(n):
    if(arr[i] == True):
        print(str(i+1)+":"+removedotcomma(inpstr[i]))


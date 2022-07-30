def findMax(dic):
    sw = False
    for item in dic:
        if(sw):
            if(dic[item]>max):
                max = dic[item]
                maxkey = item
            elif(dic[item] == max and item < maxkey):
                max = dic[item]
                maxkey = item
        else:
            sw = True
            max = dic[item]
            maxkey = item
    return maxkey



n = int(input())
for i in range(n):
    line = input()
    listj = line.split('.')
    for item in listj:
        item = item.lower()
    print(listj)

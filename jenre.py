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



genredic = {
    "Horror" : 0, 
    "Romance" : 0, 
    "Comedy" : 0, 
    "History" : 0, 
    "Adventure" : 0, 
    "Action" : 0
}
n = int(input())
for i in range(n):
    line = input()
    listj = line.split()
    for j in range(1,4):
        genredic[listj[j]] += 1
for i in range(6):
    genre = findMax(genredic)
    print(genre, " : ", genredic[genre])
    genredic.pop(genre)



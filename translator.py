n = int(input())

dic = {}
for i in range(n):
    inplist = input().split()
    dic[inplist[1]] = inplist[0]
    dic[inplist[2]] = inplist[0]
    dic[inplist[3]] = inplist[0]

text = input().split()
length = len(text)
for i in range(length):
    word = text[i]
    if word in dic:
        print(dic[word], end = " ")
    else:
        print(word, end = " ")
print()


def primeCounter(n):
    mul = 2
    counter = 0
    last = n/2
    while(mul < last):
        if(n % mul == 0):
            counter += 1
            while(n % mul == 0):
                n = n // mul            
        mul += 1
    return counter

inp = int(input())
addad = inp
count = primeCounter(addad)
for i in range(9):
    inp = int(input())
    c = primeCounter(inp)
    if(c > count):
        addad = inp
        count = c
    elif(c == count):
        addad = max(addad, inp)

print(addad, " ", count)
        

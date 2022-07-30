x , y = 5 , "it's a mistake"
def myfunc():
    array = [1,2,3]
    i,j,k = array
    global x
    print(x)
    x = 1
    if x < 2:
        print ("Hello World!")
    else :
        #it's just first line of cooment
        #and this is the second line
        print(y)

def typeFunc():
    a = "Hello World!"
    print(a, " ----> ",type(a))
    a = int("54")
    print(a, " ----> ", type(a))
    a = 5.7
    print(a, " ----> ", type(a))
    a = 3+2j
    print(a, " ----> ",type(a))
    a = [1,2,3]
    print(a, " ----> ",type(a))
    a = (1,2,3,4)
    print(a, " ----> ",type(a))
    a = range(6)
    print(a, " ----> ",type(a))
    a = {"name": "john", "age":32}
    print(type(a))
    a = {"salam", "dorood", "Hello"}
    print(a, " ----> ",type(a))
    a = frozenset({"salam", "dorood", "Hello"})
    print(a, " ----> ",type(a))
    a = True
    print(a, " ----> ",type(a))
    a = b"5465"
    print(a, " ----> ",type(a))
    a = bytearray(5)
    print(a, " ----> ",type(a))
    a = memoryview(bytes(5))
    print(a, " ----> ", type(a))
    a = None
    print(a, " ----> ", type(a))
    a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
    print(a, " ----> ", type(a))


def formatFunc():
    quantity = 3
    itemno = 567
    price = 49.95
    myorder = "I want {} pieces of item {} for {} dollars."
    myorder = myorder.format(quantity, itemno, price)
    print(myorder)

def formatFunc2():
    quantity = 3
    itemno = 567
    price = 49.95
    myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
    print(myorder.format(quantity, itemno, price))

#myfunc()
#typeFunc()
formatFunc2()
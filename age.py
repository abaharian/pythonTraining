import datetime

inplist = input().split('/')
year = int(inplist[0])
month = int(inplist[1])
day = int(inplist[2])

if year < 1000 or month < 0 or day < 0:
    print("WRONG")
    exit()
if year > 2021 or month > 12 or day > 31:
    print("WRONG") 
    exit()
birth = datetime.datetime(year, month, day)
today = datetime.datetime.now()
age = today-birth
print (age.days // 365)

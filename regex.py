import re

str = "Hi Steve, Hi Emanuel, Hi Sarah"
res = re.findall(r'[hH]i (\w+),', str)
print(res)

str = 'Iran is in the middle-east.'
result = re.findall(r'iran',str)
print(result)

str = 'i am born in 1973. i am 20 years old now.'
result = re.findall(r'(\d+)',str)
print(result)

str = 'students for passing the exam must have more than 15 grade.'
result = re.findall(r'a*',str)
print(result.count('a') + result.count(''))


str = 'This is an advanced Python programming in Maktabkhooneh.'
result = re.sub(r'[mM]aktabkhooneh','University',str)
print(result)
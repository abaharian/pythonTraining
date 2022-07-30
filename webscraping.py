import requests
import re

page = requests.get("https://far30dl.ir/series/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%D8%B3%D8%B1%DB%8C%D8%A7%D9%84-%D9%82%D8%B5%D9%87-%D9%87%D8%A7%DB%8C-%D8%AA%D8%A7-%D8%A8%D9%87-%D8%AA%D8%A7/")
html = page.text
links = re.findall(r"https://s1\.far30dl\.ir/Serial/Irani/Ta\.Be\.Ta/.*?mp4", html)
for item in links:
    if len(item) > 100:
        continue
    print("downloading:  ", item)    
    file = requests.get(item)
    print("complete")
    filename = re.findall(r"https.*/(.*\.mp4)", item)
    print(filename[0])
    with open(filename[0], 'wb') as f:
       f.write(file.content)     
    


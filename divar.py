import requests
import re

print("start")
site = requests.get("https://divar.ir/s/tehran")
print("request get")
regex = ".*(<div class=\"kt-post-card__body\".*?</div>)"
print("Regex")
res = re.findall(regex, site)
print("match")
print(res)
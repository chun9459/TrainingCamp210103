import urllib.request as request
import json
src = " https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
  data = json.load(response) 

J = data["result"]["results"]
for i in J:
   X = i["file"].split("http:", 2)
   print(X[1] + "\n")

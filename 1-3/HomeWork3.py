import urllib.request as request
import json
src = " https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
  data = json.load(response) 

J = data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
  for i in J:
    X = i["file"].split("http:", 2)
    file.write(i["stitle"] + " , " + i["longitude"] + " , " + i["latitude"] + " , " + "https:" + X[1] + "\n")

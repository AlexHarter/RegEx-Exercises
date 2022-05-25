import re

#https://regex.sketchengine.co.uk/cgi/ex2.cgi

"""
Positive:
rap them
tapeth
apth
wrap/try
sap tray
87ap9th
apothecary

Negative:
aleht
happy them
tarpth
Apt
peth
tarreth
ddapdg
apples
shape the
"""

txt = ["rap them", "tapeth", "apth", "wrap/try", "sap tray", "87ap9th", "apothecary", "aleht", "happy them", "tarpth", "Apt", "peth", "tarreth", "ddapdg", "apples", "shape the"]

for x in txt:
    matches = re.findall(".*ap.?t[hr].*", x) #This works in the web app, why not here?
    print(matches)
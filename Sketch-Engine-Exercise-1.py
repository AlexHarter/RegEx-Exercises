import re

#https://regex.sketchengine.co.uk/cgi/ex1.cgi

"""
Positive:
pit
spot
spate
slap two
respite

Negative:
pt
Pot
peat
part
"""

txt = ["pit", "spot", "spate", "slap two", "respite", "pt", "Pot", "peat", "part"]

for x in txt:
    matches = re.findall(".*p.{1}t.*", x)
    print(matches)
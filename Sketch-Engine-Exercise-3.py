import re

#https://regex.sketchengine.co.uk/cgi/ex3.cgi

"""
Positive:
affgfking
rafgkahe
bafghk
baffgkit
affgfking
rafgkahe
bafghk
baffg kit

Negative:
fgok
a fgk
affgm
afffhk
fgok
afg.K
aff gm
afffhgk
"""

txt = ["affgfking", "rafgkahe", "bafghk", "baffgkit", "affgfking", "rafgkahe", "bafghk", "baffg kit", "fgok", "a fgk", "affgm", "afffhk", "fgok", "afg.K", "aff gm", "afffhgk"]

for x in txt:
    matches = re.findall("[br]?af{1,2}g.?k.*", x)
    print(matches)

import re

def extractAllNumbers(str):
    out = [int(x) for x in re.findall(r"\d+", str)]
    return out

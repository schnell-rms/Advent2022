import re

def extractAllNumbers(str):
    out = [int(x) for x in re.findall(r"\d+", str)]
    return out

def firstNumber(str):
    m = re.search(r"\d+", str)
    return None if m == None else int(m.group(0))

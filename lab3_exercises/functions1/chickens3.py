def count(heads, legs):
    y = (legs - 2*heads)/2
    x = heads - y
    return int(x), int(y)

heads = 35
legs = 94

print(count(heads, legs))


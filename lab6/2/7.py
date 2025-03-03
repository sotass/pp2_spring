with open('ex.txt', 'r') as f:
    l = f.readlines()
with open('ex2.txt', 'a') as f:
    for i in l:
        f.write(i)

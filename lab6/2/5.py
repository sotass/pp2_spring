l = ["red", "blue", "green", "black"]
with open('ex.txt', 'w') as f:
    for i in l:
        f.write(str(i) + "\n")

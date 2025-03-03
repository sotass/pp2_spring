for i in range(26):
    name = chr(65 + i) + '.txt'
    
    with open(name, 'w') as f:
        f.write(f"This is a file named {name}")

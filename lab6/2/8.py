import os
path = '\\Users\sotas\OneDrive\Рабочий стол\pp2_spring\labs\lab6'

def f(path):
    if os.path.exists(path):
        l = os.listdir(path)
        for i in l:
            fullName = os.path.join(path, i)
            if os.path.isfile(fullName):  # Use isdir for directories
                os.remove(fullName)
    else:
        print("The file does not exist")

f(path)
 
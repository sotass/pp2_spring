import os
path = '\\Users\sotas\OneDrive\Рабочий стол\pp2_spring\labs\lab6'
l = os.listdir()

def f(path):
    if not os.path.exists(path):
        print(f"{path} does not exist")
        return

    if os.access(path, os.R_OK):
        print(f"{path} is readable")
    else:
        print(f"{path} is not readable")

    if os.access(path, os.W_OK):
        print(f"{path} is writable")
    else:
        print(f"{path} is not writable")

    if os.access(path, os.X_OK):
        print(f"{path} is executable")
    else:
        print(f"{path} is not executable")

f(path)

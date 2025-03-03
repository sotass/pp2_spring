import os
path = os.getcwd()
os.chdir('\\Users\sotas\OneDrive\Рабочий стол\pp2_spring\labs\lab6')
l = os.listdir()
for i in l:
    if os.path.isfile(i):  
        print(i)

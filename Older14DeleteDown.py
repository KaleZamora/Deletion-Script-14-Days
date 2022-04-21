import os, time, sys

pather = 'c:\\users\\'
holder = []
now = time.time()
for i in os.listdir(pather):
    path2 = 'C:\\users\\'+i
    nogo = [r'C:\users\All Users', r'C:\users\Default', r'C:\users\Default User', r'C:\users\desktop.ini', r'C:\users\Public']
    if path2 not in nogo:
        path3 = path2 + "\\Downloads"
        for j in os.listdir(path3):
            path4 = os.path.join(path3, j)
            if os.path.isfile(path4):
                if os.stat(path4).st_mtime < now - (14*86400):
                    os.remove(path4)


#path3 = path2+ '\\' +j
#if os.stat(path3).st_mtime < now - 14 * 86400:
    #if os.path.isfile(path3):
        #print(path3)
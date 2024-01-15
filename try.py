import psutil
import variabiles

def getproc():
    processlist = list()
    for proc in psutil.process_iter():
        processlist.append(proc.name().lower())
    processlist = list(set(processlist))
    for item in variabiles.windowsProcess:
        try:
            processlist.remove(item.lower())
        except:
            pass
    return processlist

print(getproc())
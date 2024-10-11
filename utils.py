import psutil
import variabiles
import os

def getProc():
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

def killProc(target):
    procs = getProc()
    #os.kill(target.os.getpid(), 1) if target in procs else print("Processo non trovato")

killProc("google chrome")

#print(getProc())
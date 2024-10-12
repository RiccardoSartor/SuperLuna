import os
import psutil

'''
def processes() -> list[psutil.Process]: #ritorna un array di pid-nomeProcesso in esecuzione sul pc
    toSend = []
    for p in psutil.process_iter(): #if p.username() == username]
        try:
            toSend.append((p.pid, p.name()))
        except:
            pass
    return toSend
'''


def processes() -> list[psutil.Process]: #ritorna un array di pid-nomeProcesso in esecuzione sul pc
    toSend = []
    for p in psutil.process_iter(): #if p.username() == username]
        try:
            toSend.append((p.pid, p.name()))
        except:
            pass
    return toSend


def listPidProc(target): #dato un nome di un processo ritorna un array con all'interno tutti i pid dei processi che contenevano il nome
    toKill = []
    for pid in processes():
        if target.lower() in pid[1].lower():
            toKill.append(pid[0])
    return toKill

def killProc(target): #termina i processi dato un nome
    toKill = listPidProc(target)
    for proc in toKill:
        os.kill(proc, 15) #15 sarebbe signal.SIGTERM
    return len(listPidProc(target)) #ritorna il numero di processi contenenti il nome fornito ancora in esecuzione (non killati)


print("OSX Utility loaded")
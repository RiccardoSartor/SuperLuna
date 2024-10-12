import psutil

processes = psutil.process_iter()
for process in processes:
    print(f"Process ID: {process.pid}, Name: {process.name()}")
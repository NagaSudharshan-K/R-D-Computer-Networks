import time
import psutil

def write_to_log(message):
    with open("file.txt", "a") as log_file:
        log_file.write(f"{time.ctime()} - {message}\n")

initial_processes = set(p.name() for p in psutil.process_iter())

while True:
    current_processes = set(p.name() for p in psutil.process_iter())

    if "firefox" in current_processes and "firefox" not in initial_processes:
        write_to_log("Firefox opened")

    if "firefox" not in current_processes and "firefox" in initial_processes:
        write_to_log("Firefox closed")
        break
        
    initial_processes = current_processes

    time.sleep(5) 


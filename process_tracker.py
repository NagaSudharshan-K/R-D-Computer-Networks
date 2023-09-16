import psutil

def list_processes():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        print(f"Process Name: {process.info['name']}, PID: {process.info['pid']}")

if __name__ == "__main__":
    list_processes()


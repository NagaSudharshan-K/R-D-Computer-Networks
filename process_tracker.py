import psutil

def list_web_app_processes():
    web_browsers = ["chrome", "firefox", "msedge"]  
    for process in psutil.process_iter(attrs=['pid', 'name']):
        process_name = process.info['name'].lower()
        for browser in web_browsers:
            if browser in process_name:
                print(f"Web Application Name: {process_name}, PID: {process.info['pid']}")

if __name__ == "__main__":
    list_web_app_processes()

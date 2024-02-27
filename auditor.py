import psutil
from ip2geotools.databases.noncommercial import DbIpCity

def network_monitor():
    processes = psutil.net_connections(kind="inet")

    for process in processes:
        if process.status == "ESTABLISHED" and process.raddr.ip != "127.0.0.1":
            print("=========================")
            print(f"connection found")
            get_process_details(process.pid)
            print("Scanning details in remote host ({process.raddr.ip})")
            get_remote_details(process.raddr.ip)


def get_process_details(pid):
    try:
        process = psutil.Process(pid)

        print(f"[+] Process Name: {process.name}")    
        print(f"[+] Process PID: {process.pid}")    
        print(f"[+] Process Status: {process.status}")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}")
    except psutil.AccessDenied:
        print(f"Access denied to process with PID {pid}")

def get_remote_details(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: Lat: {res.latitude}, Lng: {res.longitude}")

if __name__ =='__main__':
    network_monitor()
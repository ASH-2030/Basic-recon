import socket

def port_scan(ip):
    print(f"[*] Starting port scan on {ip}\n")

    for port in range(1, 1023):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)

            result = s.connect_ex((ip, port))

            if result == 0:
                print(f"[+] Port {port} is OPEN")

            s.close()

        except Exception:
            pass


if __name__ == "__main__":
    target_ip = input("Enter Target IP: ")
    port_scan(target_ip)

import socket

def grab_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #timer
        s.settimeout(2)
        
        print(f"[*] Connecting to {ip} on port {port}...")
        #connection
        s.connect((ip, port))
        
        #like sending request
        try:
            msg = f'GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n'.encode()
            s.send(msg)
        except Exception as e:
            print(f"[!] Error sending trigger: {e}")

        # 4. To receive the banner (buffer size of 1024 bytes)
        banner = s.recv(1024)
        
        print(f"[+] Banner received:\n{banner.decode().strip()}")
        
    except socket.timeout:
        print("[!] Connection timed out. The service might not be sending a banner.")
    except ConnectionRefusedError:
        print(f"[!] Connection refused. Port {port} might be closed.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")
    finally:
        # 5. Always close the socket
        s.close()

if __name__ == "__main__":
    # Take user input
    target_ip = input("Enter Target IP: ")
    target_port = int(input("Enter Target Port: "))
    

    grab_banner(target_ip, target_port)


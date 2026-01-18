import socket

def grab_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        
        print(f"[*] Connecting to {ip} on port {port}...")
        s.connect((ip, port))
        
        msg = f'HEAD / HTTP/1.1\r\nHost: {ip}\r\n\r\n'.encode()
        s.send(msg)
        
        response = s.recv(4096)
        decoded_response = response.decode(errors='ignore')
        
        print(f"[+] Banner received:")
        
        lines = decoded_response.split('\r\n')
        for line in lines:
            
            if not line: continue 
            if line.startswith("Content-type"):
                continue
            
            
            print(line)
            
        
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    target_ip = input("Enter Target IP: ")
    target_port = int(input("Enter Target Port: "))
    grab_banner(target_ip, target_port)

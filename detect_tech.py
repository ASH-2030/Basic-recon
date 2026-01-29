import socket

def detect_technologies(target, port=[80,443]):
    tech = {
        "Web Server": None,
        "Backend": set(),
        "Framework/CMS": set(),
        "HTTP Status": None
    }

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target, port))

        request = (
            f"GET / HTTP/1.1\r\n"
            f"Host: {target}\r\n"
            f"User-Agent: ReconTool\r\n"
            f"Connection: close\r\n\r\n"
        )

        s.send(request.encode())
        response = s.recv(8192).decode(errors="ignore")
        lines = response.split("\r\n")

        for line in lines:
            # status code
            if line.startswith("HTTP/"):
                tech["HTTP Status"] = line

            # server
            if line.startswith("Server:"):
                tech["Web Server"] = line.split(":",1)[1].strip()

            # backend
            if line.startswith("X-Powered-By:"):
                tech["Backend"].add(line.split(":",1)[1].strip())

            # cookies based detection
            if line.startswith("Set-Cookie:"):
                l = line.lower()
                if "phpsessid" in l:
                    tech["Backend"].add("PHP")
                if "asp.net" in l:
                    tech["Backend"].add("ASP.NET")
                if "wordpress" in l:
                    tech["Framework/CMS"].add("WordPress")
                if "laravel" in l:
                    tech["Framework/CMS"].add("Laravel")
                if "django" in l:
                    tech["Framework/CMS"].add("Django")

    except Exception as e:
        return {"Error": str(e)}

    finally:
        s.close()

    return tech


# standalone run
if __name__ == "__main__":
    target = input("Enter target (example.com): ").strip()
    port = int(input("Enter port (80): "))

    result = detect_technologies(target, port)

    print("\n[+] Technology Detection Result\n")

    for k, v in result.items():
        if isinstance(v, set):
            print(f"{k}: {', '.join(v) if v else 'Not detected'}")
        else:
            print(f"{k}: {v if v else 'Not detected'}")

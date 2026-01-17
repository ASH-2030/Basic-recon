import requests
import sys

def get_subdomains(domain):
    print(f"\n[+] Searching crt.sh for subdomains of: {domain}")
    
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"[-] Error fetching data: Status {response.status_code}")
            return

        data = response.json()
        subdomains = set() 

        for entry in data:
            name_value = entry['name_value']
           
            lines = name_value.split('\n')
            for line in lines:
                if '*' not in line: 
                    subdomains.add(line)

        # Sort and Print
        print(f"\n[+] Found {len(subdomains)} unique subdomains:")
        for sub in sorted(subdomains):
            print(sub)

    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_domain = sys.argv[1]
    else:
        target_domain = input("Enter domain : ")
    
    get_subdomains(target_domain)
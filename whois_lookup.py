import whois
import sys

def perform_whois(domain):
    print(f"\n[+] Performing WHOIS lookup for: {domain}")
    try:
        w = whois.whois(domain)
        
        print(f"Registrar:    {w.get('registrar')}") 
        print(f"Creation Date:{w.get('creation_date')}")
        print(f"Expiry Date:  {w.get('expiration_date')}")
        print(f"Name Servers: {w.get('name_servers')}")
        
    except Exception as e:
        print(f"[-] Error during WHOIS lookup: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_domain = sys.argv[1]
    else:
        target_domain = input("Enter domain: ")
    
    perform_whois(target_domain)
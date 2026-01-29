
import argparse
from datetime import datetime


from detect_tech import detect_technologies

# already written just calling the functions
from whois_lookup import perform_whois
from dns_enum import enumerate_dns
from subdomain_enum import get_subdomains
from port_scan import port_scan
from banner import grab_banner

def main():
    parser = argparse.ArgumentParser(description="Custom Reconnaissance Tool")
    parser.add_argument("--target", required=True)
    parser.add_argument("--whois", action="store_true")
    parser.add_argument("--dns", action="store_true")
    parser.add_argument("--subdomains", action="store_true")
    parser.add_argument("--ports", action="store_true")
    parser.add_argument("--banner", action="store_true")
    parser.add_argument("--tech", action="store_true")

    args = parser.parse_args()
    target = args.target

    report = []
    report.append(f"Recon Report for: {target}")
    report.append(f"Timestamp: {datetime.now()}")
    report.append("=" * 40)

    if args.whois:
        report.append("\n[WHOIS]")
        report.append(str(perform_whois(target)))

    if args.dns:
        report.append("\n[DNS ENUMERATION]")
        report.append(str(enumerate_dns(target)))

    if args.subdomains:
        report.append("\n[SUBDOMAIN ENUMERATION]")
        report.append(str(get_subdomains(target)))

    if args.ports:
        report.append("\n[PORT SCAN]")
        report.append(str(port_scan(target)))

    if args.banner:
        report.append("\n[BANNER GRABBING]")
        report.append(str(grab_banner(target, 80)))

    if args.tech:
        report.append("\n[TECHNOLOGY DETECTION]")
        tech = detect_technologies(target, [80,443])
        for t in tech:
            report.append(t)

    with open("report.txt", "w") as f:
        f.write("\n".join(report))

    print("[+] Recon completed")
    print("[+] Report saved as report.txt")

if __name__ == "__main__":
    main()

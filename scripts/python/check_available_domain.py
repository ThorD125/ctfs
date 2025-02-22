import whois

def check_domain_availability(domain):
    try:
        domain_info = whois.whois(domain)
        if domain_info.status:
            print(f"❌ Domain '{domain}' is already registered.")
        else:
            print(f"✅ Domain '{domain}' is available!")
    except whois.parser.PywhoisError:
        print(f"✅ Domain '{domain}' is available!")

if __name__ == "__main__":
    domain = input("Enter a domain name (e.g., example.com): ").strip()
    check_domain_availability(domain)

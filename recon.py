import subprocess
import json

def get_domains():

    domains =[]
    domain_num = 0
    while True:
        domain_num+=1 
        s = input(f"Input {domain_num} domain for scan: ")
        if s == "end":
            break
        else:
            domains.append(s)
    
    return domains

def get_output_file():
    filename = input("Name of the file where you want save subdomains: ")
    return filename

def get_vuln_file():
    filename = input("Name of file where will save vulnerabilities: ")
    print("Your order will be out shortly")
    return filename

def run_subfinder(domain):
    print(f"Starting subfinder...")

    subfinder_result = subprocess.run(
        ["subfinder", "-d", domain, "-silent"],
        capture_output = True,
        text = True
    )

    return subfinder_result.stdout.splitlines()

def run_amass(domain):
    print("Starting amass...")
    
    amass_result = subprocess.run(
        ["amass", "enum", "-passive", "-d", domain],
        capture_output = True,
        text = True
    )

    return amass_result.stdout.splitlines()

def run_assetfinder(domain):
    print(f"Srarting assetfinder...")

    assetfinder_result = subprocess.run(
        ["assetfinder", "--subs-only", domain],
        capture_output=True,
        text=True
    )

    return assetfinder_result.stdout.splitlines()

def run_httpx(subdomains):
    print(f"Starting httpx for domains...")

    process = subprocess.run(
        ["httpx", "-silent", "-status-code", "-no-color"],
        input="\n".join(subdomains),
        text=True,
        capture_output=True
    )

    return process.stdout.splitlines()

def run_nuclei(urls):
    print("Starting nuclei...")
    process = subprocess.run(
        ["nuclei", "-silent", "-no-color", "-json"],
        input="\n".join(urls),
        text=True,
        capture_output=True
    )

    return process.stdout.splitlines()

def parse_nuclei(lines):
    vulns = []

    for line in lines:
        try:
            data = json.loads(line)

            vulns.append({
                "url": data.get("matched-at"),
                "template": data.get("templateID"),
                "severity": data.get("info", {}).get("severity")
            })

        except:
            continue

    return vulns

def main():
    print("Hello! This is my tool that u can use for recon.\n Print \"end\" to stop input domains(you can input more then one)")
    domains = get_domains()
    print("Successful! Did i say u looks pretty today? Ohm sorry. Now please print the:")
    filename = get_output_file()
    vuln_file = get_vuln_file()
    all_subs = []

    for domain in domains:
        subs_one = run_subfinder(domain)
        subs_two = run_assetfinder(domain)
        subs_three = run_amass(domain)

        combo = subs_one + subs_two + subs_three

        print(f"Found {len(combo)} subdomains")

        all_subs.extend(combo)
    
    unique_subs = list(set(all_subs))

    alive = run_httpx(unique_subs)
    nuclei_raw = run_nuclei(unique_subs)
    vulns = parse_nuclei(nuclei_raw)

    print(f"Found {len(vulns)} vulnerabilities")
    with open(filename, "w") as f:
        for sub in alive:
            f.write(sub + "\n")

        print(f"Saved to {filename}")

    if len(vulns) != 0:
        with open(vuln_file, "w") as f:
            for v in vulns:
                f.write(f"{v['severity']} | {v['url']} | {v['template']}\n")
    else:
        print("No vulnerabilities found")
   
    

if __name__ == "__main__":
    main()

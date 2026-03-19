import sys
import requests

existing_users = [] 

def request_onedrive(username, domain, tenantname):   
    try:
        dom, tld = domain.split(".")
    except ValueError:
        print(f"Error : the domain '{domain}' must be like 'domain.com'")
        return
    
    username_replaced = username.replace(".","_")
    url = f"https://{tenantname}-my.sharepoint.com/personal/{username_replaced}_{dom}_{tld}/_layouts/15/onedrive.aspx"

    try:
        response = requests.get(url, timeout=10)
        response_size = len(response.content)

        if response.status_code != 404:
            print(f"→ {username} exists (received {response.status_code})")
            existing_users.append(f"{username}@{domain}")
        
    except requests.exceptions.RequestException as e:
        print(f"[!] Error for {username}@{domain}:", e)


def main():
    if len(sys.argv) != 4:
        print("[i] Usage: python3 enumOnedriveUsers.py users.txt domain.com tenantname")
        sys.exit(1)

    users_file = sys.argv[1]
    domain = sys.argv[2]
    tenantname = sys.argv[3]

    try:
        with open(users_file, "r") as f:
            users = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[-] Error : file not found -> {users_file}")
        sys.exit(1)

    for user in users:
        request_onedrive(user, domain, tenantname)

    print("\n" + "="*70)
    print("[+] EXISTING USERS :")
    if existing_users:
        for u in existing_users:
            print(" -", u)
    else:
        print("[-] No user was found.")
    print("="*70)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import concurrent.futures
import requests
import os

# ===== CONFIG =====
THREADS = 30
TIMEOUT = 6

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

ACTIVE_CODES = {200, 201, 202, 204, 301, 302, 303, 307, 308, 401, 403}


# ===== LOGO =====
def banner():
    print("""
\033[96m
██╗    ██╗██╗███╗   ██╗████████╗███████╗██████╗ 
██║    ██║██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██║ █╗ ██║██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██║███╗██║██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║ ╚████║   ██║   ███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

        ❄️ WINTER AKI - Active Scanner ❄️
\033[0m
""")


# ===== INPUT FUNCTION =====
def get_input_file():
    while True:
        try:
            user_input = input("[?] Enter file path OR file name: ").strip()

            # Full path
            if os.path.isfile(user_input):
                return user_input

            # Current folder
            current_path = os.path.join(os.getcwd(), user_input)
            if os.path.isfile(current_path):
                return current_path

            print("[X] File not found! Try again.\n")

        except:
            print("[X] Error reading input\n")


# ===== NORMALIZE =====
def normalize_domain(line):
    d = line.strip()
    if not d:
        return None

    d = d.replace("http://", "").replace("https://", "")
    d = d.split("/")[0]
    d = d.split(":")[0]

    return d if d else None


# ===== CHECK ACTIVE =====
def is_active(domain):
    for scheme in ("https", "http"):
        try:
            r = requests.get(
                f"{scheme}://{domain}",
                headers=HEADERS,
                timeout=TIMEOUT,
                allow_redirects=True
            )

            if r.status_code in ACTIVE_CODES or (200 <= r.status_code < 600):
                return True
        except:
            continue

    return False


def check_one(domain):
    return domain if is_active(domain) else None


# ===== MAIN =====
def main():
    banner()  # 🔥 Logo first

    input_file = get_input_file()

    output_file = os.path.join(os.getcwd(), "active.txt")

    with open(input_file, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    domains = []
    seen = set()

    for line in raw_lines:
        d = normalize_domain(line)
        if d and d not in seen:
            seen.add(d)
            domains.append(d)

    print(f"\n[*] Total domains loaded: {len(domains)}")
    print(f"[*] Checking with {THREADS} threads...\n")

    active = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = {executor.submit(check_one, d): d for d in domains}

        done = 0
        for future in concurrent.futures.as_completed(futures):
            done += 1
            domain = futures[future]

            try:
                result = future.result()
                if result:
                    active.append(result)
                    print(f"[ACTIVE] {result}")
            except Exception as e:
                print(f"[ERROR] {domain} -> {e}")

            if done % 25 == 0:
                print(f"--- Progress: {done}/{len(domains)} ---")

    active = sorted(set(active))

    with open(output_file, "w", encoding="utf-8") as f:
        for d in active:
            f.write(d + "\n")

    print("\n=======================")
    print(f"[+] Active domains found: {len(active)}")
    print(f"[+] Saved to: {output_file}")
    print("=======================\n")


if __name__ == "__main__":
    main()

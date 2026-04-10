🔍 Subdomain Filter Tool
📌 Description

This tool uses Subfinder to discover subdomains and helps filter them into active and inactive domains for better analysis and reconnaissance.

🚀 Features
🔎 Subdomain enumeration using Subfinder
✅ Identifies active (live) domains
❌ Filters out inactive (dead) domains
⚡ Fast and efficient processing
🛠️ Easy to use
📂 Installation
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git

# Go to the project directory
cd your-repo-name

Make sure you have Subfinder installed:

go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
▶️ Usage
# Basic usage
python3 tool.py -d example.com
Options:
-d → Target domain
🧠 How It Works
Uses Subfinder to collect subdomains
Sends requests to check which domains are alive
Separates results into:
Active domains
Inactive domains
📁 Output
active.txt → Contains all live domains
inactive.txt → Contains all dead domains
⚠️ Disclaimer

This tool is created for educational and ethical purposes only.
Do not use it on targets without proper authorization.

📜 License

No license added — all rights reserved.

If you want, I can also:

add badges (stars, forks, etc.)
make it more professional (like top GitHub projects)
or customize according to your code (Python/Go/etc.)

Just tell me 👍

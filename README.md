# ❄️ WINTER AKI - Active Domain Finder

A fast and simple Python tool to identify **active domains/subdomains** from a given list using multithreading.

---

## 🚀 Features

* ⚡ Fast scanning using multithreading
* 🌐 Supports both `http` and `https`
* 🧠 Smart domain normalization
* 📂 Accepts file path or filename
* 🔥 Clean CLI with banner
* 📊 Progress tracking
* 💾 Saves results automatically

---

## 📦 Installation

Clone the repository:

```bash
             git clone https://github.com/winter3aki/activedomainfinder.git
             python domainfilter.py
```

Install required dependency:

```bash
            pip install requests
```

---

## ▶️ Usage

Run the script:

```bash      
            python domainfilter.py
```

You will be prompted:

```bash   
              [?] Enter file path OR file name:
```

### 📥 Input Example

Your input file should contain domains/subdomains like:

```
example.com
test.example.com
https://google.com
site.com/path
```

---

## 📤 Output

* Active domains will be displayed in terminal
* Saved automatically as:

```
active.txt
```

(in the same directory where script is running)

---

## 🛠️ Configuration

You can modify these values inside the script:

```python
THREADS = 30
TIMEOUT = 6
```

---

## ⚙️ How It Works

1. Takes domain list as input
2. Cleans and normalizes domains
3. Sends HTTP/HTTPS requests
4. Checks response status codes
5. Identifies active domains
6. Saves results to file

---

## 📌 Supported Status Codes

```
200, 201, 202, 204,
301, 302, 303, 307, 308,
401, 403
```

---

## ⚠️ Disclaimer

This tool is for **educational and authorized testing purposes only**.
Do not use it against systems without permission.

---

## 👨‍💻 Author

**Winter AKI**

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🛠️ Contribute

---

## 🔗 Repository

👉 https://github.com/winter3aki/activedomainfinder.git

---

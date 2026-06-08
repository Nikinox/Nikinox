import requests
from bs4 import BeautifulSoup

owner = str(input("enter owner"))
repo = str(input("enter repo"))
branch = str(input("enter branch"))

BASE = "https://github.com"
RAW = "https://raw.githubusercontent.com"

def scan_folder(url):
    results = {}  # path → byte_size

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    for a in soup.find_all("a", class_="Link--primary"):
        href = a.get("href")

        # FILE
        if "/blob/" in href:
            path = href.split(f"/blob/{branch}/")[1]

            raw_url = f"{RAW}/{owner}/{repo}/{branch}/{path}"

            content = requests.get(raw_url).content

            results[path] = len(content)

        elif "/tree/" in href:
            folder_url = f"{BASE}{href}?plain=1"

            sub_results = scan_folder(folder_url)

            results.update(sub_results)

    return results

print("work in progress...")

root_url = f"{BASE}/{owner}/{repo}/tree/{branch}?plain=1"
files = scan_folder(root_url)

counters = {}

for path, size in files.items():  # files = dict path → byte
    if "." in path:
        ext = path.split(".")[-1]
        if ext in ["md", "xml", "png", "jpg", "jpeg", "txt", "gz", "yaml", "rst", "adoc", 
                    "org", "json", "yml", "toml", "ini", "cfg", "lock", "env", "properties", "iml", "gradle", "csproj", "sln", 
                    "vcxproj", "props", "targets", "gif", "svg", "ico", "webp", 
                    "zip", "tar", "gz", "7z", "exe", "dll", "so", "bin", 
                    "gitignore", "gitattributes", "gitmodules", "lock"]:
            continue
    else:
        continue
    counters[ext] = counters.get(ext, 0) + 1
    tot = sum(counters.values())
percentages = {ext: (n / tot) * 100 for ext, n in counters.items()}
for ext in percentages:
    print(ext, percentages[ext])

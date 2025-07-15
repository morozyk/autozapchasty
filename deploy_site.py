import requests, base64

GITHUB_TOKEN = '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'
USERNAME = 'david.m'
REPO = 'autozapchasty'

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Создаем репозиторий (если он уже есть — пропускаем)
resp = requests.post("https://api.github.com/user/repos", headers=headers, json={"name": REPO, "private": False})
print("Create repo:", resp.status_code, resp.json())

def upload(fpath):
    b64 = base64.b64encode(open(fpath,"rb").read()).decode()
    return requests.put(f"https://api.github.com/repos/{USERNAME}/{REPO}/contents/{fpath}",
                        headers=headers,
                        json={"message":f"Add {fpath}","content":b64})

for f in ["index.html","style.css"]:
    r = upload(f)
    print(f"Upload {f}:", r.status_code, r.json())

# Включаем Pages
r = requests.post(f"https://api.github.com/repos/{USERNAME}/{REPO}/pages", headers=headers, json={"source":{"branch":"main","path":"/"}})
print("Enable Pages:", r.status_code, r.json())

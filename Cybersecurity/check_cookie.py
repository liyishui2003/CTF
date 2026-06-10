import requests, re, base64, json

url = "http://wily-courier.picoctf.net:63375"
names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingerbread", "sugar", "fortune"]

for name in names:
    r = requests.post(f"{url}/search", data={"name": name})
    
    match = re.search(r'class="alert[^"]*"[^>]*>(.*?)<button', r.text, re.DOTALL)
    alert_text = ""
    if match:
        alert_text = re.sub(r'<[^>]+>', ' ', match.group(1)).strip()
    
    session_val = ""
    for cookie in r.cookies:
        if cookie.name == 'session':
            session_val = cookie.value[:80]
    
    decoded = ""
    if session_val:
        parts = session_val.split(".")
        if len(parts) >= 1:
            payload = parts[0]
            payload += "=" * (4 - len(payload) % 4)
            try:
                d = base64.urlsafe_b64decode(payload)
                decoded = str(json.loads(d))[:60]
            except:
                decoded = "decode error"
    
    print(f"{name:30s} | {alert_text[:50]:50s} | session: {decoded}")

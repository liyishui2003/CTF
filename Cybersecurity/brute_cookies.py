import requests

url = "http://wily-courier.picoctf.net:63375"
names = [
    "snickerdoodle", "chocolate chip", "oatmeal raisin", "gingerbread",
    "sugar", "peanut butter", "white chocolate macadamia", "thin mint",
    "fortune", "shortbread", "butter", "macaron", "biscotti",
    "ladyfinger", "tuile", "langue de chat", "pizzelle", "spritz",
    "sandwich", "mochi", "madeleine", "kourabiedes", "alfajor",
    "anise", "springerle", "lebkuchen", "pepparkakor", "pfeffernusse",
    "biscuit", "rusk", "teacake", "wafer", "crepe", "muffin",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "admin", "flag", "test", "0", "-1",
]

for name in names:
    r = requests.post(f"{url}/search", data={"name": name})
    if "That doesn't appear" not in r.text:
        print(f"[+] Found: '{name}'")
        # Extract the alert message
        from html.parser import HTMLParser
        class TextExtractor(HTMLParser):
            def __init__(self):
                super().__init__()
                self.text = []
                self.in_alert = False
            def handle_starttag(self, tag, attrs):
                if tag == "div" and any(a == "alert" for a in attrs[0] if len(attrs) > 0):
                    self.in_alert = True
            def handle_data(self, data):
                if self.in_alert:
                    self.text.append(data.strip())
        extractor = TextExtractor()
        extractor.feed(r.text)
        print(f"  Response: {r.text[:300]}")
        break
else:
    print("[-] Nothing found in list")

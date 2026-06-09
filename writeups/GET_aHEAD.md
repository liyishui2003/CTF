# CTF-12锛欸ET aHEAD 鈥?HTTP 涓夌璇锋眰鏂规硶

> 绗崄浜岄亾棰樸€傞鐪艰棌鍦ㄦ爣棰樼殑鍙屽叧閲岋細GET aHEAD 鈫?HEAD 鏂规硶銆?
> 鍏宠仈锛氫笂涓€棰?鈫?[[CTF-11_ScavengerHunt_瀵诲疂娓告垙.md]] | [[README.md]]

---

## 棰樼洰

椤甸潰鏈変袱涓寜閽細
- **Red** 鈥?`method="GET"`
- **Blue** 鈥?`method="POST"`

鐐瑰摢涓兘鍙垏鎹㈡爣棰樺拰鑳屾櫙鑹诧紝娌℃湁 flag銆?

---

## 瑙ｉ杩囩▼

### Step 1锛氳棰?

鏍囬 `GET aHEAD` 鏄弻鍏筹細
- "aHEAD" 涓?"a head" 鍚岄煶
- **HEAD** 鏄?HTTP 鐨勪竴涓姹傛柟娉?

鏃㈢劧 Red 鍜?Blue 鍒嗗埆瀵瑰簲 GET 鍜?POST锛岄偅杩樼己涓€绉嶆柟娉曟病璇曗€斺€?*HEAD**銆?

### Step 2锛氬彂 HEAD 璇锋眰

HEAD 涓?GET 绫讳技锛屼絾**鍙繑鍥炲搷搴斿ご锛屼笉杩斿洖鍝嶅簲浣?*銆?

娴忚鍣?Console锛團12锛夋墽琛岋細

```js
fetch("http://wily-courier.picoctf.net:62758/index.php", {method: "HEAD"})
  .then(r => {
    for(let [k, v] of r.headers) console.log(k + ": " + v);
  })
```

### Step 3锛氭嬁鍒?flag

杈撳嚭涓湁涓€琛岋細

```
flag: picoCTF{...}
```

---

## 鐭ヨ瘑鐐?

### 涓夌 HTTP 璇锋眰鏂规硶

| 鏂规硶 | 鍙傛暟浣嶇疆 | 杩斿洖 body | 鐢ㄩ€?|
|------|---------|----------|------|
| GET | URL 涓?| 鉁?| 鑾峰彇璧勬簮 |
| POST | 璇锋眰浣?| 鉁?| 鎻愪氦鏁版嵁 |
| HEAD | URL 涓?| 鉂?| 浠呰幏鍙栧搷搴斿ご |

### 鏈嶅姟绔€昏緫

```php
if ($_SERVER['REQUEST_METHOD'] == 'HEAD') {
    header("flag: picoCTF{...}");
}
```

鍑洪浜哄彧鍦?HEAD 鍒嗘敮涓嬪啓浜?flag 澶达紝GET 鍜?POST 閮芥病鏈夈€?

### 涓轰粈涔?Network 鐪嬩笉鍒帮紵

娴忚鍣ㄧ偣鍑?Red/Blue 鍙戠殑鏄?GET/POST銆?*flag 鍙嚭鐜板湪 HEAD 璇锋眰鐨勫搷搴斿ご閲?*銆傚彂浠€涔堣姹傚彇鍐充簬浣狅紝涓嶆槸鏈嶅姟绔喅瀹?缁欎笉缁欏ご"銆?

---

## 鍏宠仈

| 鍏宠仈鍒?| 鍘熷洜 |
|--------|------|
| [[CTF-02_DeveloperHeader缁曡繃鐧诲綍]] | 鑷畾涔?Header / 鏂规硶涔熸槸 HTTP 灞傞潰鐨勭粫杩?|
| [[../../CompetitiveProgramming/Codeforces/README.md]] | ACM 鎬濈淮锛氭灇涓炬墍鏈夊彲鑳斤紙GET銆丳OST 閮借瘯浜嗭紝杩樺墿 HEAD 鍛級 |

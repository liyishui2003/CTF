# CTF-04锛欻eapDump 娉勯湶涓庡唴瀛樺彇璇?
> 绗洓閬撻銆傛湇鍔″櫒鎶婂爢蹇収鏆撮湶鍑烘潵浜嗐€?> 鍏宠仈锛氫笂涓€棰?鈫?[[CTF-03_SSTI涓嶫inja2妯℃澘娉ㄥ叆.md]] | 涓嬩竴棰?鈫?[[CTF-05_Cookie閲岀殑绁炵閰嶆柟.md]]

---

## 棰樼洰

涓€涓崥瀹㈢綉绔欍€傚搷搴斿ご鏆撮湶浜?`X-Powered-By: Express`锛屾槸 Node.js銆?
棣栭〉娌′粈涔堢壒鍒殑锛屼絾 `/api-docs` 鏈?Swagger API 鏂囨。銆傜炕浜嗕竴涓嬶紝鍙戠幇涓€涓帴鍙ｏ細

```
GET /heapdump
Description: Diagnosing the memory allocation.
```

娌℃湁閴存潈锛岀洿鎺ョ偣 Execute 灏变細涓嬭浇涓€涓爢蹇収鏂囦欢銆俧lag 灏卞湪閲岄潰銆?
---

## 瑙ｉ杩囩▼

### 1. 鍙戠幇鎶€鏈爤

鎷垮埌鍝嶅簲澶达細

```
HTTP/1.1 200 OK
X-Powered-By: Express
ETag: W/"acd455-19e7e04134a"
```

Express.js锛孨ode 绯绘鏋躲€俙W/` 寮€澶寸殑 ETag 鏄急鏍￠獙锛坵eak validator锛夆€斺€?鏈嶅姟鍣ㄥ彧淇濊瘉璇箟绛変环锛屼笉淇濊瘉瀛楄妭绾т竴鑷淬€傞潤鎬佹枃浠堕粯璁や細甯?ETag锛岃繖閲屾病浠€涔堥棶棰橈紝浣嗘毚闇蹭簡鏂囦欢 hash锛屽彲浠ヤ綔涓轰俊鎭ˉ鍏呫€?
### 2. 缈?API 鏂囨。

璁块棶 `/api-docs`锛孲wagger UI 鍒楀嚭浜嗘墍鏈夋帴鍙ｏ紝鍖呮嫭涓€涓?`/heapdump`銆?
鎻忚堪鍐欑殑鏄?"Diagnosing the memory allocation."鈥斺€旂洿鐧藉埌涓嶈兘鍐嶇洿鐧斤紝灏辨槸璁╀綘璇婃柇鍐呭瓨鐢ㄧ殑銆?
娌℃湁閴存潈銆佹病鏈?token銆佹病鏈?IP 鐧藉悕鍗曪紝鐩存帴 Execute 灏辫兘涓嬭浇銆?
### 3. 涓嬭浇 heapdump

```
GET /heapdump 鈫?200 OK
Content-Type: application/octet-stream
Content-Disposition: attachment; filename="heapdump-1780230655952.heapsnapshot"
Content-Length: 11326549
```

澶х害 11MB 鐨?V8 鍫嗗揩鐓ф枃浠躲€?
### 4. 鎻愬彇 flag

鐩存帴 grep锛屾悳 `pico`锛堝洜涓虹煡閬撻鐩槸 picoCTF 鐨勶紝flag 鏍煎紡鏄?`picoCTF{...}`锛夛細

```bash
grep -a "pico" heapdump-1780230655952.heapsnapshot
```

涔熷彲浠ョ敤 Chrome DevTools锛?- F12 鈫?Memory 闈㈡澘 鈫?Load 鈫?閫夋嫨蹇収鏂囦欢
- Ctrl+F 鎼?`pico`

```
flag: picoCTF{Pat!3nt_15_Th3_K3y_8df117c1}
```

---

## 鍘熺悊

### HeapDump 鏄粈涔?
V8 寮曟搸鐨勫爢蹇収锛岃褰曟煇涓椂鍒绘墍鏈?JavaScript 瀵硅薄鍦ㄥ唴瀛樹腑鐨勭姸鎬併€傚寘鍚細
- 鎵€鏈夊彉閲忓€硷紙瀛楃涓层€佸璞°€侀棴鍖咃級
- 璋冪敤鏍?- 鍑芥暟瀹氫箟

Express 搴旂敤杩愯涓紝鎵€鏈夊姞杞藉埌鍐呭瓨鐨勫彉閲忛兘鍦ㄩ噷闈⑩€斺€斿寘鎷?flag銆?
### 涓轰粈涔堜細娉勯湶

Node.js 鏈変釜甯哥敤鐨勮皟璇?璇婃柇鍖呭彨 `heapdump`锛屽彲浠ヤ富鍔ㄧ敓鎴愬揩鐓х敤浜庢帓鏌ュ唴瀛樻硠婕忋€傚紑鍙戞椂寰堟湁鐢紝浣嗙嚎涓婃毚闇插嚭鍘诲氨鏄簨鏁呫€?
姝ｅ父鐨勫仛娉曪細
- **缁戝畾鍒板唴缃?localhost**锛屼笉瀵瑰鏆撮湶
- **鍔犻壌鏉?*锛屾瘮濡?header 鏍￠獙鎴?token
- **鍙湪 debug 妯″紡涓嬪紑鍚?*

杩欓鐨勫弽闈㈠氨鏄細娌″仛浠讳綍淇濇姢锛岃８濂斻€?
---

## 寤朵几锛歂ode.js 鏄粈涔?
杩欓鍑虹幇浜?`X-Powered-By: Express` 鍜?heapdump銆傝鐞嗚В杩欓锛屽緱鍏堟悶娓呮 Node.js 鍦ㄦ暣涓?Web 閲屾壆婕斾粈涔堣鑹层€?
### 娴忚鍣ㄩ噷鐨?JS vs Node.js

```
娴忚鍣紙鍓嶇 JS锛夛細      鎿嶄綔 DOM銆佹敼椤甸潰鏍峰紡銆佸彂璇锋眰
Node.js锛堝悗绔?JS锛夛細    璇绘暟鎹簱銆佸啓鏂囦欢銆佸鐞?HTTP 璇锋眰銆佺鐞嗗唴瀛?```

璇█涓€鏍凤紙閮芥槸 JavaScript锛夛紝鑸炲彴涓嶅悓銆侼ode.js = **鍦ㄦ湇鍔″櫒涓婅窇 JavaScript 鐨勮繍琛屾椂**銆?
### Node.js 鍦ㄥ悗绔殑瀹氫綅

Node.js 鏄笟鐣屼富娴佸悗绔妧鏈箣涓€銆侼etflix锛圫SR 灞傦級銆丩inkedIn锛圓PI 缃戝叧锛夈€乁ber锛堟牳蹇冭绋嬪尮閰嶏級銆侀樋閲?鑵捐锛圔FF 灞傦級閮藉湪鐢ㄣ€?
鍜屽悗绔?Java 鐢熸€佺殑甯歌鍒嗗伐锛?
```
Java锛圫pring锛夆€斺€?鏍稿績涓氬姟灞?    璁㈠崟銆佹敮浠樸€佽处鎴枫€侀鎺э紝闇€瑕佸己绫诲瀷銆侀珮绋冲畾鎬?
Node.js锛圗xpress锛夆€斺€?杈圭晫鍜岃兌姘村眰
    SSR / BFF / API 鑱氬悎 / 瀹炴椂閫氫俊 / CLI 宸ュ叿
```

### 甯歌瀹炶返鍦烘櫙

| 鍦烘櫙 | 璇存槑 |
|------|------|
| **BFF** | 鍓嶇鍜?Java 寰湇鍔′箣闂寸殑鑱氬悎灞傦紝鎷兼暟鎹牸寮?|
| **API 缃戝叧** | 璇锋眰璺敱銆侀檺娴併€侀壌鏉冿紙绫讳技浣犲疄涔犵敤鐨?Shepherd + Ocean锛墊
| **SSR** | 鏈嶅姟绔覆鏌撻〉闈紝Netflix銆丄irbnb 鍦ㄧ敤 |
| **瀹炴椂閫氫俊** | WebSocket銆丼SE锛堜綘姣曡閲屽啓杩?SSE锛墊
| **CLI 宸ュ叿** | Webpack銆丆opilot CLI銆乂S Code 鎵╁睍鈥斺€旈兘鏄?Node.js |
| **杞婚噺 CRUD** | 蹇€熸惌 API锛屽儚杩欓鐨?Express 鍗氬锛屽崄鍑犺浠ｇ爜璧蜂竴涓湇鍔?|

### 涓轰粈涔堜細鏈?heapdump

Node.js 鏈嶅姟璺戜箙浜嗗彲鑳?*鍐呭瓨娉勬紡**銆傚紑鍙戣€呴渶瑕佺湅鍐呭瓨閲屾湁浠€涔堬紝浜庢槸 Node.js 鎻愪緵浜?heapdump 鏈哄埗鈥斺€旂粰鍐呭瓨鎷嶄竴寮犲揩鐓э紝鍒嗘瀽鍝簺瀵硅薄娌¤閲婃斁銆?
姝ｅ父閾捐矾锛?
```
鍙戠幇鍐呭瓨娉勬紡 鈫?鎵?heapdump 鈫?鍒嗘瀽瀵硅薄鍒嗗竷 鈫?淇唬鐮?鈫?閮ㄧ讲
```

CTF 閲岀殑闂锛氳繖涓?debug 鎺ュ彛娌″叧锛岃繕鏆撮湶鍦?Swagger 鏂囨。閲岋紝绛変簬鎶婇挜鍖欐彃闂ㄤ笂杩樿创浜嗗紶绾告潯銆?
### 鐞嗚В浜嗚繖浜涘啀鐪嬭繖棰?
```
浣犺闂?Swagger 椤甸潰锛?api-docs锛?     鈫?鐪嬪埌浜?/heapdump 鎺ュ彛
     鈫?鐐?Execute
Node.js 鏈嶅姟鍣ㄦ敹鍒拌姹?     鈫?鎷嶄簡鍐呭瓨蹇収锛坔eapdump锛?     鈫?杩斿洖浜?11MB 鐨勬枃浠讹紝閲岄潰瀛樼潃 flag
浣犳悳鍒?flag
```

娌℃湁 `X-Powered-By: Express`锛屼綘涓嶄細鐭ラ亾杩欐槸 Node.js銆?涓嶇煡閬?Node.js 鏄粈涔堬紝灏变笉鏄庣櫧 heapdump 鏄粈涔堟枃浠躲€?涓嶇煡閬?heapdump 瀛樹簡浠€涔堬紝灏变笉浼氭兂鍒版悳 `picoCTF`銆?
姣忎竴鏉′俊鎭兘鏄摼鏉′笂鐨勪竴鐜€?
---

## 闃插尽

| 鍋氭硶 | 璇存槑 |
|------|------|
| 涓嶆毚闇茶瘖鏂帴鍙?| `/heapdump`銆乣/debug` 绛夎矾寰勪笉璇ュ嚭鐜板湪绾夸笂 |
| Nginx 灞傛嫤鎴?| 鐗瑰畾璺緞鍙厑璁稿唴缃?IP |
| 绂佺敤 `X-Powered-By` | `app.disable('x-powered-by')`锛屽噺灏戜俊鎭硠闇?|
| 鐢熶骇鐜鏈€灏忔潈闄?| debug 宸ュ叿鍙湪寮€鍙?棰勫彂鐜鍙敤 |

---

## 涓庢湰浠撳簱鐨勫叧鑱?
| 鍏宠仈鍒?| 鍘熷洜 |
|--------|------|
| [[杞欢杩愮淮]] | 鎺掓煡绗竴鎷?鍏堝畾鐣?鈥斺€旂湅鍒?X-Powered-By 灏辩煡閬撴槸 Express 鐨勬椿 |
| [[cleanCode-瑙勮寖]] | 闃插尽鎬х紪绋嬶細涓嶈鏆撮湶鐨勪笢瑗垮埆鏆撮湶 |
| [[鎶€鏈爤鍏ㄦ櫙]] | Node.js BFF 鍜屼綘瀹炰範鐢ㄧ殑 Java 寰湇鍔?+ 涓棿浠讹紝鏈川鏄悓涓€濂楁灦鏋勬€濊矾鈥斺€旀湇鍔℃媶鍒嗐€丄PI 缃戝叧銆侀厤缃鐞?|
| [[../../AI/姣曡鍘熺悊閫熼€?md]] | 姣曡鐨?Express + FastAPI 鏋舵瀯 = Node.js BFF + Python AI 鏈嶅姟锛岃繖棰橀噷鐨?Express 灏辨槸 Node.js 鍚庣 |

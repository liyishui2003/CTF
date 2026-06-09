# CTF-09锛欶lag 钘忓湪 JS 鏂囦欢閲?

> PicoCTF 鈥?Includes.
> "This code is in a separate file!" 鈥斺€?纭疄鍦ㄥ彟涓€涓枃浠堕噷銆?
> 鍏宠仈锛歔[CTF-08_鏂囦欢涓婁紶+Webshell+sudo鎻愭潈.md]]

---

## 棰樼洰

涓€涓粙缁?include 鎸囦护鐨勯潤鎬侀〉闈€傛爣棰?"On Includes"銆?

鐐瑰嚮鎸夐挳寮瑰嚭锛歚This code is in a separate file!`

## 瑙ｉ杩囩▼

### Step 1锛氭煡鐪嬮〉闈㈡簮鐮?

```html
<script src="script.js"></script>
```

椤甸潰寮曠敤浜嗗閮?JS 鏂囦欢銆?

### Step 2锛氱洿鎺ヨ闂?script.js

```
http://target/script.js
```

鍐呭锛?

```javascript
function greetings()
{
  alert("This code is in a separate file!");
}

//  f7w_2of2_6edef411}
```

鎷垮埌鍚庡崐娈?flag锛歚f7w_2of2_6edef411}`

### Step 3锛氭壘鍓嶅崐娈?

妫€鏌?`style.css` 鎴栭〉闈?HTML 娉ㄩ噴锛屽彂鐜帮細

```
picoCTF{1nclu51v17y_1of2_
```

### Step 4锛氭嫾鎺?

```
picoCTF{1nclu51v17y_1of2_f7w_2of2_6edef411}
```

---

## 鐭ヨ瘑鐐?

| 姒傚康 | 璇存槑 |
|------|------|
| 闈欐€佹枃浠跺彲璁块棶 | `<script src="...">` 寮曠敤鐨?JS 鏂囦欢鎵€鏈変汉閮借兘鐩存帴璁块棶 |
| flag 鍒嗘 | 鍑洪浜烘妸 flag 鎷嗘垚涓ゆ锛屽垎鍒棌鍦ㄤ笉鍚岀殑闈欐€佽祫婧愰噷 |
| 鏌ョ湅椤甸潰婧愮爜 | HTML 娉ㄩ噴銆丆SS銆丣S 閮藉彲鑳借棌淇℃伅 |

## 鍙嶆€?

- JS/CSS 鏂囦欢鍦ㄦ祻瑙堝櫒閲屽彲浠ョ洿鎺ラ€氳繃 URL 璁块棶锛屼笉闇€瑕佷换浣曟潈闄?
- "This code is in a separate file!" 鏈韩鏄彁绀衡€斺€斿幓閭ｄ釜鏂囦欢鐪嬬湅
- 闈欐€佹枃浠跺鏌ユ槸淇℃伅鏀堕泦鐨勭涓€姝ワ紝搴旇鏈€鍏堝仛

---

## 寤跺睍鐭ヨ瘑锛氬墠绔唬鐮佷繚鎶や笌娉勯湶

### Source Map锛?map 鏂囦欢锛?

鍘嬬缉/娣锋穯鍚庣殑 JS 鏃犳硶鐩存帴璋冭瘯銆俙.map` 鏂囦欢鏄竴鏈?瀛楀吀"锛岃褰曞帇缂╁悗鐨勪唬鐮佷笌鍘熷婧愮爜鐨勫搴斿叧绯伙細

| 鍘嬬缉鍚?| .map 鏂囦欢 | 鍘熷婧愮爜 |
|--------|-----------|----------|
| `function a(b){...}` | 鈫?(琛?鍒? 鍚嶆槧灏? | `function sayHello(name){...}` |

娴忚鍣?DevTools 妫€娴嬪埌 `.map` 鏂囦欢鍚庤嚜鍔ㄥ姞杞斤紝灞曠ず鍘熷婧愮爜銆傞棶棰樻槸寰堝浜?*鎶?`.map` 鏂囦欢閮ㄧ讲鍒颁簡鐢熶骇鐜**銆?

**Claude 娉勯湶浜嬩欢锛?* 鏀诲嚮鑰呰闂?`https://claude.ai/assets/xxx.js.map`锛岃繕鍘熶簡鍓嶇瀹屾暣閫昏緫锛屽寘鎷?API 鍦板潃銆乸rompt 妯℃澘銆佸鎴风鏍￠獙瑙勫垯銆?

**闃插尽锛?* 鏋勫缓宸ュ叿锛圵ebpack/Vite锛夐粯璁ょ敓鎴?`.map`锛屼絾鐢熶骇閮ㄧ讲鏃跺繀椤绘帓闄ゃ€傚彲閰嶇疆 `sourceMap: false` 鎴栧彧鍦ㄦ瀯寤洪樁娈典繚鐣欍€?

### 娌℃湁 .map 鎬庝箞鍔?

JS 浠嶇劧鍙互琚€嗗悜锛屽彧鏄毦搴︿笉鍚岋細

| 娣锋穯绋嬪害 | 鐗瑰緛 | 閫嗗悜闅惧害 |
|----------|------|----------|
| Minify 鍘嬬缉 | 鍙橀噺缂╃煭銆佸幓绌烘牸 | 浣?鈥?閫昏緫缁撴瀯涓嶅彉锛屽彲璇绘€у樊浣嗚兘璇?|
| 閲嶅害娣锋穯 | 瀛楃涓插姞瀵嗐€佹浠ｇ爜鎻掑叆 | 涓?鈥?闇€瑕佸伐鍏疯緟鍔?|
| 鎺у埗娴佸钩鍧﹀寲 | switch-case + 鐘舵€佸彉閲?| 楂?鈥?闇€瑕佷笓鐢ㄥ伐鍏?+ 浜哄伐鍒嗘瀽 |

### 鎺у埗娴佸钩鍧﹀寲锛圕ontrol Flow Flattening锛?

鎶婃甯哥殑 if-else / for / while 缁撴瀯鎷嶅钩鎴愪竴涓?**while + switch + 鐘舵€佸彉閲?* 鐨勭粺涓€缁撴瀯锛?

```js
// 鍘熷
if (user.role === 'admin') { showPanel(); }
else { denyAccess(); }

// 骞冲潶鍖栧悗
var state = 2;
while (true) {
    switch (state) {
        case 2: state = (user.role === 'admin') ? 3 : 4; break;
        case 3: showPanel(); state = 5; break;
        case 4: denyAccess(); state = 5; break;
        case 5: return;
    }
}
```

閫昏緫绛変环锛屼絾浜虹溂澶卞幓浜?杩欐杩樻槸閭ｆ"鐨勫眰娆℃劅銆?

### de4js 绛夐€嗗悜宸ュ叿

鍘熺悊锛氳瘑鍒?switch-case 骞冲潶鍖栨ā寮?鈫?杩借釜鐘舵€佸彉閲忕殑娴佽浆璺緞 鈫?杩樺師鎴?if-else / 鍑芥暟璋冪敤銆?

浣嗗彧鑳借В鍒颁腑闂寸姸鎬侊紝閲嶅害娣锋穯 + 澶氬眰鍙樺舰闇€瑕佷汉宸ヨˉ鍏呫€?

### 缁撹

鍙娴忚鍣ㄩ渶瑕佹墽琛?JS锛屽氨涓€瀹氳兘鎷垮埌瀹屾暣鍙墽琛岀殑婧愪唬鐮併€?*娣锋穯鍙兘澧炲姞闃呰鎴愭湰锛屼笉鑳介樆姝㈤槄璇汇€?* 鏁忔劅閫昏緫姘歌繙搴旇鏀惧湪鏈嶅姟绔?API 閲岋紝涓嶅湪鍓嶇鍋氫换浣曠瀵嗘牎楠屻€?

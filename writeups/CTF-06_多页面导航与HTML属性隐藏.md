# CTF-06: 澶氶〉闈㈠鑸笌 HTML 灞炴€ч殣钘?
> 绗叚閬撻銆俧lag 钘忓湪 about.html 鐨勮嚜瀹氫箟灞炴€ч噷銆?> 鍏宠仈锛氫笂涓€棰?鈫?[[CTF-05_Cookie閲岀殑绁炵閰嶆柟]] | 鍥炲埌 [[README.md]] | 涓嬩竴棰?鈫?[[CTF-07_IntroToBurp_OTP缁曡繃.md]]

## 棰樼洰淇℃伅

- **棰樼洰**锛歮ultipage-html锛坧icoCTF锛?- **鏍稿績鑰冪偣**锛氬椤甸潰缃戠珯瀵艰埅銆丠TML 鏍囩鑷畾涔夊睘鎬с€丅ase64 闅愯棌
- **宸ュ叿**锛氭祻瑙堝櫒 DevTools銆丅ase64 瑙ｇ爜

---

## 瑙ｉ杩囩▼

### 1. 椤甸潰瑙傚療

鎵撳紑椤甸潰锛岄椤垫樉绀猴細

```
Ha!!!!!! You looking for a flag?
Keep Navigating

Haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Keepppppppppppppp Searchinggggggggggggggggggg
```

鎻愮ず "Keep Navigating" 鈥斺€?涓€璇弻鍏筹細
- "缁х画娴忚" 鈥斺€?鍒彧鐪嬭繖涓€椤?- "鍘荤湅瀵艰埅鏍? 鈥斺€?瀵艰埅鏍忛噷鏈夊叾浠栭〉闈㈤摼鎺?
### 2. 鍥剧墖鍒嗘瀽锛堣鍏ユ閫旓級

椤甸潰鍖呭惈涓ゅ紶鍥剧墖锛?- `img/binding_dark.gif` 鈥?榛戣壊 GIF锛岀害 20KB锛屽疄闄呮樉榛?- `img/multipage-html-img1.jpg` 鈥?鏅€?JPG锛岀害 33KB

妫€鏌ョ粨鏋滐細
- **GIF**锛?80脳180锛?6 鑹茶皟鑹叉澘锛屽叏鏄繁鐏拌壊锛圧GB 9~34 涔嬮棿锛夛紝鑲夌溂鍏ㄩ粦
- **JPG**锛氫綔鑰?Shihab Ul Haque锛宍FFD9` 姝ｅ父缁撳熬锛屾棤闄勫姞鏁版嵁
- 涓ゅ紶鍥鹃兘鏃犳槑鏂?flag锛屼篃鏃犻檮鍔犳暟鎹?
瀹為檯涓婅繖鏄?*璇**鈥斺€旈鐩笉闇€瑕佺湡姝ｇ殑鍥剧墖闅愬啓鍒嗘瀽銆?
### 3. HTML 婧愮爜鍒嗘瀽

鏌ョ湅椤甸潰婧愪唬鐮侊細

```html
<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="about.html">About</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>
```

涓変釜椤甸潰銆傞椤?`index.html` 娌℃湁 flag锛屼簬鏄闂?`about.html`銆?
### 4. 鎵惧埌 Flag

鍦?`about.html` 涓彂鐜颁竴涓嚜瀹氫箟灞炴€э細

```html
<section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfZGYwZGE3Mjd9">
```

`notify_true` 涓嶆槸鏍囧噯 HTML 灞炴€э紝鍊兼槸 Base64 缂栫爜銆傝В鐮侊細

```bash
echo "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfZGYwZGE3Mjd9" | base64 -d
# 鎴?PowerShell:
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("..."))
```

寰楀埌 flag锛?
```
picoCTF{web_succ3ssfully_d3c0ded_df0da727}
```

---

## 寤朵几鐭ヨ瘑

### 涓€銆?Keep Navigating" 鐨勪竴璇弻鍏?
鑻辨枃涓?**navigate** 鏈変袱涓惈涔夛細

| 鍚箟 | 瀵瑰簲鎿嶄綔 |
|------|---------|
| 娴忚/瀵艰埅锛堝姩璇嶏級 | "缁х画娴忚鍏朵粬椤甸潰" |
| 瀵艰埅鏍忥紙鍚嶈瘝 鈫?nav锛?| "鍘荤湅鐪嬪鑸爮" |

CTF 鍑洪浜虹粡甯稿埄鐢ㄨ繖绉嶈涔夊弻鍏充綔涓烘彁绀恒€傜被浼肩殑杩樻湁锛?
- `Try inspecting the page!!` 鈫?鏌ョ湅椤甸潰婧愪唬鐮?/ 妫€鏌ュ厓绱?- `Look around` 鈫?鏌ユ壘鎵€鏈夎矾鐢?绔偣
- `robots.txt` 鈫?鐪嬬埇铏鍒欐枃浠?
### 浜屻€丠TML 鑷畾涔夊睘鎬э紙Custom Attributes锛?
鏍囧噯鐨?HTML 鑷畾涔夊睘鎬у簲璇ヤ互 `data-` 鍓嶇紑锛?
```html
<div data-user-id="12345" data-role="admin">
```

浣嗗湪瀹為檯棰樼洰涓紝鍑洪浜哄彲浠ラ殢鎰忓啓浠讳綍灞炴€у悕锛堝 `notify_true`锛夛紝娴忚鍣ㄤ笉浼氭姤閿欍€?*杩欑粰浜嗗嚭棰樹汉闅愯棌鏁版嵁鐨勭┖闂淬€?*

濡備綍鍙戠幇鑷畾涔夊睘鎬т腑鐨勬暟鎹細
1. **鏌ョ湅婧愪唬鐮?*锛圕trl+U / Cmd+U锛?2. **鍙抽敭 鈫?妫€鏌ュ厓绱?*锛圖evTools Elements 闈㈡澘锛?3. **鎼滅储** `=` 鍙锋垨鍙枒鐨?Base64 鐗瑰緛锛堝瓧姣嶆暟瀛楃粨灏剧殑 `=` 鎴?`==`锛?
### 涓夈€佷负浠€涔堣繖棰樹笉鏄湡闅愬啓

鎴戣姳浜嗕竴浜涙椂闂村垎鏋?GIF 鍜?JPG 鐨勪簩杩涘埗缁撴瀯锛?
- **GIF**锛氭彁鍙栦簡鑹叉澘锛?6 绉嶆繁鐏帮級銆丩SB锛堟渶浣庢湁鏁堜綅锛夈€佸儚绱犲垎甯?- **JPG**锛氭鏌ヤ簡 COM 娉ㄩ噴銆丄PP 鏍囪銆佹湯灏鹃檮鍔犳暟鎹?
缁撴灉閮芥槸绌恒€傚師鍥犳槸棰樼洰鏍规湰**涓嶉渶瑕?*鍥剧墖鍒嗘瀽 鈥斺€?鍥剧墖鍙槸椤甸潰鐨勮楗板厓绱犮€?
**CTF 瑙ｉ鏂规硶璁猴細鍏堟壘鏈€瀹规槗鐨勭獊鐮村彛銆?*

| 浼樺厛绾?| 妫€鏌ラ」 | 鏈缁撴灉 |
|--------|--------|---------|
| 1 | 椤甸潰婧愪唬鐮?| 鉁?杩欓噷鏈?flag |
| 2 | HTML 娉ㄩ噴 | 鉂?鏃?|
| 3 | JS/CSS 鏂囦欢 | 鉂?鏃犲叧 |
| 4 | 澶氶〉闈?澶氳矾鐢?| 鉁?about.html 鏈夊彂鐜?|
| 5 | Cookie/Header | 鉂?鏃犲叧 |
| 6 | 鍥剧墖/鏂囦欢闅愬啓 | 鉂?璇 |

浼樺厛妫€鏌?涓嶉渶瑕佷换浣曞伐鍏?鐨勪笢瑗库€斺€?*椤甸潰婧愮爜鍜岀綉缁滆姹?*銆?
### 鍥涖€佸浘鐗囬殣鍐欏叆闂紙鎷撳睍闃呰锛?
铏界劧鏈涓嶉渶瑕侊紝浣嗛『渚夸簡瑙ｅ父瑙佺殑鍥剧墖闅愬啓鎵嬫锛?
#### 4.1 LSB锛堟渶浣庢湁鏁堜綅锛?
姣忎釜鍍忕礌鐨勯鑹插€硷紙RGB 鍚?1 瀛楄妭锛夌殑**鏈€浣庝綅**鍙互琚浛鎹负淇℃伅浣嶃€?
```
鍘熷鍍忕礌: R=0b10101101, G=0b01111000, B=0b11001010
淇敼鏈€浣庝綅鍚? R=0b10101100, G=0b01111001, B=0b11001010
                                 ^         ^         ^
                        闅愯棌浜?0 (0b000)
```

浜虹溂鏃犳硶瀵熻 卤1 鐨勯鑹插彉鍖栵紝浣嗕竴闀夸覆鍍忕礌鐨?LSB 鍙互鎷煎嚭瀹屾暣鏁版嵁銆?
**宸ュ叿**锛歚zsteg`锛圥NG/BMP锛夈€乣StegSolve`锛圙UI 杞暘鏌ョ湅姣忓眰浣嶅浘锛?
#### 4.2 GIF 鐨勭储寮曡壊闅愬啓

GIF 浣跨敤璋冭壊鏉匡紙Palette锛夛紝姣忎釜鍍忕礌瀛樼殑鏄?*棰滆壊绱㈠紩**鑰屼笉鏄?RGB 鍊笺€?
濡傛灉璋冭壊鏉跨殑鐩搁偦棰滆壊鍦ㄨ瑙変笂闈炲父鎺ヨ繎锛堝杩欓噷鐨?RGB(31,31,31) 鍜?RGB(15,15,15)锛夛紝閭ｄ箞鍍忕礌绱㈠紩鐨?LSB 涔熷彲浠ヨ棌鏁版嵁鈥斺€旀浛鎹㈠悗鑲夌溂鐪嬩笉鍑烘潵銆?
**鏈鐨?GIF 鍒嗘瀽**锛?- 16 鑹茶皟鑹叉澘锛屽叏鏄繁鐏帮紙RGB 9~34锛?- 180脳180 = 32400 鍍忕礌
- 鎵€鏈?16 涓储寮曢兘鏈変娇鐢?- 鑲夌溂鐪嬭捣鏉ュ叏榛戯紝浣嗗儚绱犲疄闄呭垎甯冧笉鍧囧寑锛堜笉鏄函鑹诧級

灏濊瘯浜?LSB 鎻愬彇浣嗘湭鍙戠幇 flag锛屽洜涓烘暟鎹笉鍦?GIF 閲屻€?
#### 4.3 JPG 鐨勯殣鍐欐柟寮?
| 鏂瑰紡 | 鍘熺悊 | 宸ュ叿 |
|------|------|------|
| EXIF 鍏冩暟鎹?| 钘忓湪鐩告満淇℃伅/浣滆€?鎻忚堪瀛楁 | `exiftool` |
| 鏈熬闄勫姞鏁版嵁 | JPG 浠?FFD9 缁撳熬锛屼箣鍚庤拷鍔犲唴瀹?| `strings`, `binwalk` |
| DCT 绯绘暟闅愬啓锛圝Steg锛?| 淇敼 DCT 鍙樻崲鍚庣殑鏈€浣庝綅 | `stegdetect`, `outguess` |

#### 4.4 璇嗗埆鍥剧墖鏄惁钘忎簡涓滆タ

```bash
# 1. 鏌ョ湅鏂囦欢鏈熬鏄惁鏈夐檮鍔犳暟鎹?tail -c 100 image.jpg | xxd

# 2. 妫€鏌ュ厓鏁版嵁
exiftool image.jpg

# 3. 鏌ユ壘鍙墦鍗板瓧绗︿覆
strings image.jpg | grep -i "pico\|flag\|CTF"

# 4. 鏂囦欢绫诲瀷鏄惁鍖归厤
file image.jpg     # 搴旇杩斿洖姝ｇ‘鐨?MIME 绫诲瀷

# 5. 姣旇緝鏂囦欢澶у皬鈥斺€旂函鑹插浘涓嶅簲璇ユ湁鍑犲崄 KB
```

---

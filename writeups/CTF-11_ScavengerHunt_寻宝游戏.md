# CTF-11 Scavenger Hunt 瀵诲疂娓告垙

## 棰樼洰淇℃伅
- **骞冲彴**锛歅icoCTF
- **棰樼洰**锛歋cavenger Hunt
- **绫诲瀷**锛歐eb / 淇℃伅鏀堕泦

## 棰樼洰鎻忚堪
flag 琚媶鎴愬涓鐗囷紝钘忓湪缃戠珯鐨勫悇涓钀姐€備綘闇€瑕佸儚瀵诲疂涓€鏍峰埌澶勭炕鎵俱€?
## 瑙ｉ杩囩▼

### Part 1 鈥?HTML 娉ㄩ噴
鏌ョ湅椤甸潰婧愮爜锛屾壘鍒?HTML 娉ㄩ噴锛?```html
<!-- Here's the first part of the flag: picoCTF{t -->
```

### Part 2 鈥?CSS 鏂囦欢
寮曠敤浜嗕竴涓閮?CSS 鏂囦欢锛堥€氬父鏄?`mycss.css` 鎴栫被浼肩殑锛夛紝鍦ㄦ渶搴曢儴锛?```css
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```

### Part 3 鈥?robots.txt
JS 鏂囦欢閲屾湁鎻愮ず锛?```js
/* How can I keep Google from indexing my website? */
```
鈫?绛旀鏄?`robots.txt`銆傝闂?`/robots.txt`锛?```
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

"Access" 澶у啓 A 鏄彁绀?鈫?`.htaccess`

### Part 4 鈥?.htaccess
璁块棶 `/.htaccess`锛?```
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

"Store" 澶у啓 S 鏄彁绀?鈫?`.DS_Store`锛坢acOS 鐩綍 metadata 鏂囦欢锛?
### Part 5 鈥?.DS_Store
璁块棶 `/.DS_Store`锛?```
Congrats! You've completed the scavenger hunt! Part 5: _9588550}
```

### 鎷兼帴 Flag
```
picoCTF{t + h4ts_4_l0 + t_0f_pl4c + 3s_2_lO0k + _9588550}
= picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_9588550}
```

## 鐭ヨ瘑鐐?
### 甯歌鐨?钘忎笢瑗?鐨勬枃浠惰矾寰?
| 鏂囦欢 | 浣滅敤 | 璺緞 |
|------|------|------|
| `robots.txt` | 鍛婅瘔鎼滅储寮曟搸鐖櫕鍝簺椤甸潰涓嶈兘鐖?| `/robots.txt` |
| `.htaccess` | Apache 鐨勭洰褰曠骇閰嶇疆鏂囦欢 | `/.htaccess` |
| `.DS_Store` | macOS 鐨勭洰褰曞浘鏍?浣嶇疆鍏冩暟鎹?| `/.DS_Store` |
| `sitemap.xml` | 缃戠珯鍦板浘锛屽垪鍑烘墍鏈夐〉闈?| `/sitemap.xml` |

### 鍚ず
- 娉ㄩ噴閲屼篃鍙兘钘忔晱鎰熶俊鎭紒涓嶈浠ヤ负娉ㄩ噴涓嶄細琚湅鍒?- 澶栭儴璧勬簮鏂囦欢锛圕SS銆丣S锛変篃鏄棌涓滆タ鐨勫ソ鍦版柟
- 鍑洪浜虹粡甯稿湪鏂囦欢鍚?娉ㄩ噴閲岀敤 **澶у啓瀛楁瘝鍋氬弻鍏虫彁绀?*锛圓ccess 鈫?.htaccess, Store 鈫?.DS_Store锛?- 涓嶈鍙叧娉ㄤ富瑕侀〉闈紝**"娌′汉鐪?鐨勬枃浠跺線寰€鏈€鏈変环鍊?*

## 鍙傝€?- PicoCTF Scavenger Hunt
- [robots.txt 鍗忚](https://developers.google.com/search/docs/crawling-indexing/robots/intro)

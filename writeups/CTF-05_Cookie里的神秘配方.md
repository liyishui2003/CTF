# CTF-05锛欳ookie 閲岀殑绁炵閰嶆柟

> 绗簲閬撻銆侭ase64 钘忓湪 cookie 閲屻€?> 鍏宠仈锛氫笂涓€棰?鈫?[[CTF-04_HeapDump娉勯湶涓庡唴瀛樺彇璇?md]] | 鍥炲埌 [[README.md]] | 涓嬩竴棰?鈫?[[CTF-06_澶氶〉闈㈠鑸笌HTML灞炴€ч殣钘?md]]

---

## 棰樼洰

涓€涓櫥褰曢〉銆傝緭瀹岃处鍙峰瘑鐮侊紝椤甸潰鎻愮ず浣犲幓鐪嬬湅 cookie銆?
F12 鈫?Application 鈫?Cookies 涓€鐪嬶紝鏈変釜鍙?`secret_recipe` 鐨勪笢瑗匡細

```
secret_recipe=cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzJDODA0MEVGfQ%3D%3D
```

## 瑙ｉ杩囩▼

### 1. URL 瑙ｇ爜

`%3D` 鏄?`=` 鐨?URL 缂栫爜銆傝В鎺夛細

```
cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzJDODA0MEVGfQ==
```

鏈熬涓や釜 `=`锛孊ase64 鐨勭壒寰併€?
### 2. Base64 瑙ｇ爜

```
echo "cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzJDODA0MEVGfQ==" | base64 -d

picoCTF{c00k1e_m0nster_l0ves_c00kies_2C8040EF}
```

鎴栬€呭湪娴忚鍣?Console锛?
```javascript
atob("cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzJDODA0MEVGfQ==")
```

---

## 鍘熺悊

### Cookie 鏄粈涔?
鏈嶅姟鍣ㄥ瓨鍦ㄦ祻瑙堝櫒閲岀殑灏忔暟鎹潡銆傛瘡娆¤姹傛祻瑙堝櫒浼氳嚜鍔ㄥ甫涓娿€?
鐧诲綍鍚庢湇鍔″櫒閫氳繃 `Set-Cookie` 鍝嶅簲澶村啓杩涘幓锛屼箣鍚庝綘姣忔璁块棶閮藉甫鐫€瀹冿紝鏈嶅姟鍣ㄥ氨鐭ラ亾"浣犳槸璋?銆?
### Base64 鏄粈涔?
涓€绉嶆妸浜岃繘鍒舵暟鎹浆鎴愭枃鏈殑缂栫爜鏂瑰紡銆傜壒寰侊細鍙惈 `A-Za-z0-9+/=`銆?
**涓嶆槸鍔犲瘑**锛?*鍙槸缂栫爜**銆備换浣曚汉閮借兘瑙ｃ€傛妸 flag 鐢?Base64 缂栫爜鏀?cookie 閲岋紝鐩稿綋浜庢妸瀵嗙爜鍐欏湪渚垮埄璐翠笂璐磋剳闂ㄤ笂銆?
### 涓轰粈涔堣繖棰樹笉鍙?鐮磋В"

鍥犱负杩欓**涓嶆槸璁╀綘缁曡繃浠€涔?*锛屾槸璁╀綘瀛︿細锛?1. cookie 鍦ㄥ摢鐪?2. Base64 鎬庝箞瑙?3. 鏁忔劅淇℃伅涓嶈鏀?cookie

---

## 闃插尽

| 鍋氭硶 | 璇存槑 |
|------|------|
| 鏁忔劅淇℃伅涓嶆斁 cookie | 鍗充娇鐢?Base64 缂栫爜涔熶笉琛岋紝绛変簬鏄庢枃 |
| cookie 鍙瓨 session ID | 鐪熸鐨勬暟鎹斁鏈嶅姟绔?|
| HttpOnly 鏍囪 | JS 璇讳笉鍒?cookie锛屽噺灏?XSS 娉勯湶椋庨櫓 |
| Secure + SameSite | 闄愬埗 cookie 鐨勪綔鐢ㄥ煙鍜屽彂閫佸満鏅?|

---

## 寤朵几锛歅HP 鏄粈涔?
杩欓鐨?cookie 寰堝彲鑳芥槸 PHP 鐨?`setcookie()` 鍙戠殑銆傚鏋滃搷搴斿ご閲屾湁 `X-Powered-By: PHP`锛屽氨鑳界‘璁ゃ€?
### 鍜屽悗绔叾浠栬瑷€鐨勫叧绯?
```
PHP锛?    涓撻棬涓虹綉椤佃€岀敓鐨勮€佺墝鍚庣璇█銆俉ordPress銆丗acebook 鏃╂湡閮界敤瀹?Node.js锛?鐢?JS 鍐欏悗绔紝鐩稿鏂?Java锛?   浼佷笟绾ч噸鍨嬫鏋?```

PHP 鐨勭壒鐐规槸"鏉ヤ竴涓姹傝捣涓€涓繘绋嬶紝澶勭悊瀹屽氨閫€鍑?銆備笉鍍?Node.js 閭ｆ牱涓€鐩磋窇鍦ㄥ唴瀛橀噷銆?
### 鎬庝箞璁ゅ嚭 PHP

```
鍝嶅簲澶达細X-Powered-By: PHP/8.0.1
URL锛?  /login.php  /api.php
```

### 浠ｇ爜闀夸粈涔堟牱

```php
<?php
  $flag = "picoCTF{...}";
  setcookie("secret_recipe", base64_encode($flag));
  // setcookie 浼氭妸鍊煎啓鍒版祻瑙堝櫒鐨?cookie 閲??>
```

PHP 浠ｇ爜宓屽湪 HTML 閲屽啓锛岀畝鍗曠洿鎺ャ€傛柊椤圭洰鐢?PHP 鐨勫皯浜嗭紝浣嗗瓨閲忓法澶э紝CTF 閲岀粡甯搁亣鍒般€?
### 杩欓閲?PHP 鍋氫簡浠€涔?
```
浣犵殑娴忚鍣?                    PHP 鏈嶅姟鍣?  鈹€鈹€ 鐧诲綍璇锋眰 鈹€鈹€鈫?             妫€鏌ヨ处鍙峰瘑鐮?  鈫愨攢 Set-Cookie: secret_recipe  鐢熸垚 Base64 缂栫爜鐨?flag
  鈫愨攢 "鍘荤湅鐪?cookie"            鍛婅瘔浣犲幓鐪?浣犳墦寮€ Application 闈㈡澘
  鐪嬪埌 cookie
  瑙?Base64 鈫?flag
```

---

| 鍏宠仈鍒?| 鍘熷洜 |
|--------|------|
| [[CTF-01_Session涓嶈繃鏈熶笌Cookie鍔寔.md]] | 绗竴棰樹篃鏄?cookie锛屼笉杩囨槸鏀逛簡鍒汉鐨?session |
| [[cleanCode-瑙勮寖]] | 闃插尽鎬х紪绋嬶細鏁忔劅淇℃伅涓嶈鍑虹幇鍦ㄦ剰澶栫殑鍦版柟 |

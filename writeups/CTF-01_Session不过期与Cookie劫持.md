# CTF-01锛歋ession 涓嶈繃鏈?+ Cookie 鍔寔

> 绗竴閬撻銆傜邯蹇典竴涓嬨€?> 鍏宠仈锛歔[README.md]] | 涓嬩竴棰?鈫?[[CTF-02_DeveloperHeader缁曡繃鐧诲綍.md]]

---

## 棰樼洰

鐧诲綍缃戠珯锛屽彂鐜?session 姘镐笉杩囨湡銆傛壘鍒扮鐞嗗憳鐨?session锛屾浛鎹㈡垚鑷繁鐨勶紝鎷垮埌 flag銆?
---

## 瑙ｉ杩囩▼

### Step 1锛氬彂鐜板紓甯?
鐧诲綍鍚?`F12` 鈫?**Application** 鈫?**Cookies**锛岀湅鍒?session 鐨勮繃鏈熸椂闂达細

```
session=n0ExlJxbYH5zXabqjxXczsAt_haG1obNbPpUU96FkrQ
Expires=Wed, 06 Feb 2058 07:09:50 GMT
```

2058 骞淬€?026 骞寸殑棰橈紝session 璁惧埌浜?2058 骞淬€傜瓑浜庝笉杩囨湡銆?
### Step 2锛氭壘鍒板叆鍙?
椤甸潰涓婃湁涓€琛屾枃瀛楋細

```
find strange page at /session
```

`page` 鏄〉闈㈢殑鎰忔€濄€傚湪 URL 鍚庨潰鎷间笂 `/session`锛岃烦杞埌涓€涓柊椤甸潰銆?
椤甸潰涓婄洿鎺ュ睍绀轰簡涓や釜 session锛?- `user_xxx` 鈥?鎴戣嚜宸辩殑
- `admin_xxx` 鈥?绠＄悊鍛樼殑

缃戠珯鎶婃墍鏈夌櫥褰曟€佺殑 session 閮芥墦鍗板嚭鏉ヤ簡銆?
### Step 3锛氭浛鎹?Cookie

澶嶅埗绠＄悊鍛樼殑 session銆傚洖鍒?`F12` 鈫?**Application** 鈫?**Cookies**锛?
1. 鍙屽嚮 `session` 杩欎竴琛岀殑 Value 鍒?2. 绮樿创
3. 鎸?Enter
4. 鍒锋柊椤甸潰

椤甸潰鍙樻垚浜嗙鐞嗗憳瑙嗚銆俧lag 灏卞湪閭ｉ噷銆?
---

## 鐭ヨ瘑鐐?
### Session 杩囨湡

| | 姝ｇ‘鐨勫仛娉?| 杩欓亾棰?|
|---|---|---|
| 杩囨湡鏃堕棿 | 鍑犲皬鏃跺埌鍑犲ぉ | 30 骞村悗 |
| 娉勯湶鍚?| 鍙兘鐢ㄤ竴灏忔鏃堕棿 | 鑳界敤涓€杈堝瓙 |
| HttpOnly | 搴斿紑鍚?| 宸插紑鍚?鉁?|

### 涓や釜婕忔礊

| 婕忔礊 | 绫诲瀷 |
|---|---|
| Session 姘镐笉杩囨湡 | 閰嶇疆缂洪櫡 |
| `/session` 鎵撳嵃鎵€鏈?session | 淇℃伅娉勯湶 |

### Cookie 鍔寔

鎷垮埌鍒汉鐨?session Cookie锛?
```
Application 闈㈡澘鏀瑰€?鈫?鍒锋柊 鈫?鍙樻垚閭ｄ釜浜?```

涓嶉渶瑕佸瘑鐮併€備笉闇€瑕侀獙璇併€傝繖灏辨槸涓轰粈涔?session 瑕佷繚鎶ゅソ銆?
### 闃插尽

- Session 璁剧疆鍚堢悊杩囨湡鏃堕棿
- 涓嶅澶栨毚闇?session 鍒楄〃
- 鍏抽敭鎿嶄綔瑕佹眰浜屾楠岃瘉
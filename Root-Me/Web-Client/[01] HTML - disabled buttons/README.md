Root-Me [HTML - disabled buttons](https://www.root-me.org/en/Challenges/Web-Client/HTML-disabled-buttons)
===

該題提供一個 `Input` 與一個 `Submit`，但皆無法使用。

## 解題關鍵
1. 檢視原始碼
2. 修改原始碼

## 解題方法
首先打開原始碼可以看到以下的畫面。  
![](img/01.png)  

```HTML
<input disabled="" type="text" name="auth-login" value="">
<input disabled="" type="submit" value="Member access" name="authbutton">
```

把 `disabled` 拿掉，就可以輸入、送出了。

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
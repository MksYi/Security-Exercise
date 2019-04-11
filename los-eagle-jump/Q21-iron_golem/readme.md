Q21_iron_golem
===

該題執行過後不會有任何輸出，並且BAN掉了 sleep 與 benchmark。
但這一題語法錯誤會轉跳 SQL syntax 頁面。

藉此 SQL 的 IF 來呈現。
```SQL
SELECT IF(500<1000, "YES", "NO");
```
參考:https://www.w3schools.com/sql/func_mysql_if.asp

這時只要讓程式成功的時候出錯就可以知道對應的字元是什麼了。
假設 `select id from news union select 1,2,3` 當 union 大於主語句的 row 數時，就會返回 `The used SELECT statements have a different number of columns`。

一樣寫腳本讓他跑
![](https://i.imgur.com/DFRXTEN.png)

結果:
![](https://i.imgur.com/CWbMzP9.png)

```
https://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php?pw=!!!!
```

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
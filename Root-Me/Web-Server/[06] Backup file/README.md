Root-Me [Backup file](https://www.root-me.org/en/Challenges/Web-Server/Backup-file)
===

進入題目之後，會發現是一個簡易的登入系統，不過從題目名稱 `Backup file` 得知，該題不會考 SQLi、Weak Pwd。

## 解題關鍵
1. /backup/
2. index.php.bak
3. index.bak
4. ~index.bak
5. index.php~

## 解題方法
基本上就是把常用的備份方法之路徑，全部都嘗試過一遍，最後發現備份名稱為 `index.php~`。  
當成路徑輸入之後，會獲得一組帳號密碼，登入之後並提示「`To validate the challenge use this password`」，即表示密碼為 Flag。  

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
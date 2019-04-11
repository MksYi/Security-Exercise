Root-Me [File upload - null byte](https://www.root-me.org/en/Challenges/Web-Server/File-upload-null-byte)
===

首先這個頁面與前面檔案上傳的那幾題一樣，同時包含了上傳功能，並且明確限制上傳的檔案類型。

## 解題關鍵
1. Null Byte 繞過上傳限制

## 解題方法
首先一開始也不清楚什麼是 `Null Byte`，Google 了一下才發現是利用 `%00` 的方式，來讓上傳的程式搞不清楚真上要上傳的檔案副檔名為何。  

簡單舉個例子，上傳的檔案名稱為 `payload.php%00.png`，這時候附檔名到底是 `php` 還是 `png` 呢? 運用此方法就可以繞過上傳機制，成功將 `payload.php` 上傳。

## Reference
[【程式】一個利用-null-byte-漏洞的資安攻擊事](http://bojack.pixnet.net/blog/post/31507777-【程式】一個利用-null-byte-漏洞的資安攻擊事)

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
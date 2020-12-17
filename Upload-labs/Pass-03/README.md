Pass-01
===

## 任務
上傳 `Webshell` 

直接上傳 `.php` 副檔名的程式，出現字串 「提示：不允许上传.asp,.aspx,.php,.jsp后缀文件！」，照這個模式感覺是走黑名單。  

並且透過觀察，上傳後的文件會被更名為當下時間戳，同時還會將特定的惡意字串給過濾掉，簡單測試 `大小寫`、`%00` 繞過皆無法。  

基本上黑名單繞過，只要副檔名與黑名單不相符即可，可以被當成 PHP 解析的基本上還有 PHP5，但可能是環境的關係，這題沒有成功上傳 shell，但由於上傳後還會加上時間搓，所以也無法使用 `.htacess` 來增加要被當成 `php` 解析的副檔名。  

## 解題方法

我猜是使用 PHP5 來繞過。

## 授權聲明
[![copyright © 2020 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
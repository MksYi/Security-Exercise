Pass-01
===

## 任務
上傳 `Webshell` 

直接上傳 `.php` 與 `.php5` 副檔名的程式，出現字串 「提示：此文件不允许上传!」，感覺上是白名單，但又好像不是，嘗試上傳 `.test` 副檔名的檔案可以上傳成功。  

最後推估出應該是使用 `.htaccess` 來增加 PHP 可解析的附檔名。

## 解題方法

只要生一個檔名為 `.htaccess` 的檔案，並且內容如下，就可以把 `.test` 當成 php 來解析了。  

```
AddType application/x-httpd-php php test
```

接著將 webshell 的副檔名改成 `.test` 上傳即可。  

## 授權聲明
[![copyright © 2020 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
Pass-01
===

## 任務
上傳 `Webshell` 

直接上傳 `.php` 副檔名的程式，出現字串 「提示：文件类型不正确，请重新上传！」，上傳圖片則可以，透過 Burp 可以初步確認判斷已改為後端，接著再觀察兩種文件上傳的過程可以發現蛛絲馬跡。  

PHP 文件:  
```
Content-Type: application/octet-stream
```

JPG 文件:  
```
Content-Type: image/jpeg
```

## 解題方法

基本上就是修改 MIME 來 Bypass 檔案類型的判斷，所以上傳 PHP 文件，並修改為 image/jpeg 即可。  

## 參考資料
[https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types)

## 授權聲明
[![copyright © 2020 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
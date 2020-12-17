Pass-01
===

## 任務
上傳 `Webshell` 

直接上傳 `.php` 副檔名的程式，跳出一個 Alert 警告無法上傳副檔名為 `.php` 的檔案，簡單了解按下 `上傳` 按鈕之後到底發生了什麼事情。  

```javascript
function checkFile() {
    var file = document.getElementsByName('upload_file')[0].value;
    if (file == null || file == "") {
        alert("请选择要上传的文件!");
        return false;
    }
    //定义允许上传的文件类型
    var allow_ext = ".jpg|.png|.gif";
    //提取上传文件的类型
    var ext_name = file.substring(file.lastIndexOf("."));
    //判断上传文件类型是否允许上传
    if (allow_ext.indexOf(ext_name) == -1) {
        var errMsg = "该文件不允许上传，请上传" + allow_ext + "类型的文件,当前文件类型为：" + ext_name;
        alert(errMsg);
        return false;
    }
}
```

## 解題方法

基本上就是把 WAF 用 JavaScript 寫在了前端，透過 Burp 上傳之後改個檔名即可繞過。  

* 這部分有想說使用 `%00` 來嘗試繞過，是可以上傳的，但並不會造成截斷。

## 授權聲明
[![copyright © 2020 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
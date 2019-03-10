Q25_umaru
===

以下為過濾的程式碼：
```
if(preg_match('/prob|_|\./i', $_GET[flag])) exit("No Hack ~_~");
if(preg_match('/id|where|order|limit|,/i', $_GET[flag])) exit("HeHe");
if(strlen($_GET[flag])>100) exit("HeHe");
```

以下會讀取當前的 Flag
```
$realflag = @mysql_fetch_array(mysql_query("select flag from prob_umaru where id='{$_SESSION[los_id]}'"));
```

以下會創建一個暫時的 Flag，參數為 `$_GET[flag]`，同時該地方也為注入點，第二行會執行 update 更新 `flag`。
```
@mysql_query("create temporary table prob_umaru_temp as select * from prob_umaru where id='{$_SESSION[los_id]}'");
@mysql_query("update prob_umaru_temp set flag={$_GET[flag]}");

```


## Know How
```
select sleep("H")
Output: 
0
select sleep(true)
Output:
0

select 1 union select 1
Output: 
1
select 1 union select 2
Output: 
1
2
```

ByPass 條件:
透過 Sleep 執行判斷結果，隨後接上一個錯誤的 SQL 語句，update 便會失敗。

跑腳本結果：
![](https://i.imgur.com/VXh01OZ.png)


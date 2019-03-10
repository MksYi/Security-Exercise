#!/usr/bin/env python
# coding=utf-8
from pwn import *
ip   = '140.110.112.31'
prot = 2116
r = remote(ip, prot)
#r = process("./pwntools")

payload = p32(0x79487FF)
r.recvuntil(":)")
r.sendline(payload)
r.recvuntil("\n")
r.recvuntil("\n")

for _ in range(1000):
    question =  r.recvuntil(" = ?").split(b' = ?')[0]
    r.sendline(str(eval(question)))

r.interactive()
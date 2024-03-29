from pwn import *

data = b'H\xb8E YOU~?}PH\xb8WHERE ARPH\xb8NOTFLAG{PH\x89\xe6H1\xd2\xb0\x8c0\xc8\x88\x04\x16H\xff\xc2\xb0\x840\xc8\x88\x04\x16H\xff\xc2\xb0\x9e0\xc8\x88\x04\x16H\xff\xc2\xb0\xde0\xc8\x88\x04\x16H\xff\xc2\xb0\x960\xc8\x88\x04\x16H\xff\xc2\xb0\x950\xc8\x88\x04\x16H\xff\xc2\xb0\xd50\xc8\x88\x04\x16H\xff\xc2\xb0\xdb0\xc8\x88\x04\x16H\xff\xc2\xb0\xb20\xc8\x88\x04\x16H\xff\xc2\xb0\xdb0\xc8\x88\x04\x16H\xff\xc2\xb0\xd90\xc8\x88\x04\x16H\xff\xc2\xb0\xcd0\xc8\x88\x04\x16H\xff\xc2\xb0\x9f0\xc8\x88\x04\x16H\xff\xc2\xb0\x880\xc8\x88\x04\x16H\xff\xc2\xb0\x9b0\xc8\x88\x04\x16H\xff\xc2\xb0\x880\xc8\x88\x04\x16H\xff\xc2\xb0\x9f0\xc8\x88\x04\x16H\xff\xc2\xb0\x9e0\xc8\x88\x04\x16H\xff\xc2\xb0\x880\xc8\x88\x04\x16H\xff\xc2\xb0\xcd0\xc8\x88\x04\x16H\xff\xc2\xb0\x940\xc8\x88\x04\x16H\xff\xc2\xb0\x820\xc8\x88\x04\x16H\xff\xc2\xb0\x930\xc8\x88\x04\x16H\xff\xc2\xb0\x900\xc8\x88\x04\x16H\xff\xc2j<XH1\xff\x0f\x05'

context.arch = "amd64"

'''
print(disasm(data))

p = run_shellcode(data)
print(p.recv())
'''

data = asm("mov cl, 0xed") + data
data = data[:-2]
data += asm("""
            mov al, 1
            inc rdi
            syscall
            """)

print(disasm(data))

p = run_shellcode(data)
print(p.recv())

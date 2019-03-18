import socket
from pwn import *

r = remote('misc.ctf.nullcon.net',6001)
count = 0
while True:
    r.send("\n")
    crap = r.recvline()
    print crap
    # print "> " + r.recv()
    if count < 200:
        data = r.recvuntil("\n--- Type")
    # data = r.recvrepeat(timeout)
    # print data
    #interactive mode
    # print data
    # r.interactive()
    # print data
    if count < 200:
        data = data.strip()
        data =data.split(' ---')[1]
        data = data.split('---')[0]

    print data
    s2_out = subprocess.check_output([sys.executable, "captcha.py", data])
    print s2_out
    print count
    r.send(s2_out)
    count += 1

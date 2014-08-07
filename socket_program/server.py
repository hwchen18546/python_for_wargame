import socket,sys
from binascii import hexlify

if(len(sys.argv) < 2):
    print 'Usage : python server.py port'
    sys.exit()

port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', port))
s.listen(5)

conn, addr = s.accept()

while True:
    buf = conn.recv(64)
    if len(buf) > 0:
        sys.stdout.write(buf)
        sys.stdout.flush()
        string = ''
        for c in range(0, len(str(buf))):
            string += '0x' + hexlify(buf[c]) + ' '
        conn.send(string)

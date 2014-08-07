import socket, sys, select

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to remote host
try :
    s.connect((host, port))
except :
    print 'Unable to connect'
    sys.exit()

while 1:
    socket_list = [sys.stdin, s]

    # Get the list sockets which are readable
    read_sockets, write_sockets, error_sockets = select.select(socket_list , [], []) 

    for sock in read_sockets:
        # Incoming message from remote server
        if sock == s:
            data = sock.recv(4096)
            if not data :
                print '\nDisconnect'
                sys.exit()
            else :
                sys.stdout.write(data + '\n')
                sys.stdout.flush()

        # Entered a message
        else :
            msg = sys.stdin.readline()
            s.send(msg)

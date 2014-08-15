# Echo client program
import socket
import hashlib  #sha.md5 lib
 
# The remote host
HOST = '5d712652e1d06a362f7fc6d12d66755b.2014.shallweplayaga.me'  
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
 
# initial var
i = 0
Ori_string = ""
Ori_string22 = ""   #add to 22 byte
 
# GET initial string (just for the answer format)    
while 1:
    data = s.recv(1024)
    print 'Received:', str(data)
    if i == 1:
        Ori_string = data.split(' ')[0]
    Ori_string22 = Ori_string;
        print '\nOriginal String:', Ori_string
        for x in range(len(Ori_string),22):
        Ori_string22 += "a"          
        break
    i = i + 1
print 'Ori_string22 String',Ori_string22
print 'Sha1:',hashlib.sha1(Ori_string22).hexdigest()
print 'MD5:',hashlib.md5(Ori_string22).hexdigest()
 
offset = 0;
Obj_sha1 = ""
temp_char = "a"
 
# Start scan
while 1:
    while(chr(ord(Ori_string22[len(Ori_string)+offset])) == "z"):
          Ori_string22 = Ori_string22[:len(Ori_string)+offset] + "a" + Ori_string22[len(Ori_string)+offset+1:]
          offset += 1
          temp_char = chr(ord(Ori_string22[len(Ori_string)+offset])+1)
          Ori_string22 = Ori_string22[:len(Ori_string)+offset] + temp_char + Ori_string22[len(Ori_string)+offset+1:]
          Obj_sha1 = hashlib.sha1(Ori_string22).hexdigest()
    if Obj_sha1[:6] == '000000':
        break
    offset = 0
    temp_char = chr(ord(Ori_string22[len(Ori_string)])+1)
    Ori_string22 = Ori_string22[:len(Ori_string)+offset] + temp_char + Ori_string22[len(Ori_string)+offset+1:]
    Obj_sha1 = hashlib.sha1(Ori_string22).hexdigest()
print  '\nFinal String22',Ori_string22
print  'Final Sha1',Obj_sha1
#s.send(Ori_string22)
s.close()
 
#for char in [chr(i) for i in range(ord('a'),ord('z'))]:

# Echo client program
import telnetlib
import hashlib  #sha.md5 lib
 
# The remote host
HOST = '54.85.93.193' 
PORT = 8888
tn = telnetlib.Telnet(HOST,PORT)
 
# initial var
i = 0
init_s = ""
input_s = ""   #add to 21 byte
 
# GET initial string
data = tn.read_until('\n')
print str(data)
'''
You must first solve a puzzle, 
a sha1 sum ending in 16 bit's set to 1, 
it must be of length 21 bytes, starting with ___________
'''
init_s = data.rstrip('\n').split('starting with ')[1]
input_s = init_s;
for x in range(len(init_s),21):
    input_s += "a"          
offset = 0;
output_sha1 = ""
temp_char = "a"
while 1:
    while(chr(ord(input_s[len(init_s)+offset])) == "z"):
          input_s = input_s[:len(init_s)+offset] + "a" + input_s[len(init_s)+offset+1:]
          offset += 1
          temp_char = chr(ord(input_s[len(init_s)+offset])+1)
          input_s = input_s[:len(init_s)+offset] + temp_char + input_s[len(init_s)+offset+1:]
          output_sha1 = hashlib.sha1(input_s).hexdigest()
    if output_sha1[-4:] == 'ffff':
        break
    offset = 0
    temp_char = chr(ord(input_s[len(init_s)])+1)
    input_s = input_s[:len(init_s)+offset] + temp_char + input_s[len(init_s)+offset+1:]
    output_sha1 = hashlib.sha1(input_s).hexdigest()

print  'send: ',input_s
print  'result sha1',output_sha1

'''
Welcome to feal 4.3
Please decrypt: 495cdb364abd99b35a7ca7f7fea5e25d
'''
#Chosen Plaintext attacks
tn.write(input_s)
print tn.read_until('\n')
print tn.read_until('\n')
print "a"*8,
tn.write("a"*8)
print tn.read_until('\n')
print "\x00"*8,
tn.write("\x00"*8)
print tn.read_until('\n')
tn.interact()

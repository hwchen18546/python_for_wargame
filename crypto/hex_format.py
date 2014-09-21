import sys

if len(sys.argv) > 1:
    hex_string = sys.argv[1]
    print sys.argv[1]
else:
    print "Enter the hex string:\n",
    hex_string = sys.stdin.readline().rstrip('\n')
hex_data = hex_string.decode("hex") #'abc'
for byte in hex_data:
    # ord(byte) = 0 ~ 255
    # hex(ord(byte)) = 0x00 ~ 0xff
    sys.stdout.write('\\x' + format(ord(byte),"02x"))
sys.stdout.write('\n')

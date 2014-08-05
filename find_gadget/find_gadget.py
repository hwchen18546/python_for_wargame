#!/usr/bin/env python 

from capstone import *
import sys

print "Enter binary file name: ",
data = sys.stdin.readline().rstrip('\n')
print ''
gadget_address = 0
gadget_string = ''

gadget_len = 0

md = Cs(CS_ARCH_X86, CS_MODE_32)
with open(data, 'rb') as content_file:
    content = content_file.read()

prev = None
for i in md.disasm(content, 0x08048000):
    #print "0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str)
    if prev != None:
        if prev.mnemonic == 'pop' and i.mnemonic == 'ret':
            gadget_string += prev.mnemonic + ' ' + prev.op_str + ' ; ret'
            gadget_address = prev.address
            print "0x0%x:  %s\t" %(gadget_address, gadget_string)
            gadget_string = ''
    prev = i


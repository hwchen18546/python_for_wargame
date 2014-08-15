#!/usr/bin/env python

import base64
str1 = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="
str2 = '{"showpassword":"no","bgcolor":"#ffffff"}'
str3 = '{"showpassword":"yes","bgcolor":"#ffffff"}'
str1 = base64.b64decode(str1)
 
def xor(a, b):
    return map(lambda x: chr(ord(x[0])^ord(x[1])), zip(a,b))
     
print xor(str1, str2)
#['q', 'w', '8', 'J', 'q', 'w', '8', 'J', 'q', 'w', '8', 'J', 'q', 'w', '8', 'J', 'q', 'w', '8', 'J', 'q', 'w', '8', 'J', 'q', 'w', '8', 'J', 'q', 'w', '8', 'J', 'q', 'w', '8', 'J', 'q', 'w', '8', 'J', 'q']
print ''.join(xor(str1, str2))
#qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq
print ''.join(xor(str1,'qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq'))
#{"showpassword":"no","bgcolor":"#ffffff"}
print base64.b64encode(''.join(xor(str3,'qw8J'*50)))
#ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK


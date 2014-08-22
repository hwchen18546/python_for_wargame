#!/usr/bin/env python
# ref:https://www.crysys.hu/hashgame/

import hashlib
import base64
import sys
min_md5_base64 = 'Vf3ppC4Iu74AAAAAaHR0cDovL2hhc2hjYXQubmV0LwA='
max_md5_base64 = '6Za/F6+mur4AAAAAaHR0cDovL2hhc2hjYXQubmV0LwA='
min_sha1_base64 = 'ur5v5kHl/kEAAAAAaHR0cDovL2hhc2hjYXQubmV0LwA='
max_sha1_base64 = 'ur9CR7qfCv0AAAAAaHR0cDovL2hhc2hjYXQubmV0LwA='

string = min_md5_base64
raw = base64.b64decode(string)

print 'dm5: ' + hashlib.md5(raw).hexdigest()
#print 'sha1: ' + hashlib.sha1(raw).hexdigest()
print 'raw: ' + raw
for char in raw:
    sys.stdout.write('\\x' + format(ord(char),"02x"))
sys.stdout.write('\n')


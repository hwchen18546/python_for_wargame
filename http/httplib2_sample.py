import urllib
import httplib2

http = httplib2.Http()

url = 'http://www.example.com/login'   
body = {'USERNAME': 'foo', 'PASSWORD': 'bar'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body))

headers = {'Cookie': response['set-cookie']}

url = 'http://www.example.com/home'   
response, content = http.request(url, 'GET', headers=headers)

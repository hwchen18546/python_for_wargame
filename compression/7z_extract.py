# sudo apt-get install p7zip
# sudo apt-get install p7zip-full
import os

while 1:
    finish = 1
    lists = os.listdir('.')
    for item in lists:
        if '.7z' in item:
            # aaa.7z extract password is aaa
            os.system('7za x ' + item + ' -p' + item.split('.')[0])
            os.system('rm ' + item)
            finish = 0
    if finish == 1:
        break
os.system('cat Key.txt')

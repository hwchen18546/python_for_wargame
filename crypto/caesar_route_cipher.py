#!/usr/bin/env python
import sys
import telnetlib
 
# The remote host
HOST = '54.209.5.48'  
PORT = 12345
tn = telnetlib.Telnet(HOST, PORT)
'''
Welcome to psifer school v0.002
Your exam begins now. You have 10 seconds, work fast.
Here is your first psifer text, a famous ancient roman would be proud if you solve it.
psifer text: rfc ylqucp rm rfgq qryec gq qsncpqgknjc
'''
while 1:

    data = tn.read_until('\n')
    print data
    if 'psifer text:' in data:
        break
lists = data.split('psifer text: ')
data = lists[1]
print '\033[1;33m' + data  +'\033[1;m'

# Caesar Cipher
for offset in range(1,26):
    text = ''
    for c in data:
        n = ord(c)-ord('a')
        if n >= 0 and n <26:
            n = n + offset
            n = n % 26
            text += chr(n+ord('a'))
        else:
            text += c
    if 'the answer to this stage is' in text:
        break
print '\033[1;32m' + text  +'\033[1;m'

# the answer to this stage is supersimple
lists = text.split('the answer to this stage is ')
first_key = lists[1]
tn.write(first_key)

'''
Congratulations, you have solved stage 1. You have 9 seconds left.
Now it's time for something slightly more difficult. Hint, everybody knows it's not length that matters.

psifer text: Igaoe evrfh.e fo  yopIdoretout  nrsyse ,oh e uolfy uofodltouodsr n  tw'bositef l   ilhfbs aaa gvis"eerimt lco ay ra  cenpsr ortyatorpnhbatseliowreg.e mh rc tTshw h aifehlto elhrmre waentag"ghri.eidc !s  F. ipocfhrh r ayaylosolueue  rnhf Igaoe evrfh.e fo  yopIdoretout  nrsyse ,oh e uolfy uofodltouodsr n  tw'bositef l   ilhfbs aaa gvis"eerimt lco ay ra  cenpsr ortyatorpnhbatseliowreg.e mh rc tTshw h aifehlto elhrmre waentag"ghri.eidc !s  F. ipocfhrh r ayaylosolueue  rnhf 
'''
while 1:
    data = tn.read_until('\n')
    print data
    if 'psifer text:' in data:
        break
lists = data.split('psifer text: ')
data = lists[1]
print '\033[1;33m' + data  +'\033[1;m'


for x in range(1,200): #space
    index = 0 
    loop = 0
    text = data[index]
    for y in range(0,250):
        index += x
        if index >= len(data):
            loop += 1
            index = loop
        text += data[index]
    if "I hope you don't" in text:
        print x
        break

# I hope you don't have a problem with this challenge. 
# It should be fairly straight forward if you have done lots of basic crypto. 
# The magic phrase for your efforts is "more answers here". 
# For your efforts, you will get another challenge!
lists = text.split('"')
second_key = lists[1]
print '\033[1;32m' + second_key +'\033[1;m'
second_key += '\n'

tn.write(second_key)
data = tn.read_until('\n')
if 'Looks like you need to study more' in data:
    sys.exit()
print data

# Route(Transposition)  cipher
while 1:
    data = tn.read_until('\n')
    print data
    if 'psifer text:' in data:
        break

lists = data.split('psifer text: ')
data = lists[1]
print '\033[1;33m' + data  +'\033[1;m'
'''
Congratulations, you have solved stage 2. You have 9 seconds left.
Last one.

psifer text: PVZVL EAVZW SWCOY EJVBG QAFUW LZRLF PSOWL KKFUC SWKKQ KINLD HDIRT WPCBX EBUWZ WHYDN EBXHP PFRFG JHVQL PVRWA OOJFA EARNW OHYLK KBVPG NSJRD ROSOW EHNRM HRSHK KZMDT HSNLL DCLWL DOKEM PKVZA HZDDC AGLUW PCXLN AZFWK KTKHP PXLVL PCDDC AGLUW PVRWO AQRQZ WBUOW EHZZG JRVUZ KKDXU DKZOD XSIHI QWIHV HSKVH QHKKW IOXLU LVIDK ATFUL DSEHP PZVYW HWEWZ AAZGV HSILY DHYHJ AOGSD ADZHG GBFZE KFVWW THKRE WYVVM NSKKS PWKLK OCCYS XZVLK DCLOV LFFES XZPMM OHGXL EBJRE ABLUK AFPUZ UAVRJ OCDHL DWEJE WFPKS ZOCLL PZVOS IPCLL PZVOS IPCLL PZVOS IPDDJ UVRGS HWKWD AZRPT SVFVW BZVHR AKRVO DWKHS OGERO ERFQL SOEWL KARNW PVZVZ WFUHJ PVRQA PBVHV OHFEW ETPRM RSJRD RSUDD KHFIK EAGOW YFPSL KQYDD HSEJW OMFXH NCSDT HMROJ AOUBZ WJVWZ AQFGW WBUZA HZSUW ANVUA CVKWZ NCLJZ EHZIA PVVOH OAFVL KTKKW LZRLF PSOWA OGKDL EQRWW WQYRX PVVOW RSCVA IBFWS IOJRU DWJWL DSWXF JMKKA JUZVL DOKGW LSEGA JUFQO DWTKJ WBURE GSPBG QUVWL DOKSG AADLY DHSHW TOTWD UHYHJ EUYWG BTJHL PCJXU YSJVX QZCBE KIEWS JOKWS YYNHD HGVHD EHKOW XWKPG NSCLL PZVEA PAFUW PVVUW
'''

# Vigenere Cipher
tn.write('applepie\n')

# Congratulations, you have solved stage 3. The flag is: flag{IGraduatedPsiferSchoolAndAllIGotWasThisLousyFlag}.
# *** Connection closed by remote host ***
tn.interact()

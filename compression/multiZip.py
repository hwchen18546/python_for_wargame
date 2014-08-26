import zipfile,tarfile,magic,os,sys
root="/home/hwchen18546/hitcon/tarmful/"
path="/home/hwchen18546/hitcon/tarmful/tarmful.zip"

while 1:
    try:
        types = magic.from_file(path)
        if types.startswith('Zip'):
            tool, mode = zipfile.ZipFile, 'zip' #tuple a,b,c = 1,2,3
        elif types.startswith('gzip'):
            tool, mode = tarfile.open, 'tar.gz'
        elif types.startswith('bzip2'):
            tool, mode = tarfile.open, 'tar.bz2'
        files = tool(path)
        files.extractall(root)
        if tool == zipfile.ZipFile:
            path = root + files.namelist()[1]
            #print files.namelist()
        elif tool == tarfile.open:
            namelist = files.getnames()
            path = root + namelist[::-1][0] #last one
            #print namelist
        #print path
    except UnicodeDecodeError: #Chinese file name
        os.renames(path,root+"temp")
        path=root+"temp"
    except tarfile.ReadError:
        print open(path).read()
        break
    except:
        print 'Unexpected error:', sys.exc_info()
        break

from urllib.request import urlopen
import re, os, sys

if not os.path.exists(sys.argv[2]):
    os.makedirs(sys.argv[2])

filenum = 1
for filename in os.listdir(os.getcwd()+'/'+sys.argv[1]):
    try:
        string = open(sys.argv[1]+'/'+filename, 'r').read()
        counter = 1
        stripped_filename = filename[:filename.find('.htm')]
        stripped_filename = stripped_filename[:stripped_filename.rfind('-')+1]
        stripped_filename = stripped_filename.replace('-','/')
        for line in re.findall('"[^"]*\.gif"', string):
            s = line[1:len(line)-1]
            url = 'http://www.vgmuseum.com/'+stripped_filename+s
            try:
                fn = sys.argv[2]+'/'+s.replace('/','-')
                if os.path.exists(fn):
                    print('    Line #'+str(counter)+' already present -- '+url)
                    counter += 1
                    continue
                contents = urlopen(url).read()
                file = open(fn, 'wb')
                file.write(contents)
                file.close()
                print('    Finished line #'+str(counter)+' -- '+url)
            except:
                print('    Passed on line #'+str(counter)+' -- '+url)
            counter += 1
        for line in re.findall('"[^"]*\.png"', string):
            s = line[1:len(line)-1]
            url = 'http://www.vgmuseum.com/'+stripped_filename+s
            try:
                fn = sys.argv[2]+'/'+s.replace('/','-')
                if os.path.exists(fn):
                    print('    Line #'+str(counter)+' already present -- '+url)
                    counter += 1
                    continue
                contents = urlopen(url).read()
                file = open(fn, 'wb')
                file.write(contents)
                file.close()
                print('    Finished line #'+str(counter)+' -- '+url)
            except:
                print('    Passed on line #'+str(counter)+' -- '+url)
            counter += 1
        print('Finished file #'+str(filenum)+' -- '+str(filename))
    except:
        print('Passed on file #'+str(filenum)+' -- '+str(filename))
    filenum += 1
from urllib.request import urlopen
import re, sys, os

if not os.path.exists(sys.argv[2]):
    os.makedirs(sys.argv[2])

string = open(sys.argv[1], 'r').read()

counter = 1
for line in re.findall('".*html?"', string):
    s = line[1:len(line)-1]
    url ='http://www.vgmuseum.com/'+s
    try:
        contents = urlopen(url).read()
        file = open(sys.argv[2]+'/'+s.replace('/','-'), 'wb')
        file.write(contents)
        file.close()
        print('Finished htm #'+str(counter)+' -- '+url)
    except:
        print('Passed on htm #'+str(counter)+' -- '+url)
    counter += 1
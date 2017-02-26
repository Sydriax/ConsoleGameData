from PIL import Image
import os, sys

if not os.path.exists(sys.argv[2]):
    os.makedirs(sys.argv[2])

fn = 1
for filename in os.listdir(os.getcwd()+'/'+sys.argv[1]):
	img = Image.open(sys.argv[1]+'/'+filename)
	img.save(sys.argv[2]+'/'+filename[:filename.rfind('.')]+'.'+sys.argv[3])
	print('Finished file #'+str(fn)+' -- '+filename)
	fn += 1
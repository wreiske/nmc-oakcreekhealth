import os
from progressbar import ProgressBar, Percentage, Bar, ETA

print "------------- Will's Image Converter --------------"
print "Usage: convert.py"
print "See files { } in convert.py"
print "---------------------------------------------------"

input_file = './icon.png'

files = {
	'./res/icon/android/icon-96-xhdpi.png':'96x96',
	'./res/icon/android/icon-72-hdpi.png':'72x72',
	'./res/icon/android/icon-48-mdpi.png':'48x48',
	'./res/icon/android/icon-36-ldpi.png':'36x36',
	'./res/icon/ios/icon-72-2x.png':'144x144',
	'./res/icon/ios/icon-57-2x.png':'114x114',
	'./res/icon/ios/icon-57.png':'57x57',
	'./res/icon/ios/icon-72.png':'72x72',
	'./res/icon/windows-phone/icon-173-tile.png':'173x173', 
	'./res/icon/windows-phone/icon-62-tile.png':'62x62',
	'./res/icon/windows-phone/icon-48.png':'48x48'
}

file_count = len(files)

pbar = ProgressBar(widgets=[Percentage(),' ', ETA(), ' ', Bar()], maxval=file_count)

print "Total Images to Convert = %s" % (file_count+1)

for f,s in pbar(files.items()):
	os.system("rm " + f)
	os.system("convert " + input_file + " -resize " + s + " " + f)
import os
import json
from progressbar import ProgressBar, Percentage, Bar



print "------------- Will's Image Converter --------------"

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

pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=file_count).start()


print "Total Images to Convert = %s" % (file_count+1)

i = 0

for x in files:
	os.system("rm " + x)
	os.system("convert " + input_file + " -resize " + files[x] + " " + x)
	pbar.update(i+1)
	i = i+1

pbar.finish()
    

#os.system("convert logo.png -resize '96x96': '/Users/wreiske/nmc/nmc/www/res/icon/android/icon-96-xhdpi.png'");
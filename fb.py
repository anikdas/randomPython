#!/usr/bin/python
###################################
#Writen by Anik Das
#Date 26th September 2013
#facebook image enlarger
###############################################################################################################
#this script uses the url to a resized image of a facebook profile
#to generate a large/full size image
#please note that this script does not violate user privacy
#this script niether 'hacks' into someone's profile nor invades privacy
#this program just retrives a larger version of a photo that a user has already put on their public profile
#contact for any legal issues: mailanik@gmail.com
################################################################################################################

import urllib2

print ("THIS PROGRAM DOWNLOADS PROFILE PICS ON FACEBOOK\n")
print ('WHICH CANNOT BE ENLARGED#\n')
print ('Just right click on the small profile pic then you will see\n')
print ('copy location of the image. Click on it. Paste the link\n')
print ('below and the large/full photo will be downloaded in the\n')
print ('same directory where this script resides\n')

url_raw = raw_input('Enter URL:\n')
found = url_raw.find("/")
if found != -1:
	pass
else:
	print ("invalid\n")
	exit()
for x in range(3):
	found = url_raw.find("/",found+1)
	if x == 2:
		pos1 = found
pos2 = url_raw.rfind("/")
replace = url_raw[pos1+1:pos2+1]
url =  url_raw.replace(replace,"")
file_name = url.split('/')[-1]
print (url)
f = urllib2.urlopen(url)
print ("downloading " + file_name)
# Open our local file for writing
local_file = open('./images/'+file_name, "w" + 'b')
#Write to our local file
local_file.write(f.read())
local_file.close()
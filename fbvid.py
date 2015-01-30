#!usr/bin/python

"""
##########################
Written by Anik Das
27th Septermber 2013
##############################
facebook video downloader#####
##################################################################################################
this program downloads facebook videos in mp4 format (which is default format for facebook videos)
from a given link to that video page. Make sure the video is public. Other wise the page will not
be accessable. The video is stored to the same directory as the python script is stored
##################################################################################################
"""
import urllib2

#takes the link as input
url = raw_input('Enter URL:\n')

#retrieves the web page containing the video
f = urllib2.urlopen(url)
txt = f.read();
#fetches the title of the video from the page title
title_pos1 = txt.find(b'<title id="pageTitle">')
title_pos2 = txt.find(b'</title>')
title = txt[title_pos1:title_pos2]
title = title.replace('<title id="pageTitle">','')
if not title:
	title = 'unnamed'
#locating partial video link
found = txt.find('fbcdn-video-a.akamaihd.net')
found2 = txt.find('thumbnail_src')

#actual video link with unicode characters located
txt = txt[found:found2];
found2 = txt.find('\u002522\u00252C\u002522')
txt = txt[:found2];

"""
local_file = open('pi.txt', "w" + 'txt')
#Write to our local file
local_file.write(txt)
local_file.close()
"""

#replacing the unicode characters to generate readable link
txt = txt.replace('\u00255C\u00252F', '/')
txt = txt.replace('\u00253F', '?')
txt = txt.replace('\u00253F', '?')
txt = txt.replace('\u00253D', '=')
txt = txt.replace('\u002526', '&')
txt = txt.replace('\u002522\u00252C\u002522', '')
txt = ('https://'+txt)

#proper link
print (txt)
#downloading video file using urllib2
f = urllib2.urlopen(txt)
file_name = (title +'.mp4')
file_name = file_name.replace(' ', '_')
file_name = file_name.replace('|_Facebook', '')
print ("downloading " + file_name)
# Open our local file for writing
local_file = open('./videos/'+file_name, "w" + 'b')
#Write to our local file
local_file.write(f.read())
local_file.close()

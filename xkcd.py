#!usr/bin/python

import urllib2
import string

for x in xrange(839,840):
	if x==404:
		x+=1
	#url = raw_input('Enter URL:\n')
	url = "http://xkcd.com/" + str(x) + "/";
	#retrieves the web page containing the image
	f = urllib2.urlopen(url) #urllib.urlopen(url) , alternatively for urllib.py library
	txt = f.read();
	#fetches the title of the xkcd title from the page
	title_pos1 = txt.find(b'<title>')
	title_pos2 = txt.find(b'</title>')
	#fetching title
	title = txt[title_pos1:title_pos2]
	title = title.replace('<title>','')
	#replacing the xkcd: from title
	title = title.replace('xkcd: ', '')
	img_search = 'alt="' + (title);
	#finding nearest alt to the actual link to the image
	altfind = txt.find(img_search)
	txt = txt[0:altfind]
	img_pos = txt.rfind("<img ")
	txt = txt[img_pos:altfind]
	link_pos1 = txt.find('"')
	txt = txt[link_pos1+1:altfind]
	link_pos2 = txt.find('"')
	link = txt[0:link_pos2]
	#print (link)
	#downloading video file using urllib2
	f = urllib2.urlopen(link)
	file_name = title
	for c in string.punctuation:
		file_name = file_name.replace(c,"")
	file_name = file_name + ".PNG"
	print ("downloading ::"+ str(x)+ " :: " + file_name)
	# Open our local file for writing
	local_file = open('./comics/'+file_name, "w" + 'b')
	#Write to our local file
	local_file.write(f.read())
	local_file.close()

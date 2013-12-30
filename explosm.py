#!usr/bin/python

import urllib2
import string

for x in xrange(404,405):
	#url = raw_input('Enter URL:\n')
	url = "http://explosm.net/comics/" + str(x) + "/";
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
	title = title.replace('Cyanide & Happiness', '')
	title = title.replace(' - Explosm.net', '')
	img_search = 'Cyanide and Happiness, a daily webcomic';
	#finding nearest alt to the actual link to the image
	altfind = txt.find(img_search)
	txt = txt[altfind:]
	src_pos = txt.find('src="')
	txt = txt[src_pos:]
	txt = txt.replace('src="', '')
	next_pos = txt.find('"')
	link = txt[0:next_pos]
	link = link.replace(' ', '%20')
	link_file = open('links.txt','a')
	link_file.write(link+'\n')
	file_name_startpos = link.rfind("/")
	file_name = link[file_name_startpos+1:]
	if (file_name == "" or link == "/comics/play-button.png"):
		continue
	#downloading image file using urllib2
	f = urllib2.urlopen(link)
	print ("downloading ::"+ str(x)+ " :: " + file_name)
	# Open our local file for writing
	local_file = open('./comics/explosm/'+file_name, "w" + 'b')
	#Write to our local file
	local_file.write(f.read())
	local_file.close()

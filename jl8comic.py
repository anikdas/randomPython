#!usr/bin/python

import urllib2
import string

def downloadfn(link):
	file_name_startpos = link.rfind("/")
	file_name = link[file_name_startpos+1:]
	try:
		f = urllib2.urlopen(link)
	except urllib2.HTTPError, e:
		if e.code==404:
			return 404
	else:
		print ("downloading :: " + file_name)
		# Open our local file for writing
		local_file = open('./comics/jl8/'+file_name, "w" + 'b')
		#Write to our local file
		local_file.write(f.read())
		local_file.close()

for x in xrange(183,184):
	link = 	'http://limbero.org/jl8/comics/' + str(x) + '.jpeg'
	#downloading image file using urllib2
	if downloadfn(link) == 404:
		for y in xrange(1,10):
			link = 	'http://limbero.org/jl8/comics/' + str(x) + '_' + str(y) + '.jpeg'
			if downloadfn(link) == 404:
				break


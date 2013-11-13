
import urllib2
import cookielib

folder_path = "./pdf_files/"

jar = cookielib.FileCookieJar("cookies")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib2.install_opener(opener)
file_id = 2
print "Currently have %d cookies" % len(jar)
file_download="http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=" +str(file_id) +"&tag=1"
response = opener.open(file_download)
print response.info()
print "##############################"
response = opener.open(file_download)
#print response.headers

print "Currently have %d cookies" % len(jar)
#print jar


#opener.addheaders = { 'User-Agent' : 'Mozilla/5.0' }
print response.info()
#while x!= "application/pdf":
#	response = opener.open(file_download)
#	print x
file_local = open( folder_path + str(file_id) + '.html', 'wb' )
file_local.write(response.read())
file_local.close()
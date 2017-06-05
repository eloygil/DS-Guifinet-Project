import urllib2
import json
import sys

def print_json(i,x):

 	name=x+'.txt'
 	url="http://sants.guifi.net/maps/export/captura.php?timestamp="+i
 	#print url
 	#print name
 	f = open(x+'.txt', 'w')
 	# #sys.stdout = f
 	data = json.loads(urllib2.urlopen(url).read())
 	
 	with open(name, 'w') as outfile:
 		json.dump(data, outfile)
 	f.close()
 	# for i in range(2):
  #    	print 'i = ', i

 	# sys.stdout = orig_stdout
 	# gifinetf.close()

wjdata = json.loads(urllib2.urlopen("http://sants.guifi.net/maps/export/timestamps.php").read())


#print wjdata['1']
i= 186

#for x in range(0, 10):
for x in range(0, 141):	
#     #print_json(wjdata[x])
#     print wjdata[i]
	#print wjdata[str(i+x)]
	print_json(wjdata[str(i+x)],str(x))
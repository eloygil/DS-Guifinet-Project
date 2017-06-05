# Python Json Parser by Eloy Gil & Hao Wu
# {eloy,hao.wu}@ac.upc.edu
# MIRI - DS - FIB (UPC)
import json
def print_to_csv(i):
	name=i+'.txt'
	with open(name, 'r') as f:
		nodelist = []    # List of nodes (id, label, long, latitude)
		edgelist = []	 # List of links between nodes (origin, dest, signal, bandwidth)
		for row in f:
			data = json.loads(row)
		for key, value in data.items():
			if key == "nodes":
				for keys, values in value.items():
					label = lat = lon = 'null'
					for keys_node, value_node in values.items():
						if keys_node == "name":
							label = value_node
						if keys_node == "lon":
							lon = value_node
						if keys_node == "lat":
							lat = value_node
							nodelist.append([keys,label,lon,lat])
						if keys_node == "links":
							bw = signal = 'null'
							for key_links, value_links in value_node.items():
								for key_link, value_link in value_links.items():
									if key_link == "signal":
										signal = value_link
									if key_link == "bandwidth":
										bw = value_link
										edgelist.append([keys,key_links,signal,bw])

	#to print cvs edges
	#print ("Source;Target;Type;Weight")
		f = open('csv_'+i+'_edges.csv', 'w')
		f.write ("Source;Target;Type;Weight\n")
		for p in edgelist: 
			f.write("{d[0]};{d[1]};Directed;{d[2]}\n".format(d=p))
		f.close()
	#toprint cvs nodes
	#print("Id;Label")	
		f = open('csv_'+i+'_nodes.csv', 'w')
		f.write ("Id;Label;City;Latitude;Longitude\n")

		for p in nodelist: 
			f.write ("{d[0]};{d[1]};Barcelona;{d[3]};{d[2]}\n".format(d=p))

		f.close()
	

for x in range(0, 141):
#for x in range(0, 1):
    print_to_csv(str(x))

	#print ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
	#print ("<gexf xmlns:viz=\"http:///www.gexf.net/1.1draft/viz\" version=\"1.1\" xmlns=\"http://www.gexf.net/1.1draft\">")
	#print ("<meta lastmodifieddate=\"2010-03-03+23:44\">")
	#print ("<creator>Gephi 0.7</creator>")
	#print ("</meta>")
	#print ("<graph defaultedgetype=\"undirected\" idtype=\"string\" type=\"static\">")
	#print ('<nodes count=\"{:d}\">'.format(len(nodelist))) 
	#for p in nodelist: print ("<node id=\"{d[0]}\" label=\"{d[1]}\"/>".format(d=p))					

	#i=1
	#for p in edgelist: 

	#	if str(p[2])==str('None'):
	#		print ("<edge id=\"{i}\" source=\"{d[1]}\" target=\"{d[1]}\"/>".format(i=i , d=p))					

	#	else: print ("<edge id=\"{i}\" source=\"{d[1]}\" target=\"{d[1]}\" weight=\"{d[2]}\"/>".format(i=i , d=p))					

	#	i +=1
	#print ("</edges>")
	#print ("</graph>")
	#print ("</gexf>")
	#print nodelist[0:5]
	#print edgelist[0:5]
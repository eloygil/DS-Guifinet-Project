# Python Json Parser by Eloy Gil & Hao Wu
# {eloy,hao.wu}@ac.upc.edu
# MIRI - DS - FIB (UPC)
import json
with open('captura.json', 'r') as f:
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
	#print nodelist[0:5]
	#print edgelist[0:5]
# Python Json parser for Node as Mesh Path counter by Eloy Gil & Hao Wu
# {eloy,hao.wu}@ac.upc.edu
# MIRI - DS - FIB (UPC)
# Note: Requires simplejson -> pip install simplejson

from collections import Counter
import simplejson as json
nodes = Counter()
nodelist = []
nodelist2 = []
nodediff = []
linklist = []
linklist2 = []
linkdiff = []

# Printing "nodes" / "links" | Showing the nodes/links that are present in one but not in the other.
printing = "nodes"
# Using captures with number x and y
x = 5
y = 6
for i in range(0, 2):
        if i == 0:
            with open(str(x) + '.txt') as data_file:
                data = json.load(data_file)
                for node in data["nodes"]:
                    nodelist.append(str(node))
                for key, value in data.iteritems():
                    if key == "nodes":
                        for key_node, value_node in value.iteritems():
                            name = key_node
                            for key_value, value_value in value_node.iteritems():
                                if key_value == "name":
                                    nodes[name] = value_value
                                if key_value == "links":
                                    for key_link, value_link in value_value.iteritems():
                                        linklist.append(str(name)+','+str(key_link))
        else:
            with open(str(y) + '.txt') as data_file:
                data2 = json.load(data_file)
                for node in data2["nodes"]:
                    nodelist2.append(str(node))
                for key, value in data2.iteritems():
                    if key == "nodes":
                        for key_node, value_node in value.iteritems():
                            name = key_node
                            for key_value, value_value in value_node.iteritems():
                                if key_value == "name":
                                    nodes[name] = value_value
                                if key_value == "links":
                                    for key_link, value_link in value_value.iteritems():
                                        linklist2.append(str(name)+','+str(key_link))
for node in nodelist:
    if node not in nodelist2:
        nodediff.append(node)
for node in nodelist2:
    if node not in nodelist:
        nodediff.append(node)
for link in linklist:
    if link not in linklist2:
        linkdiff.append(link)
for link in linklist2:
    if link not in linklist:
        linkdiff.append(link)
if printing == "nodes":
    print nodediff
elif printing == "links":
    print linkdiff

#print nodelist
#print nodelist2
#print linklist
#print linklist2
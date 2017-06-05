# Python Json parser for Node as Mesh Path counter by Eloy Gil & Hao Wu
# {eloy,hao.wu}@ac.upc.edu
# MIRI - DS - FIB (UPC)
# Note: Requires simplejson -> pip install simplejson

from collections import Counter
import simplejson as json
mesh = Counter()
inet = Counter()
# Printing "mesh" / "inet" | Showing the number of nodes using that node as gateway.
printing = "inet"
# Using capture with number x
x = 7
filename = str(x) + '.txt'
with open(filename) as data_file:
    data = json.load(data_file)

for key, value in data.iteritems():
    if key == "nodes":
        for key_node, value_node in value.iteritems():
            name = key_node
            for key_value, value_value in value_node.iteritems():
                if key_value == "mesh_path":
                    if value_value is not None:
                        for key_key_value, key_value_value in value_value.iteritems():
                            mesh[key_value_value] += 1
                if key_value == "inet_path":
                    if value_value is not None:
                        for key_key_value, key_value_value in value_value.iteritems():
                            inet[key_value_value] += 1
if printing == 'mesh':
    for node in mesh:
        print str(node) + ',' + str(mesh[node])
elif printing == 'inet':
    for node in inet:
        print str(node) + ',' + str(inet[node])



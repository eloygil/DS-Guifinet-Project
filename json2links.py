# Python Json parser for Node Failure Analysis by Eloy Gil & Hao Wu
# {eloy,hao.wu}@ac.upc.edu
# MIRI - DS - FIB (UPC)
# Note: Requires simplejason -> pip install simplejson

import simplejson as json
import operator
import copy
nodelist = []
linklist = []
failed = []
down_nodes = []
for x in range(0, 1):
    name = str(x) + '.txt'
    print name
    with open(name) as data_file:
        data = json.load(data_file)
        print data
    for key, value in data.items():
        if key == "nodes":
            for key_node, value_node in value.items():
                if key_node == "name":
                    name = key_node
                if key_node == "links":
                    for key_link, value_link in value_node.items():
                        linklist.append(str(name)+'-'+str(value_link))

#frequency = {i: linklist.count(i) for i in linklist}
#sorted_freq = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
#print 'Link list, ordered by number of 1-hour downtime failures:'
#for failed_node in sorted_freq:
#    print 'Link' + str(failed_node[0]) + ' = ' + str(failed_node[1])
print linklist
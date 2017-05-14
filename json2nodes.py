# Python Json parser for Node Failure Analysis by Eloy Gil & Hao Wu
# {eloy,hao.wu}@ac.upc.edu
# MIRI - DS - FIB (UPC)
# Note: Requires simplejason -> pip install simplejson

import simplejson as json
import operator
nodelist = []
failed = []
down_nodes = []
for x in range(0, 141):
    name = str(x) + '.txt'
    #print name
    with open(name) as data_file:
        data = json.load(data_file)
    if x == 0:
        for node in data["nodes"]:
            nodelist.append(str(node))
    else:
        for down_node in down_nodes:
            if down_node not in data["nodes"]:
                failed.append(str(down_node))
        for node in data["nodes"]:
            if node not in nodelist:
                nodelist.append(str(node))
                if node not in down_nodes:
                    for y in range(0, x):
                        failed.append(str(node))
                else:
                    failed.append(str(node))
                    down_nodes.remove(str(node))
        for old_node in nodelist:
            if old_node not in data["nodes"]:
                nodelist.remove(str(old_node))
                failed.append(str(old_node))
                down_nodes.append(str(old_node))
frequency = {i:failed.count(i) for i in failed}
sorted_freq = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
print 'Failed nodes list, ordered by number of 1-hour downtime failures:'
for failed_node in sorted_freq:
    print 'Node ' + str(failed_node[0]) + ' = ' + str(failed_node[1])
# Python Json parser for Node Failure Analysis by Eloy Gil & Hao Wu
# {eloy,hao.wu}@ac.upc.edu
# MIRI - DS - FIB (UPC)
# Note: Requires simplejason -> pip install simplejson

from collections import Counter
import simplejson as json
import operator
nodes = Counter()
nodelist = []
failed = []
down_nodes = []
for x in range(0, 141):
    filename = str(x) + '.txt'
    print filename
    with open(filename) as data_file:
        data = json.load(data_file)

    for key, value in data.iteritems():
        if key == "nodes":
            for key_node, value_node in value.iteritems():
                name = key_node
                for key_value, value_value in value_node.iteritems():
                    if key_value == "name":
                        nodes[name] = value_value
                        #break!

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
print 'Failed nodes list, ordered by uptime:'
for failed_node in sorted_freq:
    print 'Node ' + nodes[str(failed_node[0])] + ' = ' + str(round(100-float(failed_node[1])*100/float(x),3)) + '%'

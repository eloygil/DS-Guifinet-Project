# Python Json parser for Node Failure Analysis by Eloy Gil & Hao Wu
# {eloy,hao.wu}@ac.upc.edu
# MIRI - DS - FIB (UPC)
# Note: Requires simplejason -> pip install simplejson
#                               or: [sudo] easy_install simplejson

from collections import Counter
import simplejson as json
l = Counter()
nodes = Counter()
for x in range(62, 63):
    name = str(x) + '.txt'
    #print name
    with open(name) as data_file:
        data = json.load(data_file)
        #print data
    for key, value in data.iteritems():
        if key == "nodes":
            for key_node, value_node in value.iteritems():
                name = key_node
                for key_value, value_value in value_node.iteritems():
                    if key_value == "name":
                        nodes[name] = value_value 
                    if key_value == "links":
                        for key_link, value_link in value_value.iteritems():
                            l[str(name)+'-'+str(key_link)] += 1

print 'Link list, ordered by increasing uptime rate:'
ordered_links = []
for link in l:
    ordered_links.append([l[link], link])
ordered_links = sorted(ordered_links)
for link in ordered_links:
    #print 'Link ' + str(nodes[str(link[1]).split('-')[0]]) + ' to ' + str(nodes[str(link[1]).split('-')[1]])
    print 'Link ' + str(nodes[str(link[1]).split('-')[0]]) + ' to ' + str(nodes[str(link[1]).split('-')[1]]) + ' has a ' + str(float(link[0]*100/(x+1))) + '% uptime. (' + str(link[0]) + '/' + str(x+1) + ')'

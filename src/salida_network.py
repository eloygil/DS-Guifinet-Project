from collections import Counter
import simplejson as json
import json

l = Counter()
nodes = Counter()
for x in range(62, 63):
    name = str(x) + '.txt'
    print name
    with open(name) as data_file:
        data = json.load(data_file)
        #print data
    for key, value in data.iteritems():
        if key == "nodes":
            for key_node, value_node in value.iteritems():
                name = key_node
                l = 0
                for key_value, value_value in value_node.iteritems():
                    #if key_value == "name":
                    #    nodes[name] = value_value 
                    #    print value_value
                    if key_value == "inet_path":
                        #for key_link, value_link in value_value.lenght():
                            json_input = value_value
                            if json.dumps(json_input) != "Null"
                                print(json.dumps(json_input))


                            #for key_link, value_link in value_links.items():                        
                            #    nodes[name] = value_value 
               #              try:
               #                  decoded = json.loads(json_input)
               #                  print decoded
               #              # Access data
               #                  #for x in decoded['inet_path']:
               #                  #    for i in 10:
               #                  #        print x[i]
 
               #              except (ValueError, KeyError, TypeError):
               #                  print "JSON format error"
               # # print nodes
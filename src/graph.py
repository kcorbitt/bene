import pydot

class Graph(pydot.Dot):
    def __init__(self, nodes):
        super(Graph, self).__init__('Network Graph', graph_type='digraph')
        self.networkNodes = dict((node.hostname, node) for node in nodes)
        self.base_graph()

    def overlay_path(self, node1, node2, color='green'):
        """Graphs the network with the path from node1 to node2 overlaid"""
        startNode = self.networkNodes[node1]
        endNode = self.networkNodes[node2]
        endAddress = endNode.links[0].address
        currentNode = startNode
        while currentNode != endNode:
            try:
                nextNode = currentNode.forwarding_table[endAddress].endpoint
                self.get_edge(currentNode.hostname, nextNode.hostname)[0].set_color(color)
            except (KeyError, IndexError):
                print "Error, no route found from %s to %s" % (currentNode.hostname, nextNode.hostname)
            currentNode = nextNode

    def overlay_all_paths(self, node, color='blue'):
        endNode = self.networkNodes[node]
        for address in [link.address for link in endNode.links]:
            for n in self.networkNodes.values():
                if n.hostname == node:
                    continue
                try:
                    destination = n.forwarding_table[address].endpoint
                    self.get_edge(n.hostname, destination.hostname)[0].set_color(color)
                except (KeyError, IndexError):
                    print "Warning, no route found from %s to %s" % (n.hostname, node)

    def base_graph(self):
        for node in self.networkNodes.values():
            self.add_node(pydot.Node(node.hostname))
            for link in node.links:
                edge = pydot.Edge(link.startpoint.hostname, link.endpoint.hostname)
                self.add_edge(edge)

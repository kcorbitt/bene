import sys
sys.path.append('..')

from src import sim, node, link, graph

if __name__ == '__main__':
    # setup network
    n1 = node.Node('n1')
    n2 = node.Node('n2')
    n3 = node.Node('n3')
    n4 = node.Node('n4')
    n5 = node.Node('n5')
    # link from 1 to 2
    l = link.Link(address=1,startpoint=n1,endpoint=n2)
    n1.add_link(l)
    n1.add_forwarding_entry(address=2,link=l)

    # link from 2 to 1
    l = link.Link(address=2,startpoint=n2,endpoint=n1)
    n2.add_link(l)
    n2.add_forwarding_entry(address=1,link=l)
    n2.add_forwarding_entry(address=3,link=l)
    n2.add_forwarding_entry(address=4,link=l)
    n2.add_forwarding_entry(address=5,link=l)
    n2.add_forwarding_entry(address=6,link=l)
    n2.add_forwarding_entry(address=7,link=l)
    n2.add_forwarding_entry(address=8,link=l)

    # link from 1 to 3
    l = link.Link(address=3,startpoint=n1,endpoint=n3)
    n1.add_link(l)
    n1.add_forwarding_entry(address=4,link=l)
    n1.add_forwarding_entry(address=5,link=l)
    n1.add_forwarding_entry(address=6,link=l)
    n1.add_forwarding_entry(address=7,link=l)
    n1.add_forwarding_entry(address=8,link=l)

    # link from 3 to 1
    l = link.Link(address=4,startpoint=n3,endpoint=n1)
    n3.add_link(l)
    n3.add_forwarding_entry(address=1,link=l)
    n3.add_forwarding_entry(address=2,link=l)
    n3.add_forwarding_entry(address=3,link=l)

    # link from 3 to 4
    l = link.Link(address=5,startpoint=n3,endpoint=n4)
    n3.add_link(l)
    n3.add_forwarding_entry(address=6,link=l)

    # link from 4 to 3
    l = link.Link(address=6,startpoint=n4,endpoint=n3)
    n4.add_link(l)
    n4.add_forwarding_entry(address=1,link=l)
    n4.add_forwarding_entry(address=2,link=l)
    n4.add_forwarding_entry(address=3,link=l)
    n4.add_forwarding_entry(address=4,link=l)
    n4.add_forwarding_entry(address=5,link=l)
    n4.add_forwarding_entry(address=7,link=l)
    n4.add_forwarding_entry(address=8,link=l)

    # link from 3 to 5
    l = link.Link(address=7,startpoint=n3,endpoint=n5)
    n3.add_link(l)
    n3.add_forwarding_entry(address=8,link=l)

    # link from 5 to 3
    l = link.Link(address=8,startpoint=n5,endpoint=n3)
    n5.add_link(l)
    n5.add_forwarding_entry(address=1,link=l)
    n5.add_forwarding_entry(address=2,link=l)
    n5.add_forwarding_entry(address=3,link=l)
    n5.add_forwarding_entry(address=4,link=l)
    n5.add_forwarding_entry(address=5,link=l)
    n5.add_forwarding_entry(address=6,link=l)
    n5.add_forwarding_entry(address=7,link=l)

    # Begin graphs

    # Graph a simple network
    g1 = graph.Graph(sim.Sim.nodes)
    g1.write_png('graphs/network.png')

    # Graph the route from n2 to n5 in the network
    g2 = graph.Graph(sim.Sim.nodes)
    g2.overlay_path('n2', 'n5', color='red')
    g2.write_png('graphs/path.png')

    # Graph all paths to n1 in the network
    g3 = graph.Graph(sim.Sim.nodes)
    g3.overlay_all_paths('n1', color='blue')
    g3.write_png('graphs/all_paths.png')
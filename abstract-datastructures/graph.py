"""
Implementing a graph data structure in Python.
This is my first attempt at implementing Graphs in Python.

Version 1:
    
"""

class Node:
    def __init__(self, name, listofneighbours):
        self.name=name
        self.listofneighbours=listofneighbours
    def add_neighbour(self,node):
        self.listofneighbours.append(node)
    def print_neighbours(self):
        print "Printing neighbours"
        for node in self.listofneighbours:
            print node.name

#for now, the entire graph is represented by a list


def main_method():
    graph=[]
    #create two nodes
    print "Creating Nodes"
    baker_street=Node("Baker Street", [])
    marylebone=Node("Marylebone", [baker_street])
    graph=graph+[baker_street, marylebone]
    #add Marylebone node to Baker Street
    baker_street.add_neighbour(marylebone)
    print "Nodes"
    for node in graph:
        print "Name", node.name
        node.print_neighbours()


main_method()


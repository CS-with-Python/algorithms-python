"""
Simple Tree data structure based on instructions here
http://cbio.ufs.ac.za/live_docs/nbn_tut/trees.html
"""

class Node(object):
    def __init__(self,value, children=[]):
        self.value = value
        self.children = children
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret+=child.__repr__(level+1)
        return ret
    def sum_nodes(self):
        if len(self.children)==0:
            return self.value
        else:
            sum=0
            for child in self.children:
                sum+= child.sum_nodes()
            return self.value+sum



tree = Node("grandmother", [
    Node("daughter", [
        Node("granddaughter"),
        Node("grandson")]),
    Node("son", [
        Node("granddaughter"),
        Node("grandson")])])
print tree

"""
Exercise: make a tree with three levels and calculate the sum
of the values in the nodes
"""

tree_numbers = Node(1, [
    Node(2, [
        Node(3),
        Node(3)]),
    Node(1,[
        Node(3),
        Node(3)])])

print tree_numbers.sum_nodes()

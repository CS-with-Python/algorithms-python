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
    def find_smallest(self):
        if len(self.children)==0:
            return self.value
        else:
            minimum = self.value
            for child in self.children:
                minimum = min(minimum, child.find_smallest())
            return minimum
    def find_height(self):
        height=0
        if len(self.children)==0:
             return 1 
        else:
            for element in self.children:
                maximum = max(height,element.find_height()+1)
                height = maximum
            return height
            




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

tree_number_2 = Node(1, [
    Node(3,[
        Node(-1,[
            Node(-2),Node(-4)
            ])])
        ])

print tree_numbers.sum_nodes()

print tree_numbers.find_smallest()
print tree_number_2.find_smallest()
print tree_number_2.find_height()

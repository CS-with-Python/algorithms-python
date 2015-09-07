"""
The first implementation of a tree data structure in Python
Author: Camilla Montonen
"""

class Node():
   def __init__(self,nodename, parent):
      self.nodename=nodename
      self.parent=parent
      self.children=[]
   def __str__(self):
      print_string= "Node: "+self.nodename+" Parent:"+ self.parent
      return print_string
   def add_child(self, childNode):
      self.children.append(childNode)
   def print_all_children(self):
      if len(self.children==0):
         print "This node has 0 children"
      for node in self.children:
         print str(node)






"""
Code for in development testing 
"""
mynode=Node('hello','root')
print str(mynode)



"""
TODO: 

"""

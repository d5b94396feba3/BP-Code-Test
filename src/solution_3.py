'''
Time complexity is O(n).

Space complexity is O(h), where h is the height/depth of the tree.
'''

class Node:
        
        def __init__(self, value): 
                self.value = value 
                self.left_node = None
                self.right_node = None


def lca(parent, node_1, node_2):

        if parent is None: 
                return None

        if parent.value == node_1 or parent.value == node_2: 
                return parent 

        left_node = lca(parent.left_node, node_1, node_2) 
        right_node = lca(parent.right_node, node_1, node_2) 


        if left_node and right_node: 
                return parent 
        elif left_node is None:
                return right_node
        else:
                return left_node

        
        

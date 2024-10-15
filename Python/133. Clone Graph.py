'''
Implementation wasn't as hard as understanding what the description wanted.
Basically we need to create an exact copy of the Graph and return that, like
creating a new list where every item is the same as the original and in the same
position but it isn't the same variable.

The hashmap "copy" is only used to keep track of the already evaluated nodes, but the
real copy is "clone"
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy = {}

        def copyNode(node):
            if node in copy:
                return copy[node]

            clone = Node(node.val)
            copy[node] = clone
            for neighbors in node.neighbors:
                clone.neighbors.append(copyNode(neighbors))
            return clone

        if not node:
            return None
        return copyNode(node)
        
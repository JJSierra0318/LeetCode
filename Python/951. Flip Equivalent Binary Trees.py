'''
The main idea is to check if the trees are flip equivalent without modifying the original
trees, for that we iterate with BFS and save both current nodes of both trees in one queue
and we check, if the children are the same we just add them to the queue, if not we check if
they're flipped and we alter the order of one of the trees only in the queue and procced, if
none of the conditions are met then it isn't a valid flip
'''
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # if they are the same from the beginning we just return true, this case
        # also takes care of both trees being None
        if (root1 == root2): return True
        # if only one of the trees is None, or the val of the root isn't the same
        # we return false
        if (not root1 or not root2 or root1.val != root2.val): return False
        # We add both roots to the same queue
        queue = [root1, root2]

        while queue:
            # we pop for the nodes of the tree 1 and 2 respectivily
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            # if at the current node their value and children are the same we can skip the check
            if node1 == node2: continue
            # if only one is None or their values don't match, we return false
            if not node1 or not node2 or node1.val != node2.val: return False
            # We first check if their children have the same value in the same positions, no matter
            # if there is only one or two children
            if (((not node1.left and not node2.left) or
                (node1.left and node2.left and node1.left.val == node2.left.val)) and
                ((not node1.right and not node2.right) or
                (node1.right and node2.right and node1.right.val == node2.right.val))):
                # We add all of the children, first all lefts and then all rights
                queue.append(node1.left)
                queue.append(node2.left)
                queue.append(node1.right)
                queue.append(node2.right)
            # if not, we check if they have the same value but in flipped positions, once
            # again not caring if there's only one or two children
            elif (((not node1.left and not node2.right) or
                (node1.left and node2.right and node1.left.val == node2.right.val)) and
                ((not node1.right and not node2.left) or
                (node1.right and node2.left and node1.right.val == node2.left.val))):
                # in this case we flip the order, first left and second right and then first
                # right and second left
                queue.append(node1.left)
                queue.append(node2.right)
                queue.append(node1.right)
                queue.append(node2.left)
            # if none of the conditions are met, the children are different either by amount or
            # values so the tree can't be flipped
            else:
                return False
        # if we iterate through all of the trees without any error, then they can be flipped
        return True

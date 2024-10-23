'''
The main idea is to save the sum of the siblings before modifying the node to the sum of
the other cousins, in previous we keep the value of the sum of all the cousins, before we
update the values we check for the children, if there are siblings we want them to have the
same value (their sum) so the difference with the other cousins is easier
'''
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS queue
        queue = [root]
        # The sum of all the cousins, initially would be the root.val as its the only node
        previous = root.val
        while queue:
            # Will keep track of the sum of all the children, which will become the sum of all cousins
            total = 0
            # with this we iterate through every single level of the three before adding new nodes to the queue
            # And every iteration of the while loop will represent a level
            for node in queue.copy():
                # we pop the initial value to clean the queue as we go
                queue.pop(0)
                # We add to the total the sum of the children of the current node (doesn't matter if its one or None)
                total += (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                # If there are sibling we want to update their values to their sum as we should not substract between
                # sibling, only cousins, this way when we substract the total the value will be correct:
                # s1 = (1, 10) s2 (7) should end up being (11, 11) (7) so when we substract 18: (7, 7) (11)
                if node.left and node.right:
                    node.left.val += node.right.val
                    node.right.val = node.left.val
                # We append the children to the queue, if any
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # Update the current node value to the substraction of the current total sum of cousins and itself
                node.val = previous - node.val
            # Finally we update previous with total, which has been keeping the sum of the children, that in the next
            # iteration will become the evaluated nodes
            previous = total
        return root
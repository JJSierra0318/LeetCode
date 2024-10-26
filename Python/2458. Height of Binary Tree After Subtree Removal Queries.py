'''
The idea is to store the max height of every node, along with its level and also store
the largest and second largest height for every level. This is because we can only remove
one node for each query, meaning if the node we remove is part of the largest height of the
tree we only need the second highest height from that level
'''
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # hashmap that will save both the level and height for every node
        queryLevel = {}
        # This will save the highest height node for every level
        firstLargest = {}
        # And this one the second highest
        secondLargest = {}
        # for the depth we need to reach the bottom first, so we use dfs
        def dfs(node, level):
            # if we reach an empty node, we return -1, so that the node before this one
            # will have height 0 (-1 + 1)
            if not node:
                return -1
            # the height will be the maximum path from the node's childrens plus one for the
            # current node
            height = max(dfs(node.left, level + 1), dfs(node.right, level + 1)) + 1
            # Then the current level and height is saved in the queryLevel hashmap
            queryLevel[node.val] = [level, height]
            # now we updated our first and second largest hashmaps based on the current height
            # if the current height is larger than or equal to the first, we pass down the later
            # to the secondlargest and save the current height as the largest
            if height >= firstLargest.get(level, -1):
                secondLargest[level] = firstLargest.get(level, -1)
                firstLargest[level] = height
            # if not we check if its larger thant the second one, if yes we replace, otherwise
            # we ignore it
            elif height > secondLargest.get(level, -1):
                secondLargest[level] = height
            # Then we return the current height for recurssion
            return height

        # we call our dsf fucntion with the root node and level 0
        dfs(root, 0)
        # Finally we return an array where, for every query in queries we are gonna add the level of the node evaluated plus the first or secondlargest height depending
        # if the query is equal to the largest height, as its the only way the height of the tree would be altered, the second condition is the equivalent as returning
        # the total height of thr tree as it would remain unaltered. Finally, in the hashmaps we check if the item exists, otherwise we return -1, as if the largest branch
        # is removed, and the node doesn't have any other cousins or brothers the height will be the node's level -1 
        return [queryLevel[query][0] + (secondLargest.get(queryLevel[query][0], -1) if queryLevel[query][1] == firstLargest.get(queryLevel[query][0]) else firstLargest.get(queryLevel[query][0], -1)) for query in queries]
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        count = {}

        def dfs(node):
            if not node:
                return 0

            total = node.val + dfs(node.left) + dfs(node.right)

            count[total] = count.get(total, 0) + 1

            return total

        dfs(root)

        max_freq = max(count.values())

        return [s for s in count if count[s] == max_freq]
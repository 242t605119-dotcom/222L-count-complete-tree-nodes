class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0

        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        left_height = get_height(root)
        right_height = get_height_right(root)

        if left_height == right_height:
            return (1 << left_height) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_height_right(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height

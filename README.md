# LeetCode 222 - Count Complete Tree Nodes

## Problem Description

Given the root of a complete binary tree, return the number of nodes in the tree.

A complete binary tree has every level completely filled except possibly the last level.

## Example

**Input:**

```text
root = [1,2,3,4,5,6]
```

**Output:**

```text
6
```

## Approach

For a complete binary tree, if the height of the leftmost path and rightmost path are equal, the tree is a perfect binary tree.

For a perfect binary tree with height `h`, the number of nodes is:

```text
2^h - 1
```

Otherwise, recursively count the nodes in the left and right subtrees.

## Algorithm

1. If the root is `None`, return `0`.
2. Find the height by following the left children.
3. Find the height by following the right children.
4. If both heights are equal, calculate the nodes using `2^h - 1`.
5. Otherwise, recursively count nodes in both subtrees.
6. Return the total count.

## Time Complexity

`O(log² n)`

## Space Complexity

`O(log n)` due to recursion.

## Key Concepts

* Binary Tree
* Complete Binary Tree
* Recursion
* Tree Height
* Bit Manipulation

## Author

T.nandhini

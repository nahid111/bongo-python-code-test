### Time and Space Complexity for Solution-3
![example tree](question/unnamed.png)

#### Time Complexity
- If we consider the nodes 8 & 7 in the given example tree, Our search begins at the given nodes.<br>
Here, the height of the example tree is 4.<br>
After 3 recursive calls our function should return the node 1 as the LCA of node 8 & 7.

- For the nodes 5 & 6 the LCA is also node 1, which is found after 2 iterations where the tree height is 3.
- Therefore, the Time Complexity for this algorithm is **O(n-1)**

#### Space Complexity
- Considering the above explained cases we get <br>
Space Complexity for this algorithm as **O(h-1)**. <br>
Where **h** is the height of the tree from root to the given nodes.


### For the iterative approach
In this approach we first visit each parent of node1 till root node and store each node in a dictionary/hashtable.<br>
Then we visit each parent of the 2nd given node and compare them with the nodes in the table.<br>
When a match is found, we return it as the LCA.
Here,
- Time complexity is **O(2h)**
- Space complexity is **O(h)**
<br>where **h** is the height of the given tree.

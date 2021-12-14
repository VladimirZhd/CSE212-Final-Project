[<- Back](README.md)

## `Lets's Talk About Trees`

Tree represents the nodes connected by edges. We will discuss binary tree or binary search tree specifically.

Binary Tree is a special data structure used for data storage purposes. A binary tree has a special condition that each node can have a maximum of two children. A binary tree has the benefits of both an ordered array and a linked list as search is as quick as in a sorted array and insertion or deletion operation are as fast as in linked list.

<p align="center">
  <img width="460" height="300" src="binary_tree.jpeg">
</p>

Binary search tree has a certain behavior. A node's left child must have a value less than its parent's value and the node's right child must have a value greater than its parent value.

If all previous data structures were based on the list data structure. Linked list and Binary tree is a class. Each node that we are adding to them is an instance of that class. We will take a look at the tree class and it's main methods.

```python
class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node
    class below is an inner class.  An inner class means that its real
    name is related to the outer class.  To create a Node object, we will
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the
        left and right sub-tree.
        """

        def __init__(self, data):
            """
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """

            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None
```

In the code snippet above you see a `BTS` class. This class is the binary search tree. Also, you see that there is a nested `node` class, this class is for each node that we are going to add to the tree. There is a two init methods. One for the tree and one for each node. to init the tree you would do something like:

```python
binary_tree = BST()
```

This will initialize an empty tree with the root node that is equals to `None`. After that we can use our tree. To use our `Node` class we would need an insert method.

```python
def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data == node.data:
            return
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
```

This is a private method here we are going to handle all our logic. Here we will decide which way every new node need to go. This method shouldn't be accessed outside of the class. We are going to have another insert method, that we can use on our tree instance.

```python
def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root
```

This method is going to use our private method to insert a value. We will access this method on all instances of BTS we are going to create.

### `Recursion`

There is a trick that we need to use to work with binary trees. It is called recursion. Recursion is a function that call itself. When using recursion we need to remember two rules, first is called `base case`. To make sure that we don't get to infinite loop we need to set a base case to get out of the recursion. The second rule is braking our problem to a smaller problem. When we call the function recursively we need to make sure we are calling the function on a smaller problem.

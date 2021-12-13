[<- Back](README.md)

## `Let's Talk About Stacks!`

When you hear a word stack, what is the first thing that comes to your mind? I always think about something like pancakes, stack of socks, stack of any clothes or shoes. Anything that I put on the top of a pile and then I am going to take the last thing that was added to the stack and use it. It is a natural process we rarely got to a stack of pancakes and trying to get one from the middle (in this case we would use a list or a dictionary), rather we grab one on the top. This is stack, it is easy remember that the stack works in this way "last in, first out."

Lets talk about performance. When we append to a stack we are not going through each element that is already there, but we adding to the end, this is O(1) time complexity always would be constant because we adding to the end. The same logic will apply for removing a item from the end. If you want to find a value then in the worse case scenario we will have O(n) if the value you are looking for would be the last value in the loop.

### `Examples`

Let's see it in the code for this example we are going to remove all adjacent duplicates in a string.

-   Given a string of lowercase letters, a duplicate removal consists of choosing two adjacent nd equal letters, and removing them.
-   We repeatedly make duplicate removals on string until we no longer can.
-   Return the final string.

To avoid a brute force (two nested 'for' loops) we will use a stack. We will start with an empty stack and loop through the string. We will check if the stack is not empty and an element is equals to a previous element in the stack. If so, we are going to pop last element in the stack, else we are going to add it to the stack. In the end we will have an empty string.

```python
def removeDuplicates(s: str):
    stack = []

    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)


# Test case
s = "ettene"
print(removeDuplicates(s))
# The output will be 'ne'
```

Next example I want you to solve by yourself.
We are going to check if the parenthesis are valid, meaning they have an opening and closing pair.

-   Given a string with parenthesis, brackets, and curly braces determine if the input string is valid.

An input is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the right order.

Try to solve it using stacks, and compare your solution with mine in the end.
[My Solution](stacks.py)

In this section we learned what stack is and how to use it. Let's move on to the next section and learn more about sets.

[Set ->](set.md)

[<- Back](README.md)

## `Lets's Talk About Sets`

Set is a list that can store multiple values. You would ask why would we use sets if we already have lists in python. The main difference between those two is that sets store unique values only. It is useful in case you what to filter values and get rid of the duplicates in your data. To determine if the value is unique the set data structure is using a `hash` function in the background and stores all values hashed.

To store hashed values sets will grab a last digit of the set and places it to corresponding index, but if that index is already occupied we will have a conflict.

### `Conflict handling`

There is two ways to handle sets conflicts, fist called open addressing. After we hash item we check if the index with corresponding last number in the hash is already occupied, we will check next index and place it to the next open spot.

The second method called chaining. Instead of searching for the next open spot we can store a list of the same hash last digit.

Both of the methods going to affect our performance. Hashing and placing a value to the same index as last digit of hash gives as O(1). But when we using open addressing we would need to check next indexes if we didn't find the value. This potentially will bring us to O(n), as well as chaining whe we would need to go through nested lists.

### `Examples`

Here we are going to got through one example together to understand how sets are working. The second example you would need to solve by yourself, but I will add my solution as well.

### `Problem 1`

Given an array of integers, verify if the array contains any duplicates.
The function should return true if any value appears at least twice in the array,
or false if every element is distinct.

```python
#Input: [3,3,1,2,6,4,1,2,4,5]
#Output: true
#Input: [1,2,3,4]
#Output: false

nums = [21, 13, 35, 31, 12, 35, 10, 9, 9]

def isThereDuplicates(nums):
    return True if len(set(nums)) < len(nums) else False

print(isThereDuplicates(nums)) #this will return true
```

### `Problem 2`

Given a string, count the number of vowels present in given string using Sets.

Examples:

```
Input : Here is a test string
Output : No. of vowels : 6

Input : Hello World
Output : No. of vowels : 3
```

[My Solution](sets.py)

In this section we learned more about sets and ways we can use them in our code.

[Trees ->](tree.md)

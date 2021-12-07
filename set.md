[<- Back](README.md)

## Lets's Talk About Sets

Set is a list that can store multiple values. You would ask why would we use sets if we already have lists in python. The main difference between those two is that sets store unique values only. It is useful in case you what to filter values and get rid of the duplicates in your data. To determine if the value is unique the set data structure is using a `hash` function in the background and stores all values hashed.

To store hashed values sets will grab a last digit of the set and places it to corresponding index, but if that index is already occupied we will have a conflict.

There is two ways to handle sets conflicts, fist called open addressing. After we hash item we check if the index with corresponding last number in the hash is already occupied, we will check next index and place it to the next open spot. The second

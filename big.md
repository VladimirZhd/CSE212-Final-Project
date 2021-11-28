[<- Back](README.md)

## What is the Big-O Notation?

If you choose a software developing as a career path you will hear about it a lot. One of my friends once said, "Out of two resources we have in software developing, one we can increase (memory), and another we can't (time)." Time, this is why we are focusing so much on the Big-O. When writing a program, function, method we need to think if our code time efficient. This is why there are many different data structures, we can use a structure that fits our needs the best and also saves the time during the execution.
For this tutorial our worse case scenario would be O(n) where "n" is a length of our data structure, and the best case O(1) where we will get data in one operation. There is another case that is better than O(n) but not as efficient as O(1), it is called O(log n). We will try to use it in all cases where we can avoid O(n). The one thing you want to remember during your technical interviews avoid O(n^2) as much as possible. If you are using a brute force to get first solution you can do O(n^2) only if you are going to improve the performance in you next solution for the same problem.

Here is a chart you can refer for better understanding:  
![big-o chart](big-o.png)

#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
Time complexity is 0(n)

b)
At first I thought O(n^2) because of the nested loop but j grows at twice the rate of the parent loop and only while less than n, so: 0(log n)

c)
0(n)

Because the bunnies(n) but the rest are constants 0(2 + n), simplified, 0(n)

## Exercise II

We would do a a binary search of the floors to find out which floor the eggs break on

So if there were 15 floors like

f= [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Starting in the middle

mid = f // 2

and dividing and conquering just like we have been for binary searches. If it broke at 8, then we know at least f >= 8, and we would split the lower half in two and repeat until we have the starting point. If it didn't break at 8 we'd split the upper half and then split again until we find the floor

0(log n) for time complexity

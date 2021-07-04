The Grandest Staircase Of Them All
==================================

With the LAMBCHOP doomsday device finished, Commander Lambda is preparing to debut on the galactic stage -- but in order to make a grand entrance, Lambda needs a grand staircase! As the Commander's personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so they can pick the one with the most options. 

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31
 
But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

#
#
#
##
41

#
##
##
32

Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(200)
Output:
    487067745

Input:
solution.solution(3)
Output:
    1

## Attempt \#1 (Fail)

1,0
2,0
3,1 - [(2,1)]
4,1 - [(3,1)]
5,2 - [(4,1), (3,2)]
6,3 - [(5,1), (4,2), (3,2,1)]
7,4 - [(6,1), (5,2), (4,3), (4,2,1)]
8,5 - [(7,1), (6,2), (5,3), (5,2,1), (4,3,1)]
9,7 - [(8,1), (7,2), (6,3), (6,2,1),  (5,4), (5,3,1), (4,3,2)]
10,9 -[(9,1), (8,2), (7,3), (7,2,1), (6,4), (6,3,1), (5,4,1), (5,3,2), (4,3,2,1)]

Notice that when we have a value that belongs to the series (1+2+3...+n), we get a n digit number. So, like some values in the series are [1, 3, 6, 10, 15]. So, my first hypothesis was trying to see if the pattern fits and it did I wanted to understand the cause to validate the relationship. 


So, we could start by returning 0 for all values less then 3. Then the algorithms would be as the following
1. [loop] while n>=k(k+1)/2. Because, if the value is bigger then that then we cannot create an array of size k 
2. Create an array of size k, like [n-A_k, ... 1] like so for an array of size 3 we would have [n-3, 2, 1]. For an array of size 4 we would have [n-6, 3, 2, 1]
3. [inner loop] while we can keep shifting the value to the right
    a. Move value from cur index to the next index until the move will be invalid


Example
n=10
k=1, A_k=(1)(2)/2=1
(9,1)
...
(6,4)
- We have 4 elements of size 2

k=2,  A_k=(2)(3)/2=3
(7,2,1)
(6,3,1) - move over
(5,4,1) - move over
(5,3,2) - move over at second position because it is still valid
- We have 4 elements of size 3

k=3, A_k=(3)(4)/2=6
(4,3,2,1) - cannot move anymore

So, we have 4+4+1=9 - which checks out

Okay let's think of a possible counter-examples

What if we had
7,2,1
6,3,1
5,4,1

Why does this break the algorithm? 
Cause if we were at
6,3,1
we would go to 
6,3,2
And, we have now way to go to 5,4,1


<!-- But, this feels too slow, lets see what the time complexity of our algorithm would be? 
So, the first loop will run  O(k) or O(√n). Where n=k(k+1)/2
then the inner loop is a bit tricky. Our first element can be moved over [n/2] atmost to the next position. And, then [n/4]. So, the sum of the series [n/2+n/4+n/8+...+1]. Which is atmost 2n-1. So, we have  O(√n). O(2n)= O(n^(1.5)). 
 -->

## Attempt \#2 (Partition)

A quick google of "way to sum up to a number" reveals the mathematical concept of "Partitions". Skimming through the Wikipedia, I found the section for distinct subset which has a weird equation. The order in sums don't matter. So, these two problem are equivalent.
If we use [this list](http://oeis.org/A008289/list) and try to do the problems via recursion, we notice this list has our answer but is always bigger by one. This is because we aren't counting a lonesome number as a valid staircase.

So, we just need to recreate the formula. 
First, we need the Pentagonal numbers: a(n) = n\*(3\*n-1)/2


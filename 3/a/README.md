Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

Input:
solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
Output:
    [7, 6, 8, 21]

Input:
solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
Output:
    [0, 3, 2, 9, 14]


Approach
==========
Approach 1(fail)- Solve in paper an try to reverse engineer process
Problem - algebra hard to replicate

[
    [0,1,1,0], //S0
    [0,0,0,0], //S1
    [1,0,0,1], //S2
    [0,0,0,0]  //S3
]

If we just try to get the probability of hitting state S3
We can break down the probability of reaching S3 from each state

If we look at S0 we have two potential path to S3
1. 0.5\*P(S1, S3)  
2. 0.5\*P(S2, S3)
which gives us  
P(S0, S3) 
= 0.5\*P(S1, S3) + 0.5\*P(S2, S3) (1)

// Now we look at probability from S1 to go to S3
P(S1,S3)=0 (2)

// Now we look at probability from S2 to go to S3
P(S2, S3) 
= 0.5\*P(S0, S3) + 0.5  
= 0.5\*{0.5\*P(S1, S3) + 0.5\*P(S2, S3)} + 0.5  // sub in (1)
= 0.5\*{0.5\*0 + 0.5\*P(S2, S3)} + 0.5 // sub in (2)
= 0.5\*{0.5\*P(S2, S3)} + 0.5
= 0.25\*P(S2, S3) + 0.5
So, we have
P(S2, S3) = 0.25\*P(S2, S3) + 0.5
=> 0.75\*P(S2, S3) = 0.5
=> P(S2, S3) = (2/3) (3)

// Now we can put both equation in (1) to get transition value to S2
P(S0, S3) 
= 0.5\*P(S1, S3) + 0.5\*P(S2, S3) 
= 0 + 0.5\*(2/3) 
= 1/3

----------------------------------------------------------

Now we can do the same for P(S0, S1)
P(S0, S1) = 0.5 + 0.5\*P(S2, S1) (1) // set up formula
P(S3,S1)=0 (2)  // probability on terminal state is always 0 
P(S2,S1)=0.5\*P(S3,S1) + 0.5\*P(S0, S1) 
=0.5\*P(S0, S1) // sub in (2)
...And using the same algebra we can see the probability are flipped so we get
P(S2,S1) = 1/3
P(S0,S1) = 2/3

So, our final vector will be 
[S1,S3,denominator]
[1,2,3]

----------------------------------------------------------
What we know 
1. Transition for terminal state to any state is always 0
2. Probability of a stating hitting itself is a 100% - P(Si,Si)=1
3. Probability of a stating reaching another state is the sum of P_ij\*h_jA : the sum of the transition probability from the current state to all states multiplied by the probability of reaching the destination state from the new state.

Approach 2 (fail)
We could try to keep running our calculation recursively until it stabilizes. THis takes too long.
e.g
\[initial state vector\]\[transition matrix\]^m = \[m-state probability\]

v_{n-1}\*P=v_n    -equation
stabilizes where v_{n-1}=v_n
so we can rewrite as
v\*P=v
v\*P-v=0
v(P-1)=0

Approach 3
Use a formula that calculates matrix probability
Let A be out probability matrix
Let v be our row vector where we have 1 for the first element and 0 for the rest of the rows
Let w = be the vector representing the probability of the process ending at i.
w=v(I−A)^-1




Reference
https://cs.stackexchange.com/questions/67487/what-algorithm-to-find-end-state-probabilities











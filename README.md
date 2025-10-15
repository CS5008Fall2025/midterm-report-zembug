[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kdfTwECC)
# Midterm p1: Report on Analysis of Fibonacci  Series
* **Author**: Emily Despres
* **GitHub Repo**: (https://github.com/CS5008Fall2025/midterm-report-zembug/blob/main/README.md)
* **Semester**: Fall 2025
* **Languages Used**: c, python

> You are free to rename/ modify these sections as you need (and don't forget to remove this line..)

## Overview

This report explores the Fibonacci sequence, a foundational concept in mathematics and computer science known for its recursive structure and widespread applications. The sequence begins with 0 and 1, and each subsequent number is the sum of the two preceding ones. Mathematically, it is defined as:

$$F(n) = F(n - 1) + F(n - 2)$$

with base cases:

$$F(0) = 0 \quad \text{and} \quad F(1) = 1$$

The sequence progresses as:

 $$0,\ 1,\ 1,\ 2,\ 3,\ 5,\ 8,\ 13,\ 21,\ 34,\ 55,\ 89,\ 144,\ 233,\ 377,\ 610,\ 987,\ 1597,\ 2584,\ 4181\ldots$$

 
First introduced to Western mathematics by Leonardo of Pisa (Fibonacci) in his 1202 book Liber Abaci, the sequence was originally used to model rabbit population growth under ideal conditions. [1][2]

Many patterns in nature reflect the Fibonacci sequence not just in appearance, but in function. For example, the number of petals on certain flowers often corresponds to Fibonacci numbers. Lilies typically have 3 petals, buttercups have 5, and some varieties of daisies can have 34. [1] These numbers are not arbitrary. They result from a process called phyllotaxis, which governs how plants grow and arrange their leaves, petals, or seeds. Fibonacci based arrangements ensure that each leaf or petal receives maximum sunlight and minimizes overlap with others. [3] Similarly, the spiral patterns found in sunflowers, pinecones, and pineapples often match consecutive Fibonacci numbers, helping distribute seeds evenly and efficiently [4].

The sequence’s relevance extends into algorithm design, dynamic programming, and number theory. It serves as a benchmark for evaluating recursive depth, computational efficiency, and memory usage across different programming paradigms. In this report, I analyze and compare three common approaches to computing Fibonacci numbers: recursive, iterative, and dynamic programming, using both C and Python. Each method offers different strengths and challenges in terms of time complexity, space usage, and implementation style. The goal is to understand how algorithmic design and language features influence performance and developer experience.

To begin my analysis of the three approaches, I first examine their Big O notation to understand the time and space complexity involved in executing each algorithm.

| Version |  Big O | Space Used | 
| :-- | :-- |  :-- |
| Recursive | $O(2^n)$  | $O(n)$ |
| Iterative | $O(n)$ | $O(1)$ |
| Dynamic Programming | $O(n)$ | $O(n)$ |

With the recursive approach, the Big O notation is $O(2^n)$,  representing exponential time. Each call to $F(n)$, the nth Fibonacci number, generates two additional calls: $F(n-1)$ and $F(n-2)$. This recursive branching continues until the base cases are reached, producing a tree like structure of calls. As a result, the number of operations increases exponentially with $n$, and many values are recomputed multiple times. For space it uses $O(n)$. That’s because each time the function calls itself, it adds a new layer to the call stack. These layers build up until the base case is reached, and the total number of active calls depends on how deep the recursion goes. Since the depth increases with the input size, memory usage grows linearly with $n$. [5]

Recursive pseudocode:
```text
function Fibonacci(n)
    if n is 0 or 1
        return n

    else 
        return Fibonacci(n-1) + Fibonacci(n-2) 
```

With the iterative approach, the Big O notation is $O(n)$, representing linear time. This is because the loop runs once for each value from 2 up to $n$, performing a constant-time operation at each step. The algorithm starts with the base cases and computes each Fibonacci number in sequence, avoiding any redundant calculations. For space, it uses a constant $O(1)$, since it only requires a fixed number of variables to track the current and previous values. As a result, memory usage remains constant regardless of the input size. [6]

Iterative pseudocode:
```text
function Fibonacci(n)
    if n is 0
        return 0

    create array arr of size (n + 1) // list to store Fibonacci numbers from index 0 to n
    set arr[0] to 0 // first Fibonacci number is 0
    set arr[1] to 1 // second Fibonacci number is 1

    for i from 2 to n // loop from index 2 to n
        set arr[i] = arr[i - 1] + arr[ i - 2] // each number is sum of previous two
    return arr[n] //return nth Fibonacci number
```

With the dynamic programming approach, the Big O notation is $O(n)$, representing linear time. This is because each Fibonacci number from $F(2)$ up to $F(n)$ is computed exactly once, using previously stored values to perform constant-time additions at each step. The algorithm begins with the base cases and builds the sequence incrementally, storing each result in a data structure for reuse. For space, it uses $O(n)$, since it maintains an array or list of size $(n+1)$ to hold all computed values from $F(0)$ through $F(n)$. As a result, both time and memory usage grow linearly with the input size. [7]


## Empirical Data & Discussion 


## Language Analysis


### Language 1: C



### Language 2: Python



### Comparison and Discussion Between Experiences


## Conclusions / Reflection

## References


1. GeekforGeeks. 2025. Real Life Applications of Fibonacci Sequence. (July 23, 2025). Retrieved October 12, 2025 from   https://www.geeksforgeeks.org/maths/real-life-applications-of-fibonacci-sequence/

2. The Department of Mathematics and Computer Science. n.d. Fibonacci's Rabbits. Retrieved October 12, 2025 from https://mathcenter.oxford.emory.edu/site/math125/fibonacciRabbits/

3. Biolecta. 2024. The Fibonacci Sequence: Its Importance in Math and Nature. (December 5, 2024) Retrieved October 12, 2025 from https://biolecta.com/articles/fibonacci-sequence-importance-mathematics-nature/

4. Insteading. 2023. The Fibonacci Sequence in Nature. (September 6, 2023). Retrieved October 12, 2025 from
https://insteading.com/blog/fibonacci-sequence-in-nature/

5. Real Python. 2023. A Python Guide to the Fibonacci Sequence. (December 1, 2023) Retrieved October 14, 2025. https://realpython.com/fibonacci-sequence-python/

6. matrixRead. 2020. Fibonacci Series - Iterative vs Recursive. (October 16, 2020). Retrieved October 14, 2025 from https://matrixread.com/fibonacci-series-iterative-vs-recursive/

7. GeeksforGeeks. 2025. Dynamic Programming (DP) Introduction. (August 7, 2025). Retrieved October 14, 2025 from https://www.geeksforgeeks.org/dsa/introduction-to-dynamic-programming-data-structures-and-algorithm-tutorials/



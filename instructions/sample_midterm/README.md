# Midterm p1: Report on Analysis of Pascal's Triangle
* **Author**: Random Student
* **Semester** Spring 2023
* **Languages Used**: c, python

> This is a sample of what to write. It is not necessarily "A" quality work, or perfect. It was quickly written to help
address common questions on what each category is needing. As a reminder, while this uses Pascal's Triangle, your
> report will be using the Fibonacci Series.

## Overview
This report focuses on the speed differences between implementations of [Pascal's Triangle]<sup>[1]</sup>. It is worth mentioning, that while it is known as Pascal's Triangle in the western world, it goes by multiple names as discovered by multiple cultures throughout the world. Some names include: Khayyam (مثلث خیام) and Yang Hui (杨辉三角; 楊輝三角) Triangle.

Pascal's triangle represents the binomial coefficients as a triangle staring with 1 and progressing. It can be presented mathematically
as:

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

A typical triangle, to N = 10 would look like the following:
```text
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
```

There are multiple ways to implement Pascal's Triangle with code, each discussed in more detail below. However,
for the implementations I used in this report the following chart represents the Big O value.

| Version |  Big O | Space Used | 
| :-- | :-- |  :-- |
| Iterative | $O(n^2)$ | $O(n^2)$ |
| Recursive | $O(2^n)$  | $O(n)$ or $O(1)$ |
| Dynamic Programming | $O(n^2)$ | $O(n^2)$ |

The iterative version has two nested for loops, developing the $O(n^2)$, while also needing to store the previous 
line, causing the room increase. There is a version that using constant room of a single variable, but it fails
on larger notations.  The recursive version is in pseudocode:

```text 
for i..n
    RV(n, i)

RV(n,i)
   if i == 1 or i == n: return 1
   return  RV(n - 1, i) + RV(n - 1, i - 1)
```
Each row of the triangle contains one more element than the previous row. To generate the nth row, the algorithm must 
calculate n elements, each of which is the sum of two elements in the previous row. 
This means that the algorithm must make $2^{(n-1)}$ recursive calls to generate the entire nth row. 
However, the only space it has to keep is the final row  itself (or if printing, no space is used), 
making the space used either $O(n)$ or $O(1)$. 

The dynamic programming version stores the value of (n,i) for each call, making the second branch constant time, 
bringing the worst case back to $n*n = O(n^2)$ time, but at the cost of $O(n^2)$ room. 

For this analysis, I selected Python for my second language. The reason for this selection, other than it is a well known
language, is that it has builtin functions to assist with dynamic programming knowing as `lru_cache` and `cache` in
the builtin functools library. This allowed to experiment with the builtin tools, while also writing
in a language designed for quick development and experimentation. 

## Empirical Data & Discussion 
For all empirical results, I maxed out the time interval to 60 seconds. This allowed for execution of code
in a timely manner, while still being able to run multiple iterations ([test script]).

Below we highlight both the speed and operations for all algorithms. 


### Operations Comparison
The number of operations for each algorithm was calculated by adding a counter to the functions. While the counter could vary a bit based on where we added it, they were added in effectively the same spot for both C and Python versions of the algorithm. It is worth noting, that in the python dynamic programming version, the counter was take into account by the recursive algo, and due to the cache, it produced the same results as where we added the counter in the C version, showing the counter placement was correct.

The first 28 rows of the triangle show in the chart below. Anything after 28 cased the recursive version to time out, so only showing the first 28 rows. For full operations count, see [ops_pascal_run_c.csv](ops_pascal_run_c.csv) and [ops_pascal_run_python.csv](ops_pascal_run_python.csv).


#### Operations Count 
| **N** | **Iterative** | **Dynamic Programming** | **Recursive** |
|-------|---------------:|-------------------------:|---------------:|
| 1     | 1             | 0                       | 0             |
| 2     | 3             | 1                       | 1             |
| 3     | 6             | 3                       | 4             |
| 4     | 10            | 6                       | 11            |
| 5     | 15            | 10                      | 26            |
| 6     | 21            | 15                      | 57            |
| 7     | 28            | 21                      | 120           |
| 8     | 36            | 28                      | 247           |
| 9     | 45            | 36                      | 502           |
| 10    | 55            | 45                      | 1013          |
| 11    | 66            | 55                      | 2036          |
| 12    | 78            | 66                      | 4083          |
| 13    | 91            | 78                      | 8178          |
| 14    | 105           | 91                      | 16,369         |
| 15    | 120           | 105                     | 32,752         |
| 16    | 136           | 120                     | 65,519         |
| 17    | 153           | 136                     | 131,054        |
| 18    | 171           | 153                     | 262,125        |
| 19    | 190           | 171                     | 524,268        |
| 20    | 210           | 190                     | 1,048,555       |
| 21    | 231           | 210                     | 2,097,130       |
| 22    | 253           | 231                     | 4,194,281       |
| 23    | 276           | 253                     | 8,388,584       |
| 24    | 300           | 276                     | 16,777,191      |
| 25    | 325           | 300                     | 33,554,406      |
| 26    | 351           | 325                     | 67,108,837      |
| 27    | 378           | 351                     | 134,217,700     |
| 28    | 406           | 378                     |   268,435,427     |



### Recursive Versions
![Recursive Runtime]  
With both version, it is easy to see the exponential growth of the recursive version. The C version timed out at N=33, while the python version topped out at N=28. The chart uses a double axis, the python axis is on right hand side showing at N=28 the speed was roughly 54 sections. The C version with N=33 was roughly 40 seconds (causing 34 to go above 60 seconds).


### Iterative and Dynamic Programming Versions
Due to the increased speed with the iterative and dynamic programming versions, we were able to look at much
larger N values to see a more gradual curve. 

![Iterative and Dynamic Programming Runtime]

The chart uses a double axis, the python axis is on right hand side. Both the dynamic programming version align nearly exactly in their speed times, minus the overall speed difference between the languages. The iterative has a bit more variation between the languages, but still follows a similar curve. The curve for both the iterative and dynamic programming versions is $O(n^2)$, as expected. 

It is possible the differences in speed could be to the function call overhead, and neither version went through heavy optimization. 

### Speed Comparison Between Languages
In all cases, the C version was faster than the python version. However, the average difference when running the algorithm was minimal, but the difference at larger numbers of N was more noticeable.

| Version | Average Speed Difference | Max Speed Difference |
| :-- | :-- | :-- | 
| Iterative | 1.603057459 |	8.032182| 
| Dynamic Programming | 3.39702299|	14.377136 | 
| Recursive | 3.942182071 |	54.427153 | 

Overall, the algorithms follow the expected Big $O$ analysis of $O(n^2)$ for both the iterative and dynamic programming versions. The recursive version is $O(2^n)$, but the space used is $O(n)$ or $O(1)$ depending on the version. In all cases, the C implementation was faster than the python implementation, though sometimes minimal depending on the value of $N$.




## Language Analysis

The code writing can be found in the following files:
* [pascalr.c]  -- implementation of functions in c
* [pascal.py] -- implementation of function in python
* [test_runner.py] -- run script to help with tests and keep timings

For the most part, I started developing code in C, as I already had the examples provided in class. I then
switched to python and mirrored those examples. However, I found myself exploring different implementations
more in python, and then updating the C versions after those were explored. 

### Language 1: C

Originally, for the C version, I was taking inspiration from [Geeks for Geeks]<sup>2</sup>. Their version
mentioned the use of combinations, or the formula of 

```
C(n, r) = C(n, r-1) * (n – r + 1) / r
```

The problem with this formula is that that while it is quick at $O(n^2)$ and only uses $O(1)$ space, it actually
started error at n > 60. Looking into it more, it was found the that the multiplication would cause an overflow
before the division action as shown on [Wikipedia Binomial Coefficient]<sup>3</sup>. 

This caused me to explore the $O(n^2)$ plus $n^2$ space version that uses an array to implement the code. 

The example used an auxiliary array setup on the stack  This also caused errors at n > 1024 due to 
limited memory constraints on a virtual machine. I ended up modifying the
code to store memory on the heap, and only as much was needed for each individual row. 

```c
ull** triangle = (ull**) malloc((n+1) * sizeof(ull*));
for (int i = 0; i < n; i++)
{
   triangle[i] = (ull*) malloc((i+1) * sizeof(ull));
/* ... and so on */
```

The code for both the recursive and dynamic programming version were trivial and matched the formula exactly. 
```c  
ull pascaldp(int n, int i)
{
    if (n == i || i == 0) {
        return 1;
    }else if (table[n][i] > 0) {
        return table[n][i];
    }else {
        table[n][i] = pascaldp(n - 1, i) + pascaldp(n - 1, i - 1);
        return table[n][i];
    }
}

ull pascalr(int n, int i)
{
    if (n == i || i == 0)
    {
        return 1;
    }
    else
    {
        return pascalr(n - 1, i) + pascalr(n - 1, i - 1);
    }
}

```
In order to make the code more efficient, I needed to add a recursion helper function that would either only generate the
Nth row, or that would generate every row up to N. 

Additionally, for the C versions, I used ints for my arguments as they were easier to convert, and had to write my own
print functions along with help functions for the final program. 

### Language 2: Python
The python version was written with the recursive version in mind first.

```python
def pascal_r(n: int, i: int) -> int:
    if n == i or i == 0:
        return 1
    return pascal_r(n - 1, i) + pascal_r(n - 1, i - 1)
```

To allow it to use dynamic programming, I only had to add the cache wrapper function

```python 
from functools import lru_cache
@lru_cache(maxsize=None)
def pascal_dp(n: int, i: int) -> int:
    if n == i or i == 0:
        return 1
    return pascal_dp(n - 1, i) + pascal_dp(n - 1, i - 1)
```

This function caches any result of a "pure function", which when programming in python is ideal to use. It has
the cost of a space overhead, but with one addition, code becomes faster.  However,
when running the code, I ran into the stack size limitation built into python on recursive calls which then had to be increased. 



### Comparison and Discussion Between Experiences
C runs  faster than Python, and in every case the iterative runs faster than the dynamic programming even
if the Big O for them is the same. However, there are further optimizations of the recursive version that I did not
implement including using the symmetry of the triangle to my advantage. It would have been much
more complex to make such changes in the iterative version. Additionally, the iterative code was more complex to write, 
and I spent more time writing and debugging it than I did other versions. 

The simplicity of adding caching to python was noticeable, but the speed difference may not
make the simplicity worth it. 

Briefly explored, but slightly against the spirit of this report was "precaching" the triangle. With both python
and C, I could quickly write out a file that had N to a high number (20,000). Then using the dynamic programming
version, I was able to load that file and thus make my access time of $O(1)$ at the cost of a slower start up time
for the program. This idea came from my initial python runs where I just called the code, and dynamic programming
version was running much faster due to the cache remaining in memory and not unloading. Also, the way the lru_cache 
works, I explored running N to 50,000 as a separate thread. Since the cache uses a pure function, it would mean
the started thread would have a chance of generating the needed N row before the program generated it. While not 
effective  for a single script run, this would have had an advantage if the 
program was interactive asking a client for various  runs or if the triangle was being 
used for other computations. 



## Conclusions / Reflection
In conclusion, the iterative solution was always faster than the other versions, simply because the triangle
is built on the idea that the previous row needs to be built before it. However, the dynamic programming
version difference wasn't noticeable, and much easier to code. Furthermore, something the iterative version
would not allow is precaching the data, whereas the dynamic programming would adapt nicely if the program
kept caches of previous runs and leaded those runs as needed. There would be a file load overhead, but at the
advantage of increased speed. At the same time, when the iterative C version as calculating N=50,000 is about 13 seconds, 
it wouldn't make sense to spend much time on alternative solutions - it was already blazing fast 
compared to other solutions. 

I learned a lot about dynamic programming and pascals triangle. Admittedly, I should have explored more of the
symmetry optimizations, but in effort to get out this assignment in time, I ended up not fully 
exploring those solutions. I believe such exploration would have helped the time 
difference between the iterative and dynamic programming variations.  It was also nice to see how easy it is
to turn a function in python to a "dynamic programming" focused function. While it shouldn't be used in every
place, for most pure functions it would make sense to keep the catch active, though at a limited size for 
memory constraints. One area I did not explore was the interoperability between C and python. The builtin utility 
of python made it a pleasant language to use. I could have prototyped the algorithm in python, wrote it in c,
and then had my python code call the C version directly. This would have created the best of both worlds,
and an easy fall back if the C version had machine constraint issues.  Something to explore in the future. 

## References

1. Wikipedia, "Pascal's triangle," Wikipedia: The Free Encyclopedia, 
October 3, 2022. https://en.wikipedia.org/wiki/Pascal%27s_triangle. 
Accessed on: February 16, 2023.
2. GeeksforGeeks, "C Program to Print Pascal Triangle," GeeksforGeeks, March 10, 2021. 
https://www.geeksforgeeks.org/c-program-to-print-pascal-triangle/. Accessed on: February 16, 2023.
3. Wikipedia, "In programming languages," Binomial coefficient, Wikipedia: The Free Encyclopedia, 
January 15, 2023. https://en.wikipedia.org/wiki/Binomial_coefficient#In_programming_languages. 
Accessed on: February 16, 2023.

<!-- auto references -->
[Pascal's Triangle]: https://en.wikipedia.org/wiki/Pascal%27s_triangle
[Recursive Runtime]: recursive_run_time.png
[Iterative and Dynamic Programming Runtime]: iter_dp_runtime.png
[test script]: test_runner.py
[pascalr.c]: pascalr.c
[pascal.py]: pascal.py
[test_runner.py]: test_runner.py
[Geeks for Geeks]: https://www.geeksforgeeks.org/c-program-to-print-pascal-triangle/
[Wikipedia Binomial Coefficient]: https://en.wikipedia.org/wiki/Binomial_coefficient#In_programming_languages
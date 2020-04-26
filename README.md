# Overview
* Open source implementations for basic data structures and algorithms: [Algorithms in Python](https://github.com/TheAlgorithms/Python) 

## LeetCode - Problems and Solutions

### Bit Manipulation
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Array
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python]() | 1. Hash O(n) and O(n) space.<br>2. Sort and search with two points O(n) and O(1) space. |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | [Python]() | 1. Set and compare length<br>2. Sort and check i,i +1|
| 238 | [Product of Array Except Self](https://leetcode.com/problems/contains-duplicate/) | [Python]() | 1. Set and compare length<br>2. Sort and check i,i +1|

### String
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Python]() | Add all curr, if curr > prev, then need to subtract 2 * prev |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/roman-to-integer/) | [Python]() | Add all curr, if curr > prev, then need to subtract 2 * prev |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [Python]() | 1. Stack<br>2. Replace all parentheses with '', if empty then True |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [Python]()| Exclude non-alphanumeric characters and compare O(n) |
| 1417 | [Reformat The String]() | | |


### Linked List
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Stack
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Queue
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Heap
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Tree
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Hash Table
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | [Python]() | 1. Hash or set, O(n) and O(n)<br>2. xor O(n) and O(1) |
| 1418 | [Display Table of Food Orders]() | | |

### Math
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | [Python]() | Overflow when the result is greater than 2147483647 or less than -2147483648.
| 69 | [Sqrt(x)](https://leetcode.com/problems/climbing-stairs/) | [Python]() | Bottom-up DP, dp[i] = dp[i - 2] + dp[i- 1] <br>1. O(n) and O(n)<br>2. Only two variables are needed, O(n) and O(1) |
| 202 | [Happy Number](https://leetcode.com/problems/count-primes/) | [Python]() | [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity), O(nloglogn) and O(n) |

### Two Pointers
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Sort
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Recursion
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Binary Search
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |
| 350 | [Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns/) | [Python]() | Backtracking, O(n!) and O(n) |


### Binary Search Tree
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Breadth-First Search
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Depth-First Search
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Python]() | 1. Quick union find, O(nlogn) and O(n^2)<br>2. BFS with marks, O(n^2) and O(1) |

### Backtracking
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

 
### Dynamic Programming
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |
| 64 | [Minimum Path Sum](https://leetcode.com/problems/unique-paths-ii/) | [Python]() | Bottom-up DP, dp[i][j] = dmap[i-1][j] + dmap[i][j-1] (if block, then 0), O(mn) and O(mn) |

<!---
### Greedy
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Graph
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |


### Geometry
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Simulation
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Design
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

### Concurrency &hearts;
| # | Title | Solution | Note |
|---| ----- | -------- | ---- |

--->

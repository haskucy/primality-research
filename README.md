# Primality Research Repository

Welcome to the Primality Research Repository! This repository contains research on primality testing algorithms, which are used to determine whether a given number is a prime number.

## Algorithms

In this repository, we delve into various types of primality testing algorithms, including:

1. **Brute Force**: This algorithm checks whether a number is divisible by any number less than itself. While simple, it can be inefficient for large numbers.
2. **Trial Division**: Similar to the brute force method, trial division checks for divisibility up to the square root of the number being tested. It provides a slight optimization over the brute force algorithm.
3. **Fermat Primality Test**: This probabilistic algorithm uses Fermat's Little Theorem to test for primality. It relies on randomly selected witnesses to provide a probabilistic determination of primality.
4. **Miller-Rabin Primality Test**: Another probabilistic algorithm, Miller-Rabin test uses a similar approach as the Fermat test but employs multiple witnesses to improve accuracy.
5. **Deterministic Primality Tests**: These algorithms guarantee a definitive answer for primality. Examples include the AKS primality test and the Elliptic Curve Primality Proving (ECPP) algorithm.

## To-Do List

Here are some tasks you can consider adding to your to-do list for further research and improvement:

- Implement and analyze the performance of additional primality testing algorithms.
- Explore and experiment with parallelized versions of existing algorithms to leverage the power of multi-core processors.
- Investigate the impact of various number representations (e.g., binary, decimal, etc.) on the efficiency of primality testing algorithms.
- Research recent developments and advancements in primality testing, such as the use of machine learning or quantum algorithms.
- Create benchmarking tests and comparisons to evaluate the relative performance of different algorithms.
- Document and publish your findings and discoveries in the field of primality research.

Feel free to contribute to this repository by adding your own research, algorithms, or improvements!

Please customize the algorithms section and the to-do list based on the specific research you have conducted or plan to undertake.

## Things I Need To Do
1. Implement isprime() with 6x+y for faster calculation
2. Implement isprime() with nx+y for faster calculation
3. Implement isprime() with non bruteforce method
4. Implement allprime()

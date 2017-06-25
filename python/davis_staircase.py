"""
Recursion: Davis' Staircase

https://www.hackerrank.com/challenges/ctci-recursive-staircase

Davis has s staircases in his house and he likes to climb each staircase 1, 2, or 3 steps at a time. Being a very
precocious child, he wonders how many ways there are to reach the top of the staircase.

Given the respective heights for each of the s staircases in his house, find and print the number of ways he can climb
each staircase on a new line.

Input Format
The first line contains a single integer, s, denoting the number of staircases in his house.
Each line i of the s subsequent lines contains a single integer, n, denoting the height of staircase i.

Constraints
1 <= s <= 5
1 <= n <= 36

Output Format
For each staircase, print the number of ways Davis can climb it in a new line.

Sample Input
3
1
3
7

Sample Output
1
4
44
"""


def paths(n):
    s0, s1, s2 = 1, 1, 2
    for _ in range(n):
        s0, s1, s2 = s1, s2, s0 + s1 + s2
    return s0


if __name__ == '__main__':
    for i in [1, 3, 7]:
        print(paths(i))

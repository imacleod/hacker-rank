"""
Strings: Making Anagrams

https://www.hackerrank.com/challenges/ctci-making-anagrams

Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character
deletions required to make and anagrams. Any characters can be deleted from either of the strings.

Input Format
    The first line contains a single string, a.
    The second line contains a single string, b.

Constraints
    1 <= a, b <= 10^4

    It is guaranteed that a and b consist of lowercase English alphabetic letters (i.e., a through z).

Output Format
    Print a single integer denoting the number of characters to delete to make the two strings anagrams of each other.

Sample Input
cde
abc

Sample Output
4
"""


from collections import Counter


def search_strings(s1, s2):
    total_del = 0
    c1 = Counter(s1)
    c2 = Counter(s2)
    c1.subtract(c2)
    for i in c1.values():
        total_del += abs(i)

    return total_del


def number_needed(s1, s2):
    """ Return number of character deletions required to make anagram """
    anagram_deletions = 0
    anagram_deletions += search_strings(s1, s2)

    return anagram_deletions


if __name__ == '__main__':
    a = 'cde'
    b = 'abc'
    print(number_needed(a, b))

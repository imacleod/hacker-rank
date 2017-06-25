"""
Merge Sort: Counting Inversions

https://www.hackerrank.com/challenges/ctci-merge-sort

In an array, the elements at indices i and j (where i < j) form an inversion if arr[i] > arr[j]. In other words,
inverted elements and are considered to be "out of order". To correct an inversion, we can swap adjacent elements.

For example, consider [2, 4, 1]. It has two inversions: (2, 1) and (4, 1).

Output Format
For each of the datasets, print the number of inversions that must be swapped to sort the dataset on a new line.

Sample Input
2
5
1 1 1 2 2
5
2 1 3 1 2

Sample Output
0
4
"""


count = 0


def count_inversions(a):
    global count
    count = 0
    merge_sort(a)
    return int(count)


def merge_sort(a):
    mid = len(a) // 2
    if not mid:
        return a
    return merge(merge_sort(a[:mid]), merge_sort(a[mid:]))


def merge(a, b):
    global count
    ans_idx = 0
    len_a = len(a)
    len_b = len(b)
    ans = (len_a + len_b) * [0]
    a_idx = 0
    b_idx = 0
    while len_a > a_idx and len_b > b_idx:
        a_val = a[a_idx]
        b_val = b[b_idx]
        if a_val <= b_val:
            ans[ans_idx] = a_val
            a_idx += 1
        else:
            # Inversion
            ans[ans_idx] = b_val
            b_idx += 1
            count += len_a - a_idx
        ans_idx += 1

    # Process remaining elements in un-exhausted list
    if len_a > a_idx:
        while len_a > a_idx:
            ans[ans_idx] = a[a_idx]
            a_idx += 1
            ans_idx += 1
    elif len_b > b_idx:
        while len_b > b_idx:
            ans[ans_idx] = b[b_idx]
            b_idx += 1
            ans_idx += 1
    return ans


if __name__ == '__main__':
    inputs = [[1, 1, 1, 2, 2], [2, 1, 3, 1, 2]]
    for i in inputs:
        print(count_inversions(i))

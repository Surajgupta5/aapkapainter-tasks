"""
Write a code that prints out the first occurrence of a duplicate in a given array of integers
    Sample Input: [1,2,3,2,1]
    Output: 1
"""
def firstDuplicateNumber(a, n):
    for i in range(n):
        if a.count(a[i]) > 1:
            return a[i]
    return "Array contains no duplicate number..."


if __name__ == '__main__':
    arr = [1, 2, 3, 2, 1]
    n = len(arr)
    result = firstDuplicateNumber(arr, n)
    print(result)

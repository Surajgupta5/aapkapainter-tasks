"""
Write a code that prints out individual scores of two players in a game of cricket
 where score is given as runs per ball in an array. In a game of cricket a person changes strike
 if he scores an odd number, and keeps strike with him if he scores an even number.
  No need to consider changing strike after every 6 balls or an over.
    Sample Input1: [1,2]
    Output1: p1: 1, p2: 2
    Sample Input2: [1,2,3,2,1]
    Output2: p1: 4, p2: 5
"""


def countingRuns(a, n):
    p1, p2, flag = 0, 0, 1
    for i in range(n):
        if flag != 0:
            if a[i] % 2 != 0:
                p1 = p1 + a[i]
                flag = 0  # for changing the strike to player 2
                continue
            else:
                p1 = p1 + a[i]
                continue
        else:
            if a[i] % 2 != 0:
                p2 = p2 + a[i]
                flag = 1  # for changing the strike to player 1
                continue
            else:
                p2 = p2 + a[i]
                continue
    return p1, p2


if __name__ == '__main__':
    # arr = [1,2] #sample test
    arr = [1, 2, 3, 2, 1]
    n = len(arr)
    p1, p2 = countingRuns(arr, n)
    print(p1, p2)

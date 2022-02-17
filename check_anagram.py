"""
Write a code that checks if two given strings are anagrams
    Sample Input: Mary Army
    Output: Yes
"""


def checkAnagram(string1, string2):
    if sorted(string1) == sorted(string2):
        return "yes"
    else:
        return "no"


if __name__ == '__main__':
    str1 = "Mary"
    str2 = "Army"
    result = checkAnagram(str1.lower(), str2.lower())
    print(result)

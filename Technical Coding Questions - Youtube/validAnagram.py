# This file is designed to test if two given strings are valid anagrams or not.
# Two strings are anagrams if they're made of the same characters and share the same frequencies.

stringList = input().split()
setOne = set()
setTwo = set()

if len(stringList[0]) != len(stringList[1]):
    print("These words are not palindromes.")
else:
    for x in range(0, len(stringList[0])):
        setOne.add(str.lower(stringList[0][x]))
        setTwo.add(str.lower(stringList[1][x]))
    if setOne == setTwo:
        print("Congratulations, these words are palindromes")
    else:
        print("Oops, these words are not palindromes")

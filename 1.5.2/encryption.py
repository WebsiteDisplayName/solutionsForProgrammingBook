# input pg 24-25
# https://stackoverflow.com/questions/796476/displaying-windows-command-prompt-output-and-redirecting-it-to-a-file

# aeiouaeiouaeiouaeiouaeiou....................
# bcdfghjklmnpqrstvwxyzbcdfghjklmnpqrstvwxyz...

# baax => abho

# input
# 2
# baax
# aaa

from collections import defaultdict

# 5
# 21
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

if __name__ == "__main__":
    numTestCases = int(input())
    for num in range(numTestCases):
        testCase = input()
        charDict = defaultdict(int)
        outputWord = []
        for char in testCase:
            charDict[char] += 1
            charCount = charDict[char]
            if char in vowels:
                # index in string where char is located
                origPosition = vowels.index(char)
                kPosition = len(vowels)*(charCount-1) + origPosition
                consonantsPos = kPosition % len(consonants)
                outputWord.append(consonants[consonantsPos])
            elif char in consonants:
                # index in string where char is located
                origPosition = consonants.index(char)
                kPosition = len(consonants)*(charCount-1) + origPosition
                vowelsPos = kPosition % len(vowels)
                outputWord.append(vowels[vowelsPos])
        print(''.join(outputWord))

# aeioua, pos = 5
# 5 % 5 = 0

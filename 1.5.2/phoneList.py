
from collections import defaultdict

if __name__ == "__main__":
    testCases = int(input())
    for testCase in range(testCases):
        numPhoneNum = int(input())
        partialPhoneNumberDict = defaultdict(int)
        fullPhoneNumberDict = defaultdict(int)
        phoneNumList = []
        switch = 1
        for _ in range(numPhoneNum):
            phoneNum = int(input())
            if switch == 0:
                continue
            phoneNumList.append(phoneNum)
            fullPhoneNumberDict[phoneNum] = phoneNum
            if phoneNum in partialPhoneNumberDict:
                switch = 0
                continue
            for charNum in range(1, phoneNum):
                phoneNumSlice = int((str(phoneNum))[:charNum])
                if phoneNumSlice in fullPhoneNumberDict and fullPhoneNumberDict[phoneNumSlice] != phoneNum:
                    switch = 0  # No
                    print(phoneNumSlice)
                    break
                partialPhoneNumberDict[phoneNumSlice] = phoneNum

        print(phoneNumList)
        if switch == 1:
            print("Yes")
        else:
            print("No")


# 911 & 91157
# sit 1: 911 comes before
# sit 2: 911 comes after

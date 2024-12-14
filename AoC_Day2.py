print('AoC 2024, Day 2, Puzzle 1')

numbers = []
diff = 0
reportAscending = []
reportDecending = []
total = 0

def reportChecker(report):
    reportAscending = sorted(report)
    reportDecending = sorted(report, reverse=True)

    if report == reportAscending or report == reportDecending:
        for x in range(len(report)-1):
            diff = abs(report[x] - report[x+1])
            if diff == 0 or diff >3:
                safe = 0
                break
            else:
                safe = 1
    else:
        safe =  0
    if safe == 1:
        return 1
    else:
        recheckSafe = reportChecker1(report)
        if recheckSafe == 1:
            return 1
        else:
            return 0

def reportChecker1(report):
    print("enter second function")
    for y in range(len(report)):
        tempList = report.copy()
        removedValue = tempList.pop(y)
        print("tempList" + str(tempList))
        reportAscending = sorted(tempList)
        reportDecending = sorted(tempList, reverse=True)
        z = 0
        if tempList == reportAscending or tempList == reportDecending:
            safeCheck1 = 1
            for z in range(len(tempList)-1):
                diff = abs(tempList[z] - tempList[z+1])
                print("diff " + str(diff))
                if diff == 0 or diff >3:
                    print("break")
                    safeCheck1 = 0
                    break
            if safeCheck1 == 1:
                return 1
    return 0


file1 = open("./DataFiles/AoC_Day2Puzzle1.txt","r")

while True:
    line = file1.readline()
    if not line:
        break
    cleanLine = line.replace("  ", " ").split()
    numbers.clear()
    numbers.extend([int(num) for num in cleanLine])
    print(numbers)
    feedback = reportChecker(numbers)
    print(feedback)
    if feedback == 1:
        total = total + 1

print("AoC Day 1 Puzzle 2: " + str(total))



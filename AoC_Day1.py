print('AoC 2024, Day 1, Puzzle 1')

cardlist = []
columnOne = []
columnTwo = []
diff = 0

file1 = open("./DataFiles/AoC_Day1Puzzle1.txt","r")

while True:
    line = file1.readline()
    if not line:
        break
    cleanLine = line.replace("  ", " ")
    cardList = line.split()

    columnOne.append(int(cardList[0]))
    columnTwo.append(int(cardList[1]))

columnOne.sort()
columnTwo.sort()

for x in range(len(columnOne)):

    y = columnOne[x]
    z = columnTwo[x]

    diff = diff + abs(y - z)

print("AoC Day 1 Puzzle 1: " + str(diff))

y = 0
z = 0
compValue = 0
multiplier = 0
sum = 0

for x in range(len(columnOne)):
    y = 0
    multiplier = 0
    for y in range(len(columnTwo)):
        if columnOne[x] == columnTwo[y]:
            multiplier = multiplier + 1
    sum = sum + (columnOne[x] * multiplier)

print("AoC Day 1 Puzzle 2: " + str(sum))

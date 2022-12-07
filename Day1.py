testdata = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

CalsList = []
MaxCalsList = []
MaxIncrements = 0
CalSum = 0

def GetInputFile():
    return input("File Name:")

def ReadFile (filename):
    return open(filename).read()

def SearchInput (input):
    # step 1: have a variable, go to line 1, add that number to the variable, 
    # increment to the next line, check if the line is blank, if not blank add that number to 
    # your variable total, if blank then set your incrementing variable to your total, set the incrementing
    # back to 0 and begin to add the next ones, once you get to a blank check if incrementing 
    # or total variable is greater and whichever is greater becomes total
    # keep going until you go through the list
    incrementingCals = 0
    totalCals = 0

    lines = input.split("\n")
    
    for line in lines:
        if line == "":
            if incrementingCals >= totalCals:
                totalCals = incrementingCals
            CalsList.append(incrementingCals)
            incrementingCals = 0
        else:
            incrementingCals = incrementingCals + int(line)
    return totalCals,CalsList

def process():
    return SearchInput(ReadFile(GetInputFile()))

def MaxSort():
    global MaxIncrements
    global CalSum
    if MaxIncrements < 3:
        MaxCalsList.append(max(CalsList))
        CalsList.remove(max(CalsList))
        MaxIncrements = MaxIncrements + 1
        MaxSort()
    return sum(MaxCalsList)

    


print(f"{process()}")
print(f"{MaxSort()}")


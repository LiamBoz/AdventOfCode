testdate = """A Y
B X
C Z"""

lines = testdate.split("\n")

value_assignment = {'A':0, 'B':1, 'C':2,'X':0, 'Y':1, 'Z':2}

result_matrix = [[0,2,1],
                 [1,0,2],
                 [2,1,0],]

# 0 is rock 1 is paper 2 is scissor
# X is rock Y is paper Z is scissor

def GetInputFile():
    return input("File Name:")

def ReadFile (filename):
    return open(filename).read()

def victory_decision():
    for line in lines:
        values = [str(lines).split(" ")]

        choice_index_you = value_assignment.get(str(values[0]))
        choice_index_elf = value_assignment.get(str(values[1]))
        
        game_result = result_matrix[choice_index_you][choice_index_elf]

        return game_result

print(victory_decision())

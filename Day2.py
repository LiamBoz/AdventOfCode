testdate = """A Y
B X
C Z"""


value_assignment = {'A':[0,1], 'B':[1,2], 'C':[2,3],'X':[0,1], 'Y':[1,2], 'Z':[2,3]}

result_matrix = [[3,0,6],
                 [6,3,0], 
                 [0,6,3],]

# 0 is rock 1 is paper 2 is scissor
# X is rock Y is paper Z is scissor
# 1 point for rock, 2 for paper, 3 for scissors

def GetInputFile():
    return input("File Name:")

def ReadFile (filename):
    return open(filename).read()

def victory_decision(input):
    total_score = 0
    lines = input.split("\n")
    for line in lines:
        point_value = 0
        values = line.split(" ")

        choice_index_you = value_assignment.get(str(values[1]))
        choice_index_elf = value_assignment.get(str(values[0]))
        
        game_result = result_matrix[choice_index_you[0]][choice_index_elf[0]]
        point_value = game_result + choice_index_you[1]
        total_score = total_score + point_value
    return total_score


def process():
    return victory_decision(ReadFile(GetInputFile()))
print(f"{process()}")

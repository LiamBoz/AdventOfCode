testdate = """A Y
B X
C Z"""

# first is row/column of matrix, second is point value
value_assignment = {'A':[0,1], 'B':[1,2], 'C':[2,3],'X':[0,1], 'Y':[1,2], 'Z':[2,3]}

part1_matrix = [[3,0,6],
                [6,3,0], 
                [0,6,3],]
# Y is draw X is lose Z is win
part2_matrix = [[3,4,8],
                [1,5,9],
                [2,6,7],]

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
        
        game_result = part1_matrix[choice_index_you[0]][choice_index_elf[0]]
        point_value = game_result + choice_index_you[1]
        total_score = total_score + point_value
    return total_score

def victory_decision2(input):
    total_score2 = 0
    lines = input.split("\n")
    for line in lines:
        point_value = 0
        values = line.split(" ")

        choice_index_you = value_assignment.get(str(values[1]))
        win_loss_draw = value_assignment.get(str(values[0]))
        
        game_result2 = part2_matrix[win_loss_draw[0]][choice_index_you[0]]
        total_score2 += game_result2
    return total_score2

def process():
   return victory_decision2(ReadFile(GetInputFile()))
    
#print(f"{victory_decision2(input)}")

#def process():
#    return victory_decision(ReadFile(GetInputFile()))
print(f"{process()}")

field_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
field = ['1','2','3','4','5','6','7','8','9']

def player1():
    valid = False
    while not valid:
        answer1 = input('What is player O\'s move?')
        if answer1 not in field:
            valid = False
        else:
            valid = True
    field_list[int(answer1) - 1] = 'O'
    print('game status')
    print(field_list[0] + '|' + field_list[1] + '|' + field_list[2] '|' +'\n-----\n'
          + field_list[3] + '|' + field_list[4] + '|' + field_list[5] + '|' +'\n-----\n'
          field_list[6] + '|' + field_list[7] + '|' + field_list[8])


def player2():
    valid = False
    while not valid:
        answer1 = input('What is player X\'s move?')
        if answer1 not in field:
            valid = False
        else:
            valid = True
    field_list[int(answer1) - 1] = 'X'
    print('game status')
    print(field_list[0] + '|' + field_list[1] + '|' + field_list[2] +'\n-----\n'
        + field_list[3] + '|' + field_list[4] + '|' + field_list[5] +'\n-----\n'
        + field_list[6] + '|' + field_list[7] + '|' + field_list[8])
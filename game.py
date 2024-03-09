# Game

board = {
    '11': ' ', '12': ' ', '13': ' ', '14': ' ',
    '21': ' ', '22': ' ', '23': ' ', '24': ' ',
    '31': ' ', '32': ' ', '33': ' ', '34': ' ',
    '41': ' ', '42': ' ', '43': ' ', '44': ' '
}
player = 1
total_moves = 0
end_check = 0
def check():
    # Horizontally 'X'
    if board['11'] == 'X' and board['12'] == 'X' and board['13'] == 'X' and board['14'] == 'X':
        print('player one won')
        return 1
    if board['21'] == 'X' and board['22'] == 'X' and board['23'] == 'X' and board['24'] == 'X':
        print('player one won')
        return 1
    if board['31'] == 'X' and board['32'] == 'X' and board['33'] == 'X' and board['34'] == 'X':
        print('player one won')
        return 1
    if board['41'] == 'X' and board['42'] == 'X' and board['43'] == 'X' and board['44'] == 'X':
        print('player one won')
        return 1
    # Vertically 'X'
    if board['11'] == 'X' and board['21'] == 'X' and board['31'] == 'X' and board['41'] == 'X':
        print('player one won')
        return 1
    if board['12'] == 'X' and board['22'] == 'X' and board['32'] == 'X' and board['42'] == 'X':
        print('player one won')
        return 1
    if board['13'] == 'X' and board['23'] == 'X' and board['33'] == 'X' and board['43'] == 'X':
        print('player one won')
        return 1
    if board['14'] == 'X' and board['24'] == 'X' and board['34'] == 'X' and board['44'] == 'X':
        print('player one won')
        return 1
    # Diagonal 'X'
    if board['11'] == 'X' and board['22'] == 'X' and board['33'] == 'X' and board['44'] == 'X':
        print('player one won')
        return 1
    # Horizontally 0
    if board['11'] == '0' and board['12'] == '0' and board['13'] == '0' and board['14'] == '0':
        print('player two won')
        return 1
    if board['21'] == '0' and board['22'] == '0' and board['23'] == '0' and board['24'] == '0':
        print('player two won')
        return 1
    if board['31'] == '0' and board['32'] == '0' and board['33'] == '0' and board['34'] == '0':
        print('player two won')
        return 1
    if board['41'] == '0' and board['42'] == '0' and board['43'] == '0' and board['44'] == '0':
        print('player one won')
        return 1
    # Vertically 0
    if board['11'] == '0' and board['21'] == '0' and board['31'] == '0' and board['41'] == '0':
        print('player two won')
        return 1
    if board['12'] == '0' and board['22'] == '0' and board['32'] == '0' and board['42'] == '0':
        print('player two won')
        return 1
    if board['13'] == '0' and board['23'] == '0' and board['33'] == '0' and board['43'] == '0':
        print('player two won')
        return 1
    if board['14'] == '0' and board['24'] == '0' and board['34'] == '0' and board['44'] == '0':
        print('player two won')
        return 1
    # Diagonal 0
    if board['11'] == '0' and board['22'] == '0' and board['33'] == '0' and board['44'] == '0':
        print('player two won')
        return 1
    return 0
print('11|12|13|14')
print('_+_+_+_')
print('21|22|23|24')
print('_+_+_+_')
print('31|32|33|34')
print('_+_+_+_')
print('41|42|43|44')
print("*********************************")
while True:
    print(board['11'] + '|' + board['12'] + '|' + board['13'] + '|' + board['14'])
    print('_+_+_+_')
    print(board['21'] + '|' + board['22'] + '|' + board['23'] + '|' + board['24'])
    print('_+_+_+_')
    print(board['31'] + '|' + board['32'] + '|' + board['33'] + '|' + board['34'])
    print('_+_+_+_')
    print(board['41'] + '|' + board['42'] + '|' + board['43'] + '|' + board['44'])
    end_check = check()
    if total_moves == 16 or end_check == 1:
        break
    while True:
        if player == 1:
            p1_input = input('player one: ')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            else:
                print('Invalid input')
        else:
            p2_input = input('player two: ')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = '0'
                player = 1
                break
            else:
                print('Invalid input')
    total_moves += 1
    print('*************************')
    print()


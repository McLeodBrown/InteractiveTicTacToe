# Tic-tac-toe assignment
    # Initialize the board to be empty
    # X starts and chooses a position to place their marker
    # O positions their marker in any empty position
    # AFTER EACH MARKER IS PLACED, a check is made to see if either won
    # Placement alternates until a player wins or the board is full
        # at which point the game is called a tie
        
# Steps to complete assignment
    # The max number of turns that can be made is 9, so if there's more moves than that
        # the loop should break
        # There cannot be more than 9 turns so if there is not a winner
            # by then we know it is a draw
    # Because a check needs to be made for a winner after each turn,
        # we should include that check within the aforementioned loop
        # Eight possible ways to win
            # Three columns
            # Three rows
            # Two diagonals
    # X starts so we should set that outside of the loop
    # Be sure to switch roles after each check
    
# Create dictionary with each value the same as requested by assignment
board = {
    'A1': 'A1', 'B1': 'B1', 'C1': 'C1',
    'A2': 'A2', 'B2': 'B2', 'C2': 'C2',
    'A3': 'A3', 'B3': 'B3', 'C3': 'C3'
}

# Set global variables that we will incorporate into loop
# Set initial player... player X
user = 1
# Keep track of move counts
move_count = 0
# Mark 1 if winner, leave 0 if not
win = 0

def make_board(board):
    print('\n')
    print('    IAA Tic-Tac-Toe Challenge' + '\n')
    print('          #############' + '\n')
    print('       ||  ' + board['A1'] + ' | ' + board['B1'] + ' | ' + board['C1'] + ' ||'  + '\n')
    print('       ||  ' + board['A2'] + ' | ' + board['B2'] + ' | ' + board['C2'] + ' ||' + '\n')
    print('       ||  ' + board['A3'] + ' | ' + board['B3'] + ' | ' + board['C3'] + ' ||' + '\n')
    print('          #############' + '\n')

# Check all possible ways for user to have won
# Should be eight possible ways
    # Three rows, three columns, two diagonals
def check_for_winner():
    for marker in ['X', 'O']:
        # Top row
        if board['A1'] == board['B1'] == board['C1'] == marker:
            print('Yippee kay yay, player ' + marker + ' won!!')
            return True
        # Second row
        if board['A2'] == board['B2'] == board['C2'] == marker:
            print('Yippee kay yay, player ' + marker + ' won!!')
            return True
        # Third row
        if board['A3'] == board['B3'] == board['C3'] == marker:
            print('Yippee kay yay, player ' + marker + ' won!!')
            return True
        # Fist column
        if board['A1'] == board['A2'] == board['A3'] == marker:
            print('Yippee kay yay, player ' + marker + ' won!!')
            return True
        # Second column
        if board['B1'] == board['B2'] == board['B3'] == marker:
            print('Yippee kay yay, player ' + marker + ' won!!')
            return True
        # Third column
        if board['C1'] == board['C2'] == board['C3'] == marker:
            print('Yippee kay yay, player ' + marker + ' won!!')
            return True
        # Negative slope diagonal
        if board['A1'] == board['B2'] == board['C3'] == marker:
            print('Yippee kay yay, player ' + marker + ' won!!')
            return True
        # Positive slope diagonal
        if board['C1'] == board['B2'] == board['A3'] == marker:
            print('Yippee kay yay, player ' + marker + ' won!!')
            return True
    return False

while True:
    
    # Print initial board for each game
    make_board(board)
    
    # Set win variable value as result of check_for_winner function
    win = check_for_winner()
    
    # Max possible moves is 9 so if game reaches 9, it'll end
    if move_count == 9:
        print('Looks like we got ourselves a draw, cowpokes.')
        break
    # If a winner is found, the game will end
    if win == 1:
        break
    while True:
        # Start with Player 1 (aka Player X)
        if user == 1:
            # Ask Player X where they want to go
            choice = input('Player ' + str(user) + ', it is your turn. Where would you like to go? ')
            # If their choice is valid (aka in the board and available), place their mark there
            if choice in board and board[choice] == choice:
                board[choice] = 'X'
                # Move to the other user
                user = 2
                break
            else:
                print("Nope, can't go there partner. Try again with a valid position.")
                continue
        else:
            # Ask Player O where they want to go
            choice2 = input('Player ' + str(user) + ', it is your turn. Where would you like to go? ')
            # If their choice is valid (aka in the board and available), place their mark there
            if choice2 in board and board[choice2] == choice2:
                board[choice2] = 'O'
                # Move to the other user
                user = 1
                break
            else:
                # If it's a tie, print the below message
                print("Nope, can't go there partner. Try again with a valid position.")
                continue
    # Keep track of total moves... if it reaches 9, game over            
    move_count += 1
    
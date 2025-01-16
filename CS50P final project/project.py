from elements import *


# Pending
# Reset Button and reset function, Enter button  ---- Done
# Score -- Done
# Images for game rules -- Done
# Indicators -- Cancelled
# Add enter function to the README file

        
def main():
    '''
    This is the main function of the program, initializes
    the variables for the Game, generates a random answer
    Displays the structure of the game and runs the Game 
    loop to check for user input.
    '''
    
    
    # Variables
    # globals
    global row, col, answer
    row,col = 0, 0
    # Local
    guess_string = ''
    guess_count = 0
    game_result = ''
    
    # Choose a random word from the list of possible answers
    answer = choice(answers)
    answer = 'words' # For testing purposes, test with slate, house, award, words
    
    # For loop execution
    running = True 
    
    # SET BACKGROUND TO CLEAR PREVIOUS TEXT
    display_surface.fill(COLORS['background'])
    pygame.display.update()  
    
    
    # Create a grid of 5 * 6 cells on the display surface
    cells(5,6)
    
    # Reset button
    reset_button = button('Reset',SIZE['reset button'], POS['reset button'], 20, COLORS['reset button'], COLORS['shadow reset'])
    
    # Enter button
    enter_button = button('Enter', SIZE['enter button'], POS['enter button'], 30, COLORS['enter button'], COLORS['shadow enter'])

    while running:
        
        # Display Score
        button(f'Won {score}', SIZE['score button'], POS['score'], 20, COLORS['score button'], COLORS['shadow score'])
        # Event check
        for event in pygame.event.get():    
            
            # Check if window has been closed, stop program
            if event.type == pygame.QUIT:
                sys.exit() 
            # Check if the enter or reset buttons have been clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() # Get the mouse position
                # Call main() to reset the game
                if reset_button.collidepoint(mouse_pos):
                    main()
                elif enter_button.collidepoint(mouse_pos):
                    if is_guess_valid(guess_string):
                        # Increase guess count
                        guess_count += 1
                        game_result = enter(guess_string)
                        guess_string = ''
                        
                        
            # Else check if a key has been pressed, three cases
            elif event.type == pygame.KEYDOWN and game_result != 'WON' and game_result != 'LOST':
                
                # 1. Check if backspace has been pressed, delete if a letter is present
                if event.key == pygame.K_BACKSPACE and col > 0:
                    col -= 1
                    Cell(cell_pos(col,row), COLORS['cell']).draw(display_surface)
                    guess_string = guess_string[:-1]
                
                # 2. Check if an alphabet has been pressed, display and save if a cell is vacant
                elif col < 5 and event.unicode.upper() in 'QWERTYUIOPASDFGHJKLZXCVBNM' and event.unicode != '': # Use regex
                    Letter(event.unicode, text_pos(col, row)).draw(display_surface)
                    guess_string = guess_string + event.unicode.lower()
                    col += 1
                
                # 3. Check if all cells in a row are filled and Enter key has been pressed
                elif col >= 5 and event.key == pygame.K_RETURN:
                    # print("Enter pressed") # test
                    # Check if the guess is a valid word
                    if is_guess_valid(guess_string):
                        # Increase guess count
                        guess_count += 1
                        game_result = enter(guess_string)
                        guess_string = ''
                        
                        
def welcome():
    '''
    Function sets the welcome screen and waits for the user 
    to press the return key to start the game.
    '''
    # initialize the game
    pygame.init()
    global display_surface
    # create display surface
    display_surface = pygame.display.set_mode(SIZE['window'])
    

    # set caption and background color for the window
    pygame.display.set_caption("WORDLE by Danish")
    display_surface.fill(COLORS['background'])
    
    # Display image with rules of the game
    rules_image = pygame.image.load(rules_image_path).convert_alpha()
    rules_rect = rules_image.get_frect(center = POS['rules'])

    display_surface.blit(rules_image, rules_rect)
    pygame.display.update()
    
    #pygame.display.update()
    #message('WELCOME', POS['welcome message'], 70)
    #message('PRESS ENTER TO START',POS['start game'] , 30)

    # Game loop for welcome screen, returns True when return key is pressed
    while True:
        for event in pygame.event.get():
            # Check if window has been closed, stop program
            if event.type == pygame.QUIT:
                sys.exit()
            # Else check if a key has been pressed,
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: 
                return True


def message(text, pos, font_size):
    '''
    Displays a text with a given font_size as an int as a surface 
    with center given as pos in the form of a tuple. 
    '''
    try:
        font = pygame.font.Font(message_font_location, font_size)
        #font = pygame.font.Font(None, font_size)
        image = font.render(text, True, COLORS['message'])
        rect = image.get_frect(center = pos)
        display_surface.blit(image,rect)
        pygame.display.update()
        return rect
    except:
        sys.exit("message function in the program was used incorrectly")

    

def enter(guess):
    
    # Global variables are updated in this function.
    global row, col, score
    # print("Valid Guess") # test
    game_result = ''

    # Compare letters of guess with the answer and update display 
    guess_checker(guess)
    # Check if guess matches answer, game is won
    if is_solved(guess):
        game_result = 'WON'
        score += 1
        message('You Won!', POS['message1'] , 25)

    # else check if guesses are over, game is lost
    elif row >= 5:
        game_result = 'LOST'
        message('You lost!', POS['message1'], 25)
        # Show correct answer
        message(f'The correct word is {answer.upper()}', POS['message2'], 25)

    # else start next guess by incrementing the row and setting column to the start of the row
    else:
        row += 1
        col = 0
    return game_result

                        
def button(text, size, pos, font_size, color, shadow_color):
    # Box
    surf = pygame.Surface(size, pygame.SRCALPHA)
    rect = surf.get_frect(center = pos)
    #rounded rect
    pygame.draw.rect(surf, color, pygame.FRect((0,0),size), 0,4)
    
    # Shadow surf
    shadow_surf = surf.copy()
    pygame.draw.rect(shadow_surf, shadow_color, pygame.FRect((0,0),size), 0,4)
    
    # Draw Shadow
    for i in range(6):
        display_surface.blit(shadow_surf, rect.topleft + pygame.Vector2(-i,i))
    
    # Draw the main/top surface of the button
    display_surface.blit(surf,rect)
    
    # Display name of button
    font1 = pygame.font.Font(button_font_location, font_size)
    font_surf = font1.render(text, True, '#E8E1EC').convert_alpha() # Delve into use of render
    font_rect = font_surf.get_frect(center = pos)
    display_surface.blit(font_surf, font_rect)
    pygame.display.update()
    return rect
    

def cells(cols, rows):
    '''
    Creates a grid of cols * rows cells on the display surface
    The maximum number of columns is 5 and the maximum number of 
    rows is 6 on the display surface.
    Function raises a TypeError if the input is invalid
    '''
    try:
        for i in range(cols):
            for j in range(rows):
                cell = Cell(cell_pos(i, j),COLORS['cell'])
                cell.draw(display_surface)
                pygame.display.update()
        return True
    except:
        raise TypeError


def cell_pos(n,m):
    '''
    The function takes the column number and row number as input,
    returns the x and y positions for the topleft corner of the cell.
    usage: cell_pos(n,m)
    '''
    try:
        x_pos = n * SIZE['cell width'] + SIZE['left padding']
        y_pos = m * SIZE['cell width'] + SIZE['top padding']
        return (x_pos, y_pos)
    except:
        raise TypeError


def text_pos(n,m):
    '''
    The function takes the column number and row number as input,
    returns the x and y positions for the center  of the letter 
    to be diplayed.
    usage: text_pos(n,m)
    '''
    try:
        x_pos = 80 + 90 * n
        y_pos = 90 + 90 * m
        return (x_pos, y_pos)
    except:
        raise TypeError
        
                    
def is_guess_valid(text):
    '''
    checks if text is in word list- case insensitively
    usage: is_valid(text). 
    It will raise a TypeError for a non string error
    '''
    try:
        # print(text) # For testing
        if text.lower() in guesses:
            return True
        return False
    except:
        raise TypeError


def is_solved(guess):
    '''
    checks if guess matches the answer
    '''
    try:
        if guess == answer:
            return True
        return False
    except:
        raise TypeError


def update_letter(char, col, row, color):
    '''
    Updates cell and letter colors for a correctly placed letter
    '''
    # print('Col ', col, 'and' 'Row', row, 'is correctly placed')
    try:
        Cell(cell_pos(col,row),color).draw(display_surface)
        Letter(char, text_pos(col, row), COLORS['text final']).draw(display_surface)
        return True
    except:
        raise TypeError

        
def guess_checker(guess_string):
    '''
    Handles the functionality for checking a guess with the correct answer
    and corresponding screen updates
    '''    
    guess_list = list(guess_string)
    answer_copy = list(answer)
    # Iterate through each letter of guess to catch 
    # letters that match in the correct postion
    for i in range(5):
        if guess_list[i] == answer_copy[i]:
            update_letter(guess_list[i] , i, row, COLORS['cell_correct_letter'])
            guess_list[i] = ''
            answer_copy[i] = ''
        i += 1
    
    
    # Iterate through each letter of the guess again
    # to check for letters in the answer that
    # are in the wrong position
    col_check = 0
    for i in range(5):
        if len(guess_list[i]) != 0:
            for j in range(5):
                if guess_list[i] == answer_copy[j] and len(answer_copy[j]) != 0:
                    update_letter(guess_list[i], i, row, COLORS['cell_wrong_spot'])
                    guess_list[i] = ''
                    answer_copy[j] = ''
                j += 1
        i += 1
        
    col_check = 0
    for letter in guess_list:
        if len(letter) != 0:
            update_letter(letter, col_check, row, COLORS['cell_wrong_letter'])
        col_check += 1
    return True


def rules():
    # SET BACKGROUND TO CLEAR PREVIOUS TEXT
    display_surface.fill(COLORS['background'])
    pygame.display.update()
    cells(5,6)
    words = 'MUNCH'
    for i in range(5):
            update_letter(words[i], i, 0, COLORS['input text'])
    update_letter('H', 4, 0, COLORS['cell_wrong_letter'])
    while True:
        for event in pygame.event.get():
            # Check if window has been closed, stop program
            if event.type == pygame.QUIT:
                sys.exit() 

# Check if project has been called
if __name__ == '__main__':
    
    # Call welcome function
    welcome()
    
    # Call main function
    main()
    
    # Rules
    #rules()
import sys
from os.path import join
import pygame
from random import choice


score = 0

# import locations

## Images
rules_image_path = join('data', 'images', 'Rules.png')

## word files
file1_path = join('data', 'files', 'wordle_answers.txt')
file2_path = join('data', 'files', 'wordle_guesses.txt')

## fonts
button_font_location = join('data', 'fonts', 'Oxanium-Bold.ttf')
message_font_location = join('data', 'fonts','Oxanium-Regular.ttf')

 
try:
    # Load possible answers into a list
    answers = []
    with open(file1_path) as file:
        for line in file:
            answers.append(line.strip().lower())
    
    # Load allowed guesses into a list
    guesses = []
    with open(file2_path) as file:
        for line in file:
            guesses.append(line.strip().lower())
except:
    sys.exit("Word files not found")

# dict of different sizes for the program
SIZE = {
    'window' : (520, 720),
    'cell': (80, 80),
    'cell width': 90,
    'left padding': 40,
    'top padding' : 40,
    'text' : 120,
    'enter button' : (120, 60),
    'score button' : (140, 30),
    'reset button' : (80, 30)
}

# dict of colors used in the program
COLORS = {
    'background' : '#002C37', #'#121213',
    'cell' : '#F8F8F8',
    'input text' : '#121213',
    'enter button' :'#7C1137', #'#818384',
    'shadow enter':'#1F040E',
    'cell_correct_letter': '#538E4E',
    'cell_wrong_spot' : '#B5A03B',
    'cell_wrong_letter' : '#3A3A3C',
    'message' : '#DC3901',
    'text final': '#F8F8F8',
    'reset button': '#E73438',
    'shadow reset' : '#731A1C',
    'score button' : '#31d629',
    'shadow score' : '#12500F'
}

# dict of positions of different items in the program
POS = {
    'message1': (260,660),
    'message2' : (260,700),
    'welcome message' : (260, 100),
    'start game': (260,600),
    'reset button' : (100, 660),
    'enter button' : (430, 620),
    'score': (120,620),
    'rules': (260, 360),
    
}


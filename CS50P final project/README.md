> CS50 python final project
>
>Title : Wordle by Danish
>
> By Danish Mushtaq
#### Video Demo: Click [here](https://youtu.be/1uVLy6I04nQ) to check the video demo on youtube.

# Wordle - A game created using the pygame library 

Hello, world! This is CS50. I am Danish, and here is my submission for the final project for CS50's python course.
    
As a part of the requirements to complete the  assignments for the CS50's Introduction to Python Course, I had to make a final project. I decided to develop a copy of the famous online game Wordle. Wordle is a web-based word game created and developed by Welsh software engineer Josh Wardle. Players have six attempts to guess a five-letter word, with feedback given for each guess in the form of coloured tiles indicating when letters match or occupy the correct position. Source: [Wikipedia](https://en.wikipedia.org/wiki/Wordle)

The answer is choosen randomly from a list of 2315 words. The player tries to guess the answer in 6 tries. The list of allowable guesses is larger with 12,972 words. The words are spelled with the American spelling. My project allows the user to play the game with a GUI. I have used **pygame-ce** library to build the game. The project is a good learning exercise for a beginner. I tried to incorporate most of the concepts taught by David during the course. I used **Libraries**, **Classes** and **Functions**, stored data with **strings**, **lists**, **ints** and **dicts**, incorporated the use of **exceptions**, **file handling** and **tests** to build the project. Deciding to use the **pygame-ce** was a rewarding effort. I learned the use of a basic game engine and learnt the development of quite a few basic games like pong, a space shooter game along the way. 

I hope that this document, in addition to fulfilling the conditions for the completion of the course requirements, might also prove beneficial to a few future pilgrims of the programming path. The path to seek any knowledge is always a humbling experience. It has been so for me throughout my life. I understand that a lot can be said about the defects of the project and I am also aware that there are always better and more optimal ways to solve the problem but as a beginner I feel proud of having built this. With these few words, I will delve into the description of the nuts and bolts of the project.


## Requirements

The game needs the **pygame-ce** library to run. Pygame is a free and open-source cross-platform **library** for the development of multimedia applications like video games using Python. For documentation, feel free to check out this [link](https://pyga.me/docs/).

    To install the library, type the following in your terminal window,
> pip install pygame-ce

The test program for the project needs the **pytest** library to run. Official documentation for the library can be found [here](https://docs.pytest.org/en/stable/getting-started.html).
    
    To install, type the following in your terminal window,
> pip install -U pytest

## Game

### Objective
The objective of the game is to guess a random five letter word from the word list within 6 tries.

### How to play
1. After each guess, the player can either press the return key or click on the enter button to check. The color of the tiles will change to show how close the guess was to the actual answer.
+ If a letter is in the word and in the correct spot, the color of the tile turns green.
+ If a letter is in the word but not in  the correct spot, the color of the tile turns yellow.
+ If a letter is not in the word, the color of the tile turns grey.
    
2. The player can reset the game to start over by clicking on the reset button.
3. Everytime the player guesses the correct word, the score increases by a point. This is shows as the number of games won.
    

## Files

The root directory of the project contains the following files
1. `project.py`
2. `settings.py`
3. `elements.py`
4. `test_project.py`
5. `requirements.txt`
6. `README.md`

Besides these, the directory also has a **Word files** directory. It has the lists of the allowable guesses(wordle_guesses.txt) and the possible answers(wordle_answers.txt) in the game. The file **src_attrb.txt** has details on the source of these word files.
    
+ The `project.py` contains the main function of the program
+ The `settings.py` file imports the libraries needed for the program.It also loads the word files into lists that can be accessed during the execution of the program. The file also has the details for the size, position and colours of different items used in the program.
+ The `elements.py` file has the classes used in the project. The project uses two classes, the first one is for the cell object and the second one is for the letter object.
+ The `requirements.txt` file has the list of python libraries that are needed to run the project.
+ The `test_project.py` file has a few tests to test the proper working of a few functions in the **project.py** file. The tests can be run using **pytest**.
+ The `README.md` file is the current file and describes the project's working. It explains the design of the game and use of the classes and functions used in the project. It also explains how to play the game.
    
        
## Design
The first design choice I faced with the program was whether it would be Command line or a graphical interface. I have choosen the latter. This gives it a better look and was a nice learning experience using the `pygame` library.
    
The game is played on a 520 * 720 window. The game starts with a welcome screen waiting for the player to press the return key to start the game. After this, the player can see the familiar Wordle screen. As is evident from this, I have choosen not to use the indicator keys at the bottom of the cells to make it simpler to design. The screen is covered with 6 rows of 5 tiles each. As the player enters the keys, the program checks that the key entered is a character key before displaying it on the screen. After the return key is pressed, the program checks whether the guess contains five letters and if it is found in the list of admissible guesses for the game.
    
Once the above tests are satisfied, the program checks each letter of the guess with the answer and makes corresponding changes in the display. It then allows the player to enter another guess if the game is not yet won. The game ends in a loss if the player is unable to guess the correct word in 6 tries. The player the reset the game anytime during play to start the game with a new answer to guess. This is acheived by calling the `main()` function each time the reset button is clicked.
    
The game can be closed anytime by pressing of the close button for the window
    
### Classes
The project used two classes.
    
+ The `Cell` class is used to create the cell objects for the game. These are used to form the grid for the user input. It takes the position of the topleft corner of the cell and colour as arguments at the time of initialization. The cell is then drawn on the display using the `draw` method. The `draw` method takes the surface as an argument.
    
+ The `Letter` class is used to create the letter objects for the game. They are used to create the letter objects based on the user input. It takes the character, position of the center of the letter and an optional color as arguments at the time of initialization. The letters are drawn in upper case only irrespective of the case of the input character. The `draw` method then displays the letter and takes the surface as the only argument.
    
    
### Functions
Below is a brief description of the working of the various functions in the program.
    
+ The `main` function contains the event loop that checks for user input during the running of the program. It handles the control and flow of different functions of the program. The program takes keyboard input as well as mouse input. It also keeps track of the score. Global variables are quite infamous in the programming world. They are difficult to keep track of and making debugging a nightmare for the beginner programmers. In this project, I tried to limit their use. However, I ended by using a few of them anyhow. 

+ The `welcome` function handles the first screen displayed to show the rules of the game and wait for the player to begin play by pressign the return key.

+ The `message` function is used to display text on the display. It is used to show the text on the welcome screen, the result of the game and the score.

+ The `cells` function is used to display a grid of cells. It takes the number of rows and columns as the inputs.

+ The `cell_pos` function takes two integers as input which represent the column and row for the cell in the grid. The function then returns the x and y coordinates in pixels within the display for the top left corner of the cell. Each cell is 80 * 80 pixels and the distance between two adjacent cells is 10 pixels. This function has a test in `test_project.py` 

+ The `text_pos` function performs a similar function to determine the position of the center of a letter to be displayed. The function has a test in `test_project.py`.
    
+ The `is_guess_valid` function takes a 5 letter string as an input. It then checks if the text matches any of the words in the list of admissible guess, case-insentively. Returns `True` if a match is found. The `test_project.py` has a test to check this function as well.
        
+ The `guess_checker` function is at the heart of the game. It takes in the **guess_string** as an input. It first checks for exact matches between the **guess_string** and the **answer**. Then, it checks for letters in the **guess_string** that match with the **answer** but are in the wrong spot. The color of the cell is changed accordingly.
    
+ The `is_solved` function checks if the player was able to guess the correct answer.
    
+ The `button` function is used to check the buttons for reset and enter on the screen. I have also, somewhat lazily, used the same to display the **score**.
    

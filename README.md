# AlienInvasion

*What did I create?* I created a interactive game similar to Tomohiro Nishikado's Space Invaders.

### Summary of Technical Design:

The construction of the program takes an object oriented approach. The game is divided into different classes which control each aspect
of the game. The program uses Python's pygame library to display all the moving objects. This library was also usd to simplify the 
detection of collisions as well as screen boundaries. 

### Summary of the Game:

The goal of the game is to eliminate all the aliens in the screen and rack up as many points as possible. The game will keep spawning
new groups of aliens and likewise increase in difficulty. Everytime the an alien collides with a border, its direction changes and 
the alien shifts downwards. Additionally, if aliens collide with each other, their directions are changed as well. If a new highscore 
is reached the game will automatically save the score. Moreover, the user may pick the difficulty of the game at the start of the 
program. Finally, the spaceship is limited to 3 bullets at a time. 

#### Game Controls:
p - play
r - resets the game
1 - easy
2 - medium
3 - hard
Left & Right Arrowkeys - movement
Spacebar - shoot bullet
q - close game and window

### How to do play the game?
- Download the files
- Make sure you are running python3
- Run alien_invasion.py

#### Sneak Peak into the Game:
![Screen Shot 2022-01-10 at 9 01 57 PM](https://user-images.githubusercontent.com/89400862/148870843-d7f37004-ec80-4e5c-865c-3eca150c8925.png)

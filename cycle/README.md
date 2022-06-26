# Cycle
Cycle will take you back in time to a game similar to TRON. If you love snake, but hate playing alone, this game is perfect for you! As long as you have friends, or two hands, you will be able to enjoy this wonderful game!

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 cycle
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
All of the classes are in the same folder. Is it laziness, or brilliance? I think it's brilliance, but I'm too lazy to explain why.
root                    (project root folder)
+--Main - __main__.py runs this beast. Boom.
+--Action -  sets up a husk for other classes to use.
+--Actor - initializes some methods that encapsulate the different images on the screen
+--Cast - cast wraps all of the actors and objects into one beautiful place and does things with it.
+--Color - It's color, folks. Nothing interesting here.
+--Constants - A place for all the major values used to be stored.
+--ControlActorsAction - Fairly self explanitory. Keyboard input to move actors.
+--Director - This is the majority of the actual game logic. Pretty complicated, but pretty flipping sweet, Napolean.
+--DrawActorsAction - Draws the actors.
+--Keyboard_service - Left? Right? We got you covered.
+--MoveActorsAction - Allows the actors to move correctly.
+--point - Location. Probably the highest-level parent class here.
+-- README.md           (general info)
+--Script - The cast class but for actions.
+--Snake - Child of actor which makes a snake.
+--Video_service - Video things and stuff.
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* # Caleb Francis created this README


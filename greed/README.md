# Greed
Greed, for lack of a better word, is...well, it's still bad. Sorry Gordon. It's pretty bad, but this game is loads of literal non-stop fun for the whole family. It never ends! Take turns playing for 24-48-72 hours straight! Get gems, get bit-rich! It's totally worth it.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 greed
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
+--Actor - actor.py initializes some methods that encapsulate the different images on the screen
+--Cast - cast wraps all of the actors and objects into one beautiful place and does things with it.
+--Color - It's color, folks. Nothing interesting here.
+--Director - This is the majority of the actual game logic. Pretty complicated, but pretty flipping sweet, Napolean.
+--Keyboard_service - Left? Right? We got you covered.
+--Objects - This is the parent class for gems, rocks, and robots. Sounds like an 80s band.
+--point - Location. Probably the highest-level parent class here.
+-- README.md           (general info)
+--score - Score.
+--Video_service - Video things and stuff.
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* # Jer Johnson created this README. His email is joh02052@byui.edu. Bye.
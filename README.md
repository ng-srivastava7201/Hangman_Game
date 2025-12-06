# Hangman_Game
This is my 12th class Python-Tkinter and Turtle based project, where I have programme a classic game -'Hangman'.

## Outcome of the project
* Interactive gameplay among friends
* Look into play guide to know the rule
* Guess the work before the man is drawn!

## Setup and Installation
You can install Python 3.11 or a higher version on your desktop.
For the installation of the module, you can either install it in your command prompt or run the following code
```bash
  import subprocess
  import sys
  def import_or_install(module_name):
      try:
          __import__(module_name)
          pass
      except ImportError:
          print(f"The module '{module_name}' is not installed. Installing now...")
          subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
          pr int(f"'{module_name}' has been installed successfully.")
  import_or_install('tkinter')
```
This is used when we have to share the exact code on someone else's laptop and send the file as it is. This block of code checks whether the modules are pre-installed, and if not, then installs them before continuing further.

## Logic Behind word guessing
We use python's random to take a random word from category and words. Display each letter of the random word as hyphen '-'.
```bash
        global gcategory_, gword_, gword, gcategory
        gcategory = random.choice(category)
        gword = random.choice(words[gcategory])
        gcategory_ = Label(window, text= gcategory, bg="floralwhite", font = ('Arial', 15))
        gcategory_.place(y=400, x=425)
        gword_ = Label(window, text="-"*len(gword), bg='floralwhite', font=('Arial', 30))
        gword_.place(y=425, x = 425)
```
The task of reset() function are
*  Resets tries = 6
* Resets turtle drawing
* Clears previous word
* Picks new random word
* Resets all letter-button colors to blue

The task of assign_value(value) are
1. Is the guessed letter in the word?
2. If yes → reveal the letter
3. If no → reduce tries and draw a hangman body part
4. Check if the player won
5. Check if the player lost

```bash
selection = value
```
If user clicks 'A': → selection = 'A'
You also fetch the current visible word:
```bash
current_word = gword_.cget("text")
```
Example: If the player guessed some letters
current_word = "-A--E"
<br>
If letter is in the hidden word, you must reveal all matching positions.<br>
Example <br>
word = "CAKE" <br>
selection = "A"
→ Correct. Build a new version of the word.<br>
How new_word is built:<br>
Loop through each letter of the actual word:
```bash
for i, letter in enumerate(gword):
```
For each letter:
-  If it's the guessed letter → reveal it
-  Else keep the previous revealed letters
-  Otherwise put a - (dash)

Finally update:
```bash
gword_.config(text=new_word)
```

## Important Points to Remember
*  Always let the turtle complete its drawing process
*  It required, go through the 'How to Play' menu

## Find a bug?
If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above.

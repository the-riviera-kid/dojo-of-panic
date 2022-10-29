# Word Grids!

We're going to start with an easy one. :)

Write a program which asks the user to enter a word. The program will then print that word out several times, once for each letter in the word. However, on each line, a different letter should be capitalized. As an example, imagine this was a run of the program:

```
> python word-grid.py

Please enter a word: cabbage

Cabbage
cAbbage
caBbage
cabBage
cabbAge
cabbaGe
cabbagE
```
As you can see, on the first line, the first letter is capitalized. On the second line, the second letter is capitalized, and so on. Some more details:
* if the given word contains any capitals, they should not alter the output of the program
* the prompt must read "Please enter a word: " exactly
* there must be one blank line after the prompt
* i expect you to have written unit tests :)

# Getting Started

I have given you a template to get started. You'll need to create a virtual environment to work in, and install Pytest.
* `virtualenv -p python3 venv`
* `. venv/bin/activate`
* `pip install -r requirements.txt`
* Now you can run the base program with `python word-list.py`

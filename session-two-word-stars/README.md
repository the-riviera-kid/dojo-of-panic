# Word Stars!

We're going to continue with another easy one! :)

A Word Star is a thing I made up. It's a drawing of a star you make using the letters of a word. For instance, if you wanted to make a Word Star out of the word "Donkey", you'd draw this:

```
.....y.....
.....e.....
.....k.....
.....n.....
.....o.....
yeknoDonkey
.....o.....
.....n.....
.....k.....
.....e.....
.....y.....
```

And for the word "cat":

```
..t..
..a..
tacat
..a..
..t..
```

The word starts in the centre, and goes out in every cardinal direction (i.e. up, down, left and right). To make it look cooler, every other cell of the grid just contains a full-stop/period.

As you may have guessed, today you'll be writing a program to print these out. An example run of the program might be:

```
> python word-star.py

Please enter a word: BAG

..G..
..A..
GABAG
..A..
..G..
```

Just like always, you should write unit tests for your work.

# Getting Started

I have given you a template to get started. You'll need to create a virtual environment to work in, and install Pytest.
1. Create your virtual environment: `virtualenv -p python3 venv`
2. Activate it: `. venv/bin/activate`
3. Install the prequisites (which in this case, is just Pytest): `pip install -r requirements.txt`
4. Now you can run the base program with `python word-star.py`

Note that steps 1 and 3 *only* need to be done the first time you work with this project. However, you'll need to do step 2 every time you come back to this folder.

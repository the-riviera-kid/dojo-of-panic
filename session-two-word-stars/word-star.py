"""
Program to print out Word Stars!

Word Stars are totally a thing that I made up for this exercise. :) Look at the 
README.md file for more information. Don't edit this file, you won't need to.
"""

# This is importing the function you're going to write
from build_word_star import build_word_star

# This is main function of our program, where the main work happens.
# Note that this function does all the input and output; the
# build_word_star function that you'll write doesn't have to do any
# of that. Your function *shouldn't* do any of that. This is so that
# your function will be easier to test; you don't have to work out
# how to fake the user typing on the keyboard. This is a good idea
# in general, not just for this program.
def main():
    word = input('Please enter a word: ') # Assign the user's word to the "word" variable
    print() # Print a blank line
    for line in build_word_star(word): # Call your function, iterate over the return value
        print(line)

# Have you seen this before? It's a common Python thing that means
# a file can work both as a standard program, and be imported as a module.
# It's often a good idea to do this.
if __name__ == '__main__':
    main()

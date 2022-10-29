"""
Program to print out Word Grids!

Word Grids are totally a thing that I made up for this exercise. :) Look at the 
README.md file for more information.
"""

def main():
    word = input('Please enter a word: ')
    print()
    for line in build_word_grid(word):
        print(line)

def build_word_grid(word):
    """
    Builds a word grid!

    ...you didn't think it would be this easy, right? :)

    This is where your code goes. There's a file set up for your tests already.
    The function takes a string as a parameter, and will return... well,
    something. That's up to you :) You can change the main() function if you
    really want, but I've written it so that you shouldn't have to.
    """
    pass

if __name__ == '__main__':
    main()

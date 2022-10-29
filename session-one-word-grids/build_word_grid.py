def build_word_grid(word):
    lower = word.lower()
    upper = word.upper()
    for i in range(len(word)):
        yield lower[0:i] + upper[i] + lower[i+1:] 

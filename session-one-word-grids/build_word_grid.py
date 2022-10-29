def build_word_grid(word):
    lower = word.lower()
    upper = word.upper()
    result = []
    for i in range(len(word)):
        result.append( lower[0:i] + upper[i] + lower[i+1:] )
    return result

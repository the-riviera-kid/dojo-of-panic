def build_word_star(word):
    return_value = []
    grid_size = len(word) * 2 - 1
    centre_location = grid_size - len(word)
    for row_index in range(grid_size):
        row_string = ""
        for column_index in range(grid_size):
            if row_index == column_index and row_index == centre_location:
                row_string += word[0]
            elif row_index == centre_location:
                distance = abs(centre_location - column_index)
                row_string += word[distance]
            elif column_index == centre_location:
                distance = abs(centre_location - row_index)
                row_string += word[distance]
            else:
                row_string += "."
        return_value.append(row_string)

                
    return return_value

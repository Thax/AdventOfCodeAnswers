def find_index_of_character(target_string, target_character):
    if (target_string == ''):
        return -1
    index = 0
    for actual_character in target_string:
        if (actual_character == target_character):
            return index
        index += 1
    return -1
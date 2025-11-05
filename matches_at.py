def matches_at(text, pattern, p):
    comparison_number = 0
    for i in range(len(pattern)):
        comparison_number += 1
        if text[p + i] != pattern[i]: return False, comparison_number
    return True, comparison_number
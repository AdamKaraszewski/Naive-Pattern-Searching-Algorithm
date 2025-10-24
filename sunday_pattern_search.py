from matches_at import matches_at
from report import report

def init_table_for_sunday(alphabet, pattern):
    dictionary = {}
    for letter in alphabet:
        dictionary[letter] = -1
    for i in range(len(pattern)):
        dictionary[pattern[i]] = i
    return dictionary

def sunday_pattern_search(alphabet, pattern, text):
    lastp = init_table_for_sunday(alphabet, pattern)
    p = 0
    indexes_where_pattern_matches_text = []
    comparison_number = 0
    while p <= (len(text) - len(pattern)):
        does_match, comp_num = matches_at(text, pattern, p)
        comparison_number += comp_num
        if does_match:
            report(p, indexes_where_pattern_matches_text)
        p = p + len(pattern)
        if p < len(text):
            p = p - lastp[text[p]]
    return [indexes_where_pattern_matches_text, comparison_number]
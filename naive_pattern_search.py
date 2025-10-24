from matches_at import matches_at
from report import report

def naive_pattern_search(pattern, text):
    indexes_where_pattern_matches_text = []
    comparison_number = 0
    for i in range(len(text) - len(pattern) + 1):
        does_match, comp_num = matches_at(text, pattern, i)
        comparison_number += comp_num
        if does_match: report(i, indexes_where_pattern_matches_text)
    if len(indexes_where_pattern_matches_text) == 0:
        indexes_where_pattern_matches_text.append(-1)
    return [indexes_where_pattern_matches_text, comparison_number]
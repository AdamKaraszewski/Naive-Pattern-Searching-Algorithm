from report import report

def init_table(pattern):
    table = [0] * (len(pattern) + 1)
    the_longest_pref_suf = table[0] = -1
    table_inserts_number = 0
    for i in range (1, len(pattern) + 1):
        if the_longest_pref_suf > -1 and pattern[the_longest_pref_suf] != pattern[i - 1]:
            the_longest_pref_suf = table[the_longest_pref_suf]
        the_longest_pref_suf = the_longest_pref_suf + 1
        table[i] = the_longest_pref_suf
        table_inserts_number += 1
    return [table_inserts_number, table]

# Example 1.
# pref_suf represents index of the last letter of the longest pref_suf
# ABAC
# _ 0 1 2 3 4 <- |pattern| + 1 and pref_suf(_) = -1 and

# i = 1
# pref_suf(0) = 0

# i = 2
# extend 'A' to 'AB' and check if 'A' == 'B' <- try to extend pref_suf
# 'A' != 'B' - the longest pref-suf is _ => pref_suf = -1 + 1
# table[2] = pref_suf = 0
# _  0 1 2 3 4
# -1 0 0 ? ? ?

# i = 3
# extend 'AB' to 'ABA' and check if 'A' == 'A' <- try to extend pref_suf
# 'A' == 'A' - the longest pref-suf is _ => pref_suf++ // 1
# table[3] = pref_suf = 1

# i = 4
# extend 'ABA' to 'ABAC' and check if 'B' == 'C' <- try to extend pref_suf
# 'B' != 'C' - the longest available pref_suf for _ABAC_ is _ => pref_suf = -1 + 1

def morris_pratt_pattern_search(pattern, text):
    indexes_where_pattern_matches_text = []
    # crucial_operations_number, table = init_table(pattern)
    crucial_operations_number = 0
    table = init_table(pattern)[1]
    b = 0
    for i, text_letter in enumerate(text):
        # print("b: " + str(b) + " i: " + str(i) + " porównuje: " + pattern[b] + " z litera tekstu:" + text_letter)
        crucial_operations_number += 1
        while b > -1 and pattern[b] != text_letter:
            b = table[b]
            if b != -1:
                crucial_operations_number += 1
            # if b != -1: print("b: " + str(b) + " i: " + str(i) + " porównuje: " + pattern[b] + " z litera tekstu:" + text_letter)
        b += 1
        if b == len(pattern):
            report(i - len(pattern) + 1, indexes_where_pattern_matches_text)
            b = 0
    if len(indexes_where_pattern_matches_text) == 0:
        indexes_where_pattern_matches_text.append(-1)
    return [indexes_where_pattern_matches_text, crucial_operations_number]
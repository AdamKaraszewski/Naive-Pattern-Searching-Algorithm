from naive_pattern_search import naive_pattern_search as naive
from sunday_pattern_search import sunday_pattern_search as sunday

print(naive("ABA", "ACBCDABABBDB"))
print(sunday({'A', 'B', 'C', 'D'}, "ABA", "ACBCDABABBDB"))
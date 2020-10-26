import re
from collections import Counter

def count_words(word_str):
    words = Counter(re.findall(r"\b[\w'-]+\b", word_str.lower()))
    return dict(words)


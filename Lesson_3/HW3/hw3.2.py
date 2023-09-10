from collections import Counter
import string

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

text = """
A green oak tugged at a green hillock,
By a green oak, there lies a chain of gold.
And on that chain is a learned cat,
Walking to and fro all the day long:
He's walking right, he's walking left,
All the while singing a song.
"""

most_common_words = Counter(text.translate(str.maketrans('', '', string.punctuation)).lower().split()).most_common(10)

for word, count in most_common_words:
    print(word, count)

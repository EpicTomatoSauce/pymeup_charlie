import os

#open txt file in resources directory
dirname = os.path.dirname(__file__)

pyparagraph = os.path.join(dirname,"..", "Resources", "pyparagraph.txt")

with open(pyparagraph) as text:
    paragraph = text.read()

#find the number of words
words_count = len([t for t in paragraph.split(" ")])

#approximate sentence count based on the assumption that the delimiters to a sentence is ".", "!", "?"
sentence_count = len(f'{t for t in paragraph if t is "."}{t for t in paragraph if t is "!"}{t for t in paragraph if t is "?"}')
print(sentence_count)

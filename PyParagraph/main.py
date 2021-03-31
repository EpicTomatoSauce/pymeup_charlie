import os
import re

#open txt file in resources directory
dirname = os.path.dirname(__file__)

pyparagraph = os.path.join(dirname,"..", "Resources", "pyparagraph.txt")

with open(pyparagraph) as text:
    paragraph = text.read()

#find the number of words
    #words_count = [t for t in paragraph.split(" ")] - Alternative statement, re.split also works in this case
words_count = re.split(" ", paragraph)

#approximate sentence count based on the assumption that the delimiters to a sentence is ".", "!", "?"
sentence_count = re.split("(?<=[.!?]) +",paragraph)

#character count
characters = 0
for word in words_count:
    characters += len(word)

#average letter count
average_letter = round(characters / len(words_count), 1)

#average_sentence
average_sentence = round(len(words_count) / len(sentence_count), 1)

#callable message
analysis = f'Paragraph Analysis\n-------------------------------\
    \nApproximate Word Count: {len(words_count)}\
    \nApproximate Sentence Count: {len(sentence_count)}\
    \nApproximate Letter Count: {average_letter}\
    \nApproximate Sentence Length: {average_sentence}'

print(analysis)

#create analysis .txt file
output_file = os.path.join(dirname, "paragraph_analysis.txt")
with open(output_file, "w") as f:
    f.write(analysis)

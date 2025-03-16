#Programmer: Alethea Lo
#Date: 3/16/25
#Title: Word Separator

import re

def split_camel_case(sentence):
    words = re.findall(r'[A-Z][a-z]*', sentence)

    formatted_sentence = words[0] + ' ' + ' '.join(word.lower() for word in words[1:])

    return formatted_sentence

#User Input
camel_case_sentence = input("Enter a CamelCase sentence: ")

#Displaying the results
print("Formatted sentence:", split_camel_case(camel_case_sentence))
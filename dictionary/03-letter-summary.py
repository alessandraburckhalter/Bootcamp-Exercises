# Task: Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word.

user_input = str(input("\nPlease, tell me a word:\n> "))

word = {}

for letters in user_input:
    if letters in word:
        word[letters] += 1
    else:
        word[letters] =  1
print(word)

# Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text. 

sentence = str(input("\nTell me a sentence:\n> ")).lower().split()

words = []
for strings in sentence:
    word_count = sentence.count(strings)
    words.append((strings, word_count))

dict_ = dict(words)
print(dict_)

# Given a histogram tally (one returned from either letter_histogram or word_histogram), print the top 3 words or letters.
  
sort = sorted(dict_, key=dict_.get, reverse=True)
for eachline in sort[:3]:
    print(f'\n{eachline}')